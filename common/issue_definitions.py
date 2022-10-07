ISSUE_DEFINITIONS = {
    'common': {
        'HAS_MULTIPLE_RECORDS': 
            'Occurrence Tentacle server found duplicate instances of this record',
        },
    'gbif': {
        'AMBIGUOUS_COLLECTION':
            'The given collection matches with more than 1 GrSciColl collection.',
        'AMBIGUOUS_INSTITUTION':
            'The given institution matches with more than 1 GrSciColl institution.',
        'BASIS_OF_RECORD_INVALID':
            'The given basis of record is impossible to interpret or significantly different from the recommended vocabulary.',
        'COLLECTION_MATCH_FUZZY':
            'The given collection was fuzzily matched to a GrSciColl collection.',
        'COLLECTION_MATCH_NONE':
            "The given collection couldn't be matched with any GrSciColl collection.",
        'CONTINENT_COUNTRY_MISMATCH':
            'The interpreted continent and country do not match.',
        'CONTINENT_DERIVED_FROM_COORDINATES':
            'The interpreted continent is based on the coordinates, not the verbatim string information.',
        'CONTINENT_INVALID': 'Uninterpretable continent values found.',
        'COORDINATE_ACCURACY_INVALID': 'Deprecated. ',
        'COORDINATE_INVALID':
            'Coordinate value is given in some form but GBIF is unable to interpret it.',
        'COORDINATE_OUT_OF_RANGE':
            'Coordinate has a latitude and/or longitude value beyond the maximum (or minimum) decimal value.',
        'COORDINATE_PRECISION_INVALID':
            'Indicates an invalid or very unlikely coordinatePrecision',
        'COORDINATE_PRECISION_UNCERTAINTY_MISMATCH': 'Deprecated. ',
        'COORDINATE_REPROJECTED':
            'The original coordinate was successfully reprojected from a different geodetic datum to WGS84.',
        'COORDINATE_REPROJECTION_FAILED':
            'The given decimal latitude and longitude could not be reprojected to WGS84 based on the provided datum.',
        'COORDINATE_REPROJECTION_SUSPICIOUS':
            'Indicates successful coordinate reprojection according to provided datum, but which results in a datum shift larger than 0.1 decimal degrees.',
        'COORDINATE_ROUNDED':
            'Original coordinate modified by rounding to 5 decimals.',
        'COORDINATE_UNCERTAINTY_METERS_INVALID':
            'Indicates an invalid or very unlikely dwc:uncertaintyInMeters.',
        'COUNTRY_COORDINATE_MISMATCH':
            'The interpreted occurrence coordinates fall outside of the indicated country.',
        'COUNTRY_DERIVED_FROM_COORDINATES':
            'The interpreted country is based on the coordinates, not the verbatim string information.',
        'COUNTRY_INVALID': 'Uninterpretable country values found.',
        'COUNTRY_MISMATCH':
            'Interpreted country for dwc:country and dwc:countryCode contradict each other.',
        'DEPTH_MIN_MAX_SWAPPED': 'Set if supplied minimum depth > maximum depth',
        'DEPTH_NON_NUMERIC': 'Set if depth is a non-numeric value',
        'DEPTH_NOT_METRIC':
            'Set if supplied depth is not given in the metric system, for example using feet instead of meters',
        'DEPTH_UNLIKELY': 'Set if depth is larger than 11,000m or negative.',
        'ELEVATION_MIN_MAX_SWAPPED':
            'Set if supplied minimum elevation > maximum elevation',
        'ELEVATION_NON_NUMERIC': 'Set if elevation is a non-numeric value',
        'ELEVATION_NOT_METRIC':
            'Set if supplied elevation is not given in the metric system, for example using feet instead of meters',
        'ELEVATION_UNLIKELY':
            'Set if elevation is above the troposphere (17km) or below 11km (Mariana Trench).',
        'GEODETIC_DATUM_ASSUMED_WGS84':
            'Indicating that the interpreted coordinates assume they are based on WGS84 datum as the datum was either not indicated or interpretable.',
        'GEODETIC_DATUM_INVALID': 'The geodetic datum given could not be interpreted.',
        'GEOREFERENCED_DATE_INVALID':
        "The date given for dwc':georeferencedDate is invalid and can't be interpreted at all.",
        'GEOREFERENCED_DATE_UNLIKELY': 
            'The date given for dwc:georeferencedDate is in the future or before Linnean times (1700).',
        'IDENTIFIED_DATE_INVALID':
            "The date given for dwc':dateIdentified is invalid and can't be interpreted at all.",
        'IDENTIFIED_DATE_UNLIKELY':
            'The date given for dwc:dateIdentified is in the future or before Linnean times (1700).',
        'INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS':
            'Example: individual count value > 0, but occurrence status is absent.',
        'INDIVIDUAL_COUNT_INVALID': 'The individual count value is not a positive integer',
        'INSTITUTION_COLLECTION_MISMATCH': "The collection matched doesn't belong to the institution matched.",
        'INSTITUTION_MATCH_FUZZY': 'The given institution was fuzzily matched to a GrSciColl institution.',
        'INSTITUTION_MATCH_NONE': 
            "The given institution couldn't be matched with any GrSciColl institution.",
        'INTERPRETATION_ERROR': 
            'An error occurred during interpretation, leaving the record interpretation incomplete.',
        'MODIFIED_DATE_INVALID': 'A (partial) invalid date is given for dc:modified, such as a nonexistent date, zero month, etc.',
        'MODIFIED_DATE_UNLIKELY':
            'The date given for dc:modified is in the future or predates Unix time (1970).',
        'MULTIMEDIA_DATE_INVALID': 'An invalid date is given for dc:created of a multimedia object.',
        'MULTIMEDIA_URI_INVALID': 'An invalid URI is given for a multimedia object.',
        'OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD': 'Occurrence status was inferred from basis of records',
        'OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT': 
            'Occurrence status was inferred from the individual count value',
        'OCCURRENCE_STATUS_UNPARSABLE': "Occurrence status value can't be assigned to OccurrenceStatus",
        'POSSIBLY_ON_LOAN': 'The given owner institution is different than the given institution.',
        'PRESUMED_NEGATED_LATITUDE': 'Latitude appears to be negated, e.g.',
        'PRESUMED_NEGATED_LONGITUDE': 'Longitude appears to be negated, e.g.',
        'PRESUMED_SWAPPED_COORDINATE': 'Latitude and longitude appear to be swapped.',
        'RECORDED_DATE_INVALID':
            'A (partial) invalid date is given, such as a non existing date, zero month, etc.',
        'RECORDED_DATE_MISMATCH':
            'The recorded date specified as the eventDate string and the individual year, month, day are contradictory.',
        'RECORDED_DATE_UNLIKELY':
            'The recorded date is highly unlikely, falling either into the future or representing a very old date before 1600 thus predating modern taxonomy.',
        'REFERENCES_URI_INVALID': 'An invalid URI is given for dc:references.',
        'TAXON_MATCH_FUZZY':
            'Matching to the taxonomic backbone can only be done using a fuzzy, non exact match.',
        'TAXON_MATCH_HIGHERRANK':
            'Matching to the taxonomic backbone can only be done on a higher rank and not the scientific name.',
        'TAXON_MATCH_NONE':
            'Matching to the taxonomic backbone cannot be done because there was no match at all, or several matches with too little information to keep them apart (potentially homonyms).',
        'TYPE_STATUS_INVALID':
            'The given type status is impossible to interpret or significantly different from the recommended vocabulary.',
        'ZERO_COORDINATE':
            'Coordinate is the exact 0°, 0° coordinate, often indicating a bad null coordinate.',
        },
    'idb': {
        'datecollected_bounds':
            'Date Collected out of bounds (Not between 1700-01-02 and the date of Indexing). Date Collected is generally composed from dwc:year, dwc:month, dwc:day or as specified in dwc:eventDate.',
        'dwc_acceptednameusageid_added':
            'Accepted Name Usage ID (dwc:acceptedNameUsageID) added where none was provided.',
        'dwc_basisofrecord_invalid':
            'Darwin Core Basis of Record (dwc:basisOfRecord) missing or not a value from controlled vocabulary.',
        'dwc_basisofrecord_paleo_conflict':
            'Darwin Core Basis of Record (dwc:basisOfRecord) is not FossilSpecimen but the record contains paleo context terms',
        'dwc_basisofrecord_removed':
            'Darin Core Basis of Record (dwc:basisOfRecord) removed because of invalid value.',
        'dwc_class_added':
            'Darwin Core Class (dwc:class) added where none was provided.',
        'dwc_class_replaced':
            'Darwin Core Class (dwc:class) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_continent_added':
            'Darwin Core Continent (dwc:continent) added where none was provided.',
        'dwc_continent_replaced':
            'Darwin Core Continent (dwc:continent) replaced with a standardized value.',
        'dwc_country_added': 'Darwin Core Country (dwc:country) added where none was provided.',
        'dwc_country_replaced':
            'Darwin Core Country (dwc:country) replaced with a standardized value from Getty Thesaurus of Geographic Names.',
        'dwc_datasetid_added': 'Darwin Core Dataset ID (dwc:datasetID) added where none was provided.',
        'dwc_datasetid_replaced': 'Darwin Core Dataset ID (dwc:datasetID) replaced with value from ? TBD',
        'dwc_family_added': 'Darwin Core Family (dwc:family) added where none was provided.',
        'dwc_family_replaced': 'Darwin Core Family (dwc:family) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_genus_added': 'Darwin Core Genus (dwc:genus) added where none was provided.',
        'dwc_genus_replaced':
            'Darwin Core Genus (dwc:genus) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_infraspecificepithet_added':
            'Darwin Core Infraspecific Epithet (dwc:infraspecificEpithet) added where none was provided.',
        'dwc_infraspecificepithet_replaced':
            'Darwin Core Infraspecific Epithet (dwc:infraspecificEpithet) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_kingdom_added':
            'Darwin Core Kingdom (dwc:kingdom) added where none was provided.',
        'dwc_kingdom_replaced':
            'Darwin Core Kingdom (dwc:kingdom) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_kingdom_suspect':
            'Darwin Core Kingdom (dwc:kingdom) not replaced with a standardized value from GBIF Backbone Taxonomy due to insufficient confidence level.',
        'dwc_multimedia_added': 'TBD',
        'dwc_order_added':
            'Darwin Core Order (dwc:order) added where none was provided.',
        'dwc_order_replaced':
            'Darwin Core Order (dwc:order) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_originalnameusageid_added':
            'Darwin Core Original Name Usage ID (dwc:originalNameUsageID) added where none was provided.',
        'dwc_parentnameusageid_added':
            'Darwin Core Parent Name Usage ID (dwc:parentNameUsageID) added where none was provided.',
        'dwc_phylum_added': 'Darwin Core Phylum (dwc:phylum) added where none was provided.',
        'dwc_phylum_replaced':
            'Darwin Core Phylum (dwc:phylum) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_scientificnameauthorship_added':
            'Darwin Core Scientific Name Authorship (dwc:scientificNameAuthorship) added where none was provided.',
        '*** dwc_scientificnameauthorship_replaced':
            'Darwin Core Scientific Name Authorship (dwc:scientificNameAuthorship) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_specificepithet_added':
            'Darwin Core Specific Epithet (dwc:specificEpithet) added where none was provided.',
        'dwc_specificepithet_replaced':
            'Darwin Core Specific Epithet (dwc:specificEpithet) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_stateprovince_replaced':
            'Darwin Core State or Province (dwc:stateProvince) replaced with a standardized value.',
        'dwc_taxonid_added': 'Darwin Core Taxon ID (dwc:taxonID) added where none was provided.',
        'dwc_taxonid_replaced':
            'Darwin Core Taxon ID (dwc:taxonID) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_taxonomicstatus_added':
            'Darwin Core Taxonomic Status (dwc:taxonomicStatus) added where none was provided.',
        'dwc_taxonomicstatus_replaced':
            'Darwin Core Taxonomic Status (dwc:taxonomicStatus) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_taxonrank_added': 'Darwin Core Taxon Rank (dwc:taxonRank) added where none was provided.',
        'dwc_taxonrank_invalid':
            'The supplied Darwin Core Taxon Rank (dwc:taxonRank) is not contained in controlled vocabulary (Taxonomic Rank GBIF Vocabulary).',
        'dwc_taxonrank_removed':
            'Darwin Core Taxon Rank (dwc:taxonRank) removed because it is not contained in controlled vocabulary (Taxonomic Rank GBIF Vocabulary).',
        'dwc_taxonrank_replaced':
            'Darwin Core Taxon Rank (dwc:taxonRank) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'dwc_taxonremarks_added': 'Darwin Core Taxon Remarks (dwc:taxonRemarks) added none was provided.',
        'dwc_taxonremarks_replaced':
        'Darwin Core Taxon Remarks (dwc:taxonRemarks) replaced with a standardized value from GBIF Backbone Taxonomy.',
        'gbif_canonicalname_added': 'GBIF Canonical Name added from GBIF Backbone Taxonomy.',
        'gbif_genericname_added': 'GBIF Generic Name added from GBIF Backbone Taxonomy.',
        'gbif_reference_added': 'GBIF Reference added from GBIF Backbone Taxonomy',
        'gbif_taxon_corrected':
            'A match in GBIF Backbone Taxonomy was found. Inverse of taxon_match_failed flag.',
        'gbif_vernacularname_added': 'GBIF Vernacular Name (common name) added.',
        'geopoint_0_coord': "Geographic Coordinate contains literal '0' values.",
        'geopoint_bounds':
            'Geographic Coordinate out of bounds (valid range is -90 to 90 lat, -180 to 180 long)',
        'geopoint_datum_error':
            'Geographic Coordinate Datum (dwc:geodeticDatum) is Unknown or coordinate cannot be converted to WGS84.',
        'geopoint_datum_missing':
            'Geographic Coordinate is missing Geodetic Datum (dwc:geodeticDatum) (Assumed to be WGS84).',
        'geopoint_low_precision': 'Geographic Coordinate contains a Low Precision value.',
        'geopoint_pre_flip':
            'Geographic Coordinate latitude and longitude replaced with swapped values. Prior to examining other factors, the magnitude of latitude was determined to be greater than 180, and the longitude was less than 90.',
        'geopoint_similar_coord':
            'Geographic Coordinate latitude and longitude are similar (+/- lat == +/- lon) and likely have data entry issue.',
        'idigbio_isocountrycode_added': 'iDigBio ISO 3166-1 alpha-3 Country Code added.',
        'rev_geocode_both_sign':
            'Geographic Coordinate Latitude and Longitude negated to place point in correct country.',
        'rev_geocode_corrected':
            'Geographic Coordinate placed within stated country by reverse geocoding process.',
        'rev_geocode_eez':
            "Geographic Coordinate is outside land boundaries of stated country but does fall inside the country's exclusive economic zone water boundary (approx. 200 miles from shore) based on reverse geocoding process.",
        'rev_geocode_eez_corrected':
            "The reverse geocoding process was able to find a coordinate operation that placed the point within the stated country's exclusive economic zone.",
        'rev_geocode_failure':
            'Geographic Coordinate could not be reverse geocoded to a particular country.',
        'rev_geocode_flip':
            'Geographic Coordinate Latitude and Longitude replaced with swapped values to place point in stated country by reverse geocoding process.',
        'rev_geocode_flip_both_sign':
            'Geographic Coordinate Latitude and Longitude replaced with both swapped and negated values to place point in stated country by reverse geocoding process.',
        'rev_geocode_flip_lat_sign':
            'Geographic Coordinate Latitude and Longitude replaced with swapped values, Latitude negated, to place point in stated country by reverse geocoding process.',
        'rev_geocode_flip_lon_sign':
            'Geographic Coordinate Latitude and Longitude replaced with swapped values, Longitude negated, to place it in stated country by reverse geocoding process.',
        'rev_geocode_lat_sign':
            'Geographic Coordinate Latitude negated to place point in stated country by reverse geocoding process.',
        'rev_geocode_lon_sign':
            'Geographic Coordinate had its Longitude negated to place it in stated country.',
        'rev_geocode_mismatch':'Geographic Coordinate did not reverse geocode to stated country.',
        'scientificname_added':
            'Scientific Name (dwc:scientificName) added where none was provided with the value constructed by concatenation of stated genus and species.',
        'taxon_match_failed':
            'Unable to match a taxon in GBIF Backbone Taxonomy. Inverse of gbif_taxon_corrected flag.'
  }
  }