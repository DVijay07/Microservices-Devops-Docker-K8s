
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def home():
    count = cache.incr('hits')
    return f'Hello! This page has been visited {count} times.'

app.run(host="0.0.0.0", port=5000)