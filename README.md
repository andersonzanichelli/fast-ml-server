# Fast Rest API to Iris ML
An example of rest api using Fast API to use a machine learning model.

## Create a virtual environment
```
$ virtualenv fastvenv
$ source fastvenv/bin/activate
```

## Installing the dependencies
```
$ pip install -r requirements.txt
```

## Running the APP
- Localy
```
$ uvicorn main:app --host=127.0.0.1 --port=5000
```

## Docs
Api docs automatically generated

http://localhost:5000/docs

http://localhost:5000/redoc

http://localhost:5000/openapi.json


## Dockerized
```
$ docker build --tag fast-ml-server .
$ docker run fast-ml-server:latest
```

## Utility Commands
To check lib versions
```
$ pip list
```