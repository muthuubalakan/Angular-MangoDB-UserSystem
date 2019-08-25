# Angular-MangoDB-UserSystem

Simple aiohttp User-login system using AngularJs routing and MongoDB

## Installation

```python
pip3 install -r requirements.txt
```

## Database
The application is configured with MongoDB env to store and perform queries in NoSQL.

MongoDB configuration is really simple. Provide the MongoDB URI in conf.json file.

TODO: 
1. Make ssl connection between server and database. 
2. Update, delete users.


If you don't want to connect to mongoDB with URI,  username, password and db server instead,
you will find following code snippet useful.

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
