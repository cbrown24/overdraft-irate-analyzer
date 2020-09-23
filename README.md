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
python3 -m venv updraft
```
activate venv and clone https://github.com/cbrown24/updraft.git
```
ChristohersMBP2:test_updraft_solution christopherbrown$ python3 -m venv updraft
ChristohersMBP2:test_updraft_solution christopherbrown$ cd updraft/
ChristohersMBP2:updraft christopherbrown$ source bin/activate
(updraft) ChristohersMBP2:updraft christopherbrown$ pwd
/Users/christopherbrown/Documents/test_updraft_solution/updraft
(updraft) ChristohersMBP2:updraft christopherbrown$ git clone https://github.com/cbrown24/updraft.git
Cloning into 'updraft'...
remote: Enumerating objects: 29, done.
remote: Counting objects: 100% (29/29), done.
remote: Compressing objects: 100% (22/22), done.
remote: Total 29 (delta 2), reused 29 (delta 2), pack-reused 0
Unpacking objects: 100% (29/29), done.
(updraft) ChristohersMBP2:updraft christopherbrown$ cd updraft/src
```

pip install
```
(updraft) ChristohersMBP2:src christopherbrown$ pip install -r requirements.txt 
Collecting alembic==1.3.2 (from -r requirements.txt (line 1))
Collecting aniso8601==8.0.0 (from -r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/eb/e4/787e104b58eadc1a710738d4e418d7e599e4e778e52cb8e5d5ef6ddd5833/aniso8601-8.0.0-py2.py3-none-any.whl
Collecting attrs==19.3.0 (from -r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/a2/db/4313ab3be961f7a763066401fb77f7748373b6094076ae2bda2806988af6/attrs-19.3.0-py2.py3-none-any.whl
Collecting bcrypt==3.1.7 (from -r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/62/20/4c94f3f8dfc6b8720c8bc903ce2951ec6397ad864e3a64b4abdced014514/bcrypt-3.1.7-cp34-abi3-macosx_10_6_intel.whl
Collecting cffi==1.13.2 (from -r requirements.txt (line 5))
  Using cached https://files.pythonhosted.org/packages/cf/bb/a3f00f4eccec9a3bdaaf31f5c0261f34888284dc6760495d2d6f82dec0c5/cffi-1.13.2-cp38-cp38-macosx_10_9_x86_64.whl
Collecting Click==7.0 (from -r requirements.txt (line 6))
  Using cached https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl
Collecting cryptography==2.8 (from -r requirements.txt (line 7))
  Using cached https://files.pythonhosted.org/packages/6b/4a/ce93178469d4460d6b3a5e648fc1a2f426030f3d30a12d7ed4df73d044de/cryptography-2.8-cp34-abi3-macosx_10_6_intel.whl
... snip ...
```

## Testing Using Swagger 
Startup using
```
python manage.py run
e.g:
(updraft) ChristohersMBP2:src christopherbrown$ python manage.py run
 * Serving Flask app "app.main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 252-960-147

```

## Demo
curl generated from swagger ui
```
(updraft) ChristohersMBP2:fixtures christopherbrown$ pwd
/Users/christopherbrown/Documents/test_updraft_solution/updraft/updraft/src/test/fixtures
(updraft) ChristohersMBP2:fixtures christopherbrown$  curl -X POST "http://localhost:5000/overdraft/file/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@15475-ba.json;type=application/json"
{
    "status": "success",
    "message": "Summary complete",
    "data": [
        {
            "name": "apr",
            "data": [
                {
                    "date": "2020-08-31",
                    "value": 0.009150716113899024
                },
                {
                    "date": "2020-07-31",
                    "value": 0.007255815085524479
                },
                {
                    "date": "2020-06-30",
                    "value": 0.004164296831268787
                },
                {
                    "date": "2020-05-31",

```

## Automated Testing
```
(updraft) ChristohersMBP2:src christopherbrown$ pwd
/Users/christopherbrown/Documents/test_updraft_solution/updraft/updraft/src
(updraft) ChristohersMBP2:src christopherbrown$ pytest 
================================================== test session starts ==================================================
platform darwin -- Python 3.8.1, pytest-6.0.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/christopherbrown/Documents/test_updraft_solution/updraft/updraft/src
collected 2 items                                                                                                       

test/test_01_txn_unit.py ..                                                                                       [100%]

=================================================== warnings summary ====================================================
/Users/christopherbrown/Documents/test_updraft_solution/updraft/lib/python3.8/site-packages/flask_restplus/fields.py:17
  /Users/christopherbrown/Documents/test_updraft_solution/updraft/lib/python3.8/site-packages/flask_restplus/fields.py:17: DeprecationWarning: The import 'werkzeug.cached_property' is deprecated and will be removed in Werkzeug 1.0. Use 'from werkzeug.utils import cached_property' instead.
    from werkzeug import cached_property

/Users/christopherbrown/Documents/test_updraft_solution/updraft/lib/python3.8/site-packages/flask_restplus/model.py:8
  /Users/christopherbrown/Documents/test_updraft_solution/updraft/lib/python3.8/site-packages/flask_restplus/model.py:8: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
    from collections import OrderedDict, MutableMapping

-- Docs: https://docs.pytest.org/en/stable/warnings.html
============================================= 2 passed, 2 warnings in 0.27s =============================================

```


## Unfinished items
- Complete Test coverage
- setup to auto generate Sphinx docs

## How will this be deployed ? 
- I dont offer much experienve in Zappa or deploying to AWS/Azure. I have worked with Heroku's CLI tools to deploy aftifacts to Heroku containers. Zappa looks very attractive and would be keen to learn more.
- Most of my experience is deploying via Jenkins CD job which pulls a frozen artifact from the firms defined artifact repository. In many cases this is Artifactory.

## How would I automate in CI/CD environment ? 
- Use Jenkins or another CI tool (I started with Cruise Control for Ruby years ago), which will trigger a build if all the unit + functional tests complete succesfully. I would also incorproate pylint, code-smell and code coverage checks before the pytest run
- We should have subsequent CI jobs which facilitate promotion to given environment once appropriate control gates are passed (e.g test on QA/UAT environment)
- The CI release jobs which also facilitate composition of documentation/release notes
