# Angular-MangoDB-UserSystem

Simple aiohttp User-login system using AngularJs routing and MongoDB

## Installation

```python
pip3 install -r requirements.txt
```

## MongoDB configuration
The module pymongo is used to configure and connect db.

You can connect to the database server locally or a cloud service. 

Edit the conf.json file and add database uri, and database name.

Or you could configure database by following steps,

```python3
import pymongo


connection = pymongo.MongoClient(host, port)
db = connection[db_name]
db.authenticate(username, password)
customer_db = db[collection_name]
```

## usage

```
python3 run.py
```
