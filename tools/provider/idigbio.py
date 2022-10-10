import csv
from http import HTTPStatus
import os

from common.issue_definitions import ISSUE_DEFINITIONS
from common.lmconstants import (
    GBIF_MISSING_KEY, Idigbio, ServiceProvider, ENCODING, DATA_DUMP_DELIMITER)
from common.s2n_type import S2nEndpoint, S2nKey, S2nSchema
from tools.fileop.logtools import (log_info)
from tools.fileop.ready_file import ready_filename

from tools.provider.api import APIQuery
from tools.s2n.utils import add_errinfo

# .............................................................................
class IdigbioAPI(APIQuery):
    """Class to query iDigBio APIs and return results"""
    
    PROVIDER = ServiceProvider.iDigBio
    OCCURRENCE_MAP = S2nSchema.get_idb_occurrence_map()

    # ...............................................
    def __init__(self, q_filters=None, other_filters=None, filter_string=None,
                 headers=None, logger=None):
        """Constructor for IdigbioAPI class
        """
        idig_search_url = '/'.join((
            Idigbio.SEARCH_PREFIX, Idigbio.SEARCH_POSTFIX,
            Idigbio.OCCURRENCE_POSTFIX))
        all_q_filters = {}
        all_other_filters = {}

        if q_filters:
            all_q_filters.update(q_filters)

        if other_filters:
            all_other_filters.update(other_filters)

        APIQuery.__init__(
            self, idig_search_url, q_key=Idigbio.QKEY, q_filters=all_q_filters,
            other_filters=all_other_filters, filter_string=filter_string,
            headers=headers, logger=logger)

    # ...............................................
    @classmethod
    def init_from_url(cls, url, headers=None, logger=None):
        """Initialize from url
        """
        base, filters = url.split('?')
        if base.strip().startswith(Idigbio.SEARCH_PREFIX):
            qry = IdigbioAPI(
                filter_string=filters, headers=headers, logger=logger)
        else:
            raise Exception(
                'iDigBio occurrence API must start with {}' .format(
                    Idigbio.SEARCH_PREFIX))
        return qry

    # ...............................................
    def query(self):
        """Queries the API and sets 'output' attribute to a JSON object
        """
        APIQuery.query_by_post(self, output_type='json')

    # ...............................................
    @classmethod
    def _standardize_record(cls, big_rec):
        newrec = {}
        to_list_fields = ('dwc:associatedSequences', 'dwc:associatedReferences')
        issue_fld = 's2n:issues'
        cc_std_fld = 'dwc:countryCode'
        view_std_fld = S2nSchema.get_view_url_fld()
        data_std_fld = S2nSchema.get_data_url_fld()

        # Outer record must contain 'data' and may contain 'indexTerms' elements
        try:
            data_elt = big_rec['data']
        except Exception as e:
            pass
        else:
            # Pull uuid from outer record
            try:
                uuid = big_rec[Idigbio.ID_FIELD]
            except:
                print('Record missing uuid field')
                uuid = None

            # Pull indexTerms from outer record
            try:
                idx_elt = big_rec['indexTerms']
            except Exception as e:
                pass
            else:
                # Pull optional 'flags' element from 'indexTerms'
                try:
                    issue_codes = idx_elt['flags']
                except Exception:
                    issue_codes = None
                try:
                    ctry_code = idx_elt['countrycode']
                except Exception:
                    ctry_code = None

                    
            # Iterate over desired output fields
            for stdfld, provfld in cls.OCCURRENCE_MAP.items():
                # Include ID fields and issues even if empty
                if provfld == Idigbio.ID_FIELD:
                    newrec[stdfld] = uuid                    
                    newrec[view_std_fld] = Idigbio.get_occurrence_view(uuid)
                    newrec[data_std_fld] = Idigbio.get_occurrence_data(uuid)
                    
                elif provfld == issue_fld:
                    newrec[stdfld] = cls._get_code2description_dict(
                        issue_codes, ISSUE_DEFINITIONS[ServiceProvider.iDigBio[S2nKey.PARAM]])
                
                elif stdfld == cc_std_fld:
                    newrec[stdfld] = ctry_code
                    
                else:
                    # all other fields are pulled from data element
                    try:
                        val = data_elt[provfld]
                    except:
                        val = None
                    
                    if val and provfld in to_list_fields:
                        lst = val.split('|')
                        elts = [l.strip() for l in lst]
                        newrec[stdfld] = elts                            
                    else:
                        newrec[stdfld] =  val
        return newrec

    # ...............................................
    def query_by_gbif_taxon_id(self, taxon_key):
        """Return a list of occurrence record dictionaries."""
        self._q_filters[Idigbio.GBIFID_FIELD] = taxon_key
        self.query()
        specimen_list = []
        if self.output is not None:
            # full_count = self.output['itemCount']
            for item in self.output[Idigbio.RECORDS_KEY]:
                new_item = item[Idigbio.RECORD_CONTENT_KEY].copy()

                for idx_fld, idx_val in item[Idigbio.RECORD_INDEX_KEY].items():
                    if idx_fld == 'geopoint':
                        new_item['dec_long'] = idx_val['lon']
                        new_item['dec_lat'] = idx_val['lat']
                    else:
                        new_item[idx_fld] = idx_val
                specimen_list.append(new_item)
        return specimen_list

    # ...............................................
    @classmethod
    def get_occurrences_by_occid(cls, occid, count_only=False, logger=None):
        """Return iDigBio occurrences for this occurrenceId.  This will
        retrieve a one or more records with the given occurrenceId.
        
        Todo: enable paging
        """
        errinfo = {}
        qf = {Idigbio.QKEY: 
              '{"' + Idigbio.OCCURRENCEID_FIELD + '":"' + occid + '"}'}
        api = IdigbioAPI(other_filters=qf, logger=logger)

        try:
            api.query()
        except Exception as e:
            errinfo = add_errinfo(errinfo, 'error', cls._get_error_message(err=e)) 
            std_out = cls.get_api_failure(
                S2nEndpoint.Occurrence, HTTPStatus.INTERNAL_SERVER_ERROR,
                errinfo=errinfo)
        else:
            errinfo = add_errinfo(errinfo, 'error', api.error)
            std_out = cls._standardize_output(
                api.output, Idigbio.COUNT_KEY, Idigbio.RECORDS_KEY, Idigbio.RECORD_FORMAT, 
                S2nEndpoint.Occurrence, query_status=api.status_code, 
                query_urls=[api.url], count_only=count_only, errinfo=errinfo)
        
        return std_out

    # ...............................................
    @classmethod
    def _write_idigbio_metadata(cls, orig_fld_names, meta_f_name):
        pass

    # ...............................................
    @classmethod
    def _get_idigbio_fields(cls, rec):
        """Get iDigBio fields
        """
        fld_names = list(rec['indexTerms'].keys())
        # add dec_long and dec_lat to records
        fld_names.extend(['dec_lat', 'dec_long'])
        fld_names.sort()
        return fld_names

#     # ...............................................
#     @classmethod
#     def _count_idigbio_records(cls, gbif_taxon_id):
#         """Count iDigBio records for a GBIF taxon id.
#         """
#         api = idigbio.json()
#         record_query = {
#             'taxonid': str(gbif_taxon_id), 'geopoint': {'type': 'exists'}}
# 
#         try:
#             output = api.search_records(rq=record_query, limit=1, offset=0)
#         except Exception:
#             log_info('Failed on {}'.format(gbif_taxon_id))
#             total = 0
#         else:
#             total = output['itemCount']
#         return total
# 
#     # ...............................................
#     def _get_idigbio_records(self, gbif_taxon_id, fields, writer,
#                              meta_output_file):
#         """Get records from iDigBio
#         """
#         api = idigbio.json()
#         limit = 100
#         offset = 0
#         curr_count = 0
#         total = 0
#         record_query = {'taxonid': str(gbif_taxon_id),
#                         'geopoint': {'type': 'exists'}}
#         while offset <= total:
#             try:
#                 output = api.search_records(
#                     rq=record_query, limit=limit, offset=offset)
#             except Exception:
#                 log_info('Failed on {}'.format(gbif_taxon_id))
#                 total = 0
#             else:
#                 total = output['itemCount']
# 
#                 # First gbifTaxonId where this data retrieval is successful,
#                 # get and write header and metadata
#                 if total > 0 and fields is None:
#                     log_info('Found data, writing data and metadata')
#                     fields = self._get_idigbio_fields(output['items'][0])
#                     # Write header in datafile
#                     writer.writerow(fields)
#                     # Write metadata file with column indices
#                     _meta = self._write_idigbio_metadata(
#                         fields, meta_output_file)
# 
#                 # Write these records
#                 recs = output['items']
#                 curr_count += len(recs)
#                 log_info(('  Retrieved {} records, {} recs starting at {}'.format(
#                     len(recs), limit, offset)))
#                 for rec in recs:
#                     rec_data = rec['indexTerms']
#                     vals = []
#                     for fld_name in fields:
#                         # Pull long, lat from geopoint
#                         if fld_name == 'dec_long':
#                             try:
#                                 vals.append(rec_data['geopoint']['lon'])
#                             except KeyError:
#                                 vals.append('')
#                         elif fld_name == 'dec_lat':
#                             try:
#                                 vals.append(rec_data['geopoint']['lat'])
#                             except KeyError:
#                                 vals.append('')
#                         # or just append verbatim
#                         else:
#                             try:
#                                 vals.append(rec_data[fld_name])
#                             except KeyError:
#                                 vals.append('')
# 
#                     writer.writerow(vals)
#                 offset += limit
#         log_info(('Retrieved {} of {} reported records for {}'.format(
#             curr_count, total, gbif_taxon_id)))
#         return curr_count, fields

    # ...............................................
    def assemble_idigbio_data(
            self, taxon_ids, point_output_file, meta_output_file, 
            missing_id_file=None, logger=None):
        """Assemble iDigBio data dictionary"""
        if not isinstance(taxon_ids, list):
            taxon_ids = [taxon_ids]

        # Delete old files
        for fname in (point_output_file, meta_output_file):
            if os.path.exists(fname):
                log_info(
                    'Deleting existing file {} ...'.format(fname), logger=logger)
                os.remove(fname)

        summary = {GBIF_MISSING_KEY: []}

        ready_filename(point_output_file, overwrite=True)
        with open(point_output_file, 'w', encoding=ENCODING, newline='') as csv_f:
            writer = csv.writer(csv_f, delimiter=DATA_DUMP_DELIMITER)
            fld_names = None
            for gid in taxon_ids:
                # Pull / write field names first time
                pt_count, fld_names = self._get_idigbio_records(
                    gid, fld_names, writer, meta_output_file)

                summary[gid] = pt_count
                if pt_count == 0:
                    summary[GBIF_MISSING_KEY].append(gid)

        # get/write missing data
        if missing_id_file is not None and len(
                summary[GBIF_MISSING_KEY]) > 0:
            with open(missing_id_file, 'w', encoding=ENCODING) as out_f:
                for gid in summary[GBIF_MISSING_KEY]:
                    out_f.write('{}\n'.format(gid))

        return summary

    # ...............................................
    def query_idigbio_data(self, taxon_ids):
        """Query iDigBio for data
        """
        if not isinstance(taxon_ids, list):
            taxon_ids = [taxon_ids]

        summary = {GBIF_MISSING_KEY: []}

        for gid in taxon_ids:
            # Pull/write fieldnames first time
            pt_count = self._count_idigbio_records(gid)
            if pt_count == 0:
                summary[GBIF_MISSING_KEY].append(gid)
            summary[gid] = pt_count

        return summary

