from flask import Flask
import redis



app = Flask(__name__)
cache = redis.StrictRedis(host-'localhost', portd=6379, db=0)
cache.set(default_key, 'one')

@app.route('/')
def hello_world():
    return 'hello mini'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
