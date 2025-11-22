from flask import Flask
import redis
import os
import time

class DummyRedis:
    def __init__(self):
        self.count = 0
    def incr(self, key):
        self.count += 1
        return self.count
    def ping(self):
        return True

app = Flask(__name__)

# Connect to redis container with retry logic
def get_redis_connection():
    redis_host = os.getenv('REDIS_HOST', 'redis')
    for attempt in range(5):
        try:
            r = redis.Redis(host=redis_host, port=6379, decode_responses=True)
            r.ping()
            return r
        except redis.ConnectionError:
            if attempt < 4:
                time.sleep(1)
            continue
    # Fallback to in-memory counter so app still runs
    return DummyRedis()

r = get_redis_connection()

@app.route('/')
def home():
    count = r.incr('hits')
    # Detect dummy fallback by attribute check
    if isinstance(r, DummyRedis):
        return f"(Fallback) No Redis reachable. Local count: {count}", 200
    return f"Hello! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
