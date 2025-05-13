from flask import Flask  # type: ignore
import redis
import os

app = Flask(__name__)
# Get Redis config from environment
redis_host = os.environ.get("REDIS_HOST", "localhost")
# Connect to Redis
redis_port = int(os.environ.get("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, db=0)


@app.route("/")
def home():
    return "Welcome to my DevOps app!"


@app.route("/health")
def health():
    return "Health is Okay!", 200


@app.route("/visits")
def visit():
    try:
        count = r.incr("counter")
        return f"Number of visits: {count}"
    except redis.exceptions.ConnectionError:
        return "Could not connect to Redis", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
