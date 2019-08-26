from python:3
env PYTHONUNBUFFERED 1

env http_proxy
env https_proxy 

run mkdir /aioapp
workdir /aioapp
copy requirements.txt /aioapp
run pip install -r requirements.txt
copy . /aioapp/

cmd ["python", "run.py"]