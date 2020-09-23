#  Updraft Python assignment

## Assignment
```

Build a microservice that has an API that can receive a list of transactions, and returns the following:

    1.  The calendar month by calendar month overdraft fees on the account
    2.  The interest rate each calendar month shown as an annual percentage rate

```


## Solution
Developed in Python 3.8.1
- Is a Flask App
- Restplus for API marhsalling


## Installing
 create a venv
```
Christophers-MacBook-Pro:rabo christopherbrown$ python3 -m venv updraft:
```
activate venv and clone https://github.com/cbrown24/blog-starter.git
```
Christophers-MacBook-Pro-2:office_app christopherbrown$ source bin/activate

(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ git clone https://github.com/cbrown24/blog-starter.git src

Cloning into 'src'...

remote: Enumerating objects: 62, done.

remote: Counting objects: 100% (62/62), done.

remote: Compressing objects: 100% (45/45), done.

remote: Total 62 (delta 16), reused 52 (delta 11), pack-reused 0

Unpacking objects: 100% (62/62), done.

(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ cd src/
```

pip install
```
(office_app) Christophers-MacBook-Pro-2:src christopherbrown$ pip install -r requirements.txt
Collecting alembic==1.3.2 (from -r requirements.txt (line 1))
... snip ...
```

DB setup
```
(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ pwd

/Users/christopherbrown/Documents/testing_app/office_app
### set app environment
(office_app) Christophers-MacBook-Pro-2:office_app christopherbrown$ export FLASK_APP=BLOG_STARTER:app


### Now run the db migration to setup tables and the admin user
(office_app) Christophers-MacBook-Pro-2:blog-starter christopherbrown$ python manage.py db upgrade

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.

INFO  [alembic.runtime.migration] Will assume non-transactional DDL.

INFO  [alembic.runtime.migration] Running upgrade  -> c292fb06f01d, empty message
```


## Testing Using Swagger 
Startup using
```
python manage.py run
```
- Unfortunately due to time constraints,  automated testing is not included in this project.
- This application can be tested using the swagger UI which is available on localhost:5000/api
- Please generate a JWT Authorization token using the login endpoint.
- The response will give you an Authorization token which can be stored and used to authenticate agains other endpoints.
- Please click the authorise padlock icon in the top right hand corner of the SwaggerUI page to store this token.
- All endpoints requiring authorisation will subsequently use this token.


## Demo
use curl to create a topic
```
(office_app) Christophers-MacBook-Pro-2:blog-starter christopherbrown$ curl -X POST "http://127.0.0.1:5000/topic/" -H "accept: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk2MDE1ODIsImlhdCI6MTU3OTUxNTE3Nywic3ViIjoxfQ.URmm0eBdMJHeyU6ywdX2Gmpgz2AC6F0cxDtVQAMX_s8" -H "Content-Type: application/json" -d "{ \"name\": \"test_topic\"}"
```


create a post in a topic
```
curl -X POST "http://127.0.0.1:5000/post/" -H "accept: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk2MDE1ODIsImlhdCI6MTU3OTUxNTE3Nywic3ViIjoxfQ.URmm0eBdMJHeyU6ywdX2Gmpgz2AC6F0cxDtVQAMX_s8" -H "Content-Type: application/json" -d "{ \"title\": \"string\", \"body\": \"string\", \"topic_id\": 1}"
```

read topic
```
curl -X GET "http://127.0.0.1:5000/topic/" -H "accept: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk2MDE1ODIsImlhdCI6MTU3OTUxNTE3Nywic3ViIjoxfQ.URmm0eBdMJHeyU6ywdX2Gmpgz2AC6F0cxDtVQAMX_s8" 
[{
"name": "test_topic",
"created_by": null,
"created_on": null,
"posts": [
{
"created_by": "unknown",
"created_on": "2020-01-20T10:50:36.707717",
"title": "string",
"body": "string",
"topic_id": 2
}
],
"id": 2
}]
```


## Unfinished items
- add comments to blog
- unit + functional testing
- pycodestlye / pep8
