# Python-PDF

pdf generator that create pdf files from html
in this project i made the hard path easy

## Features

- async
- auto several pages
- sample for watermark, fonts, css and extra
- pydentic and fully documented
- base on python 3.10

## for starting project with docker

```bash
docker-compose up --build
```

## for starting project with simple venv

```bash
python -m venv venv
source venv/bin/activate
(venv) python -m pip install --upgrade pip
(venv) python -m pip install -r requirements.txt
(venv) uvicorn main:app
```

## for poetry project setup

```bash
python -m venv venv
source venv/bin/activate
(venv) python -m pip install --upgrade pip poetry
(venv) python -m poetry run uvicorn main:app
```

## some personal notes

i used my coworker html css, and i just don't have any clue the best html and css
so do not get mad at, and instead contribute.

i solved the watermark problem in this project, so others can use the trick or make boiler plate out of this
and i hope it helps you in a way.

Thanks
