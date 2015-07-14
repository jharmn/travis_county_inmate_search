# Travis county inmate search
Uses SOAP service and public mugshot images from Travis county to download all mugshots

## Configure
``` bash
virtualenv venv
. venv/bin/active
```

## Generate list of folders
Scrapes folder with directory listing to produce text list
``` bash
python sites.py > sites.txt
```

## Download mugshots
Uses sites.txt to spider all mugshot images
``` bash
./scraper.sh
```

## Call SOAP service
** Not currently working, issue in WSDL **
``` bash
python search.py
```
