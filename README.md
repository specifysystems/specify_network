# Welcome to the Specify Network!

The Specify Network consists of tools and services to serve the Specify Collections 
Consortium.  There are currently several elements in production, and some still in 
development.

## Specify Cache
The Specify Cache stores records submitted by Specify Collections for public access via 
the Specify-assigned GUID, held in the DarwinCore occurrenceID field.  It holds records
for Specify collections without a public endpoint for each record.

## Specify Resolver
The Specify Resolver retrieves the URL of a Specify record given the Specify-assigned 
GUID, held in the DarwinCore occurrenceID field.  Specify 6 records are 
served from the Specify cache, if they have been exported to the Specify Network.  
Specify 7 records can be accessed directly from the Specify 7 webserver if the server  
has been made public.

### Specify Cache and Resolver API documentation
The Specify Cache and Resolver web services are documented using the
[Open API 3 spec](https://swagger.io/specification/).  The raw documentation can be
found at [/docs/openapi.yml](/docs/openapi.yml) and a version rendered with Swagger can
be found at https://specifysystems.github.io/specify_cache/.


## Syftorium (in development)
![Logo](static/syftorium.png)

The Syftorium is in development, and will be a collection of specimen-based analytics 
assessing the composition of collection holdings and available species information. 

These data are used to compare and assess collections against and among the collective 
holdings globally distributed data.  The analytics are then returned to the 
contributing institutions and others to assist those collections in prioritizing
collecting and digitization efforts, institutional loans, mergers, deaccessions, and 
more, to improve, the overall quality of the collection.  This information can also be 
used by the community as a whole to identify gaps in species knowlege or redundancies.  

The Syftorium presents this information in multivariate-, but subsettable, space 
to provide as much value and feedback to the community as possible.


# Specify Network Deployment

To run the containers, generate `fullchain.pem` and `privkey.pem` (certificate
and the private key) using Let's Encrypt and put these files into the
`./lmsyft/config/` directory.

While in development, you can generate self-signed certificates:

```zsh
openssl req \
  -x509 -sha256 -nodes -newkey rsa:2048 -days 365 \
  -keyout ./config/privkey.pem \
  -out ./config/fullchain.pem
```

To run the production container, or the development container with HTTPs
support, generate `fullchain.pem` and `privkey.pem` (certificate and the private
key) using Let's Encrypt and put these files into the `./config/`
directory.

### Production

Modify the `FQDN` environment variable in `.env.conf` as needed.

Run the containers:

```zsh
docker compose up -d
```

lmsyft is now available at [https://localhost/](https://localhost:443)

#### Process DWCAs

You can setup a cron job to process pending DWCAs.

See `./cron/lmsyft_process_dwcas_cron.in`.

Note, you many need to modify `lmsyft-sp_cache-1` to reflect your container
name.

### Development

Run the containers:

```zsh
docker compose -f docker-compose.yml -f docker-compose.development.yml up
```

lmsyft is now available at [http://localhost/](http://localhost:443).

Flask has hot-reload enabled.

#### Configuring Debugger

Debugger configuration is IDE dependent. [Instructions for
PyCharm](https://kartoza.com/en/blog/using-docker-compose-based-python-interpreter-in-pycharm/)

`runner` container is running `debugpy` on port `5001` and `sp_cache` on
port `5002`.
