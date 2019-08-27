# Aio-User-System

Simple aiohttp User-login system using AngularJs routing and MongoDB

## Installation

### Dependencies

python 3.5+

```python
pip3 install -r requirements.txt
```
## Dockerize
check if docker is installed in your system.

#### Build

If you are behind proxy, set proxy env in Dockerfile. Or else remove env.
```bash
docker build -t aio-app:latest .
```
Start container

**docker run -d -p 8080:8080 aio-app**

TODO: 
1. Write a docker compose for the service. Define networks for db and backend.

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
Don't write a custon ODM for just user login. Pymongo provides rich tools.


## Running locally

```
python3 run.py
```
