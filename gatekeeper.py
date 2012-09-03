import os
import urlparse
from datetime import datetime

from redis import StrictRedis

from flask import Flask, abort, jsonify, request
app = Flask(__name__)

HEROKU = 'HEROKU' in os.environ

if HEROKU:
    urlparse.uses_netloc.append('redis')
    redis_url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
    redis = StrictRedis(
        host=redis_url.hostname,
        port=redis_url.port,
        password=redis_url.password
    )
else:
    redis = StrictRedis()


@app.route('/locks/')
def all_locks():
    locks = []
    for lock in redis.keys():
        locks.append(redis.hgetall(lock))
    return jsonify(locks=locks)


@app.route('/locks/<env>/', methods=['GET', 'POST', 'DELETE'])
def environment_lock(env):
    if request.method == 'GET':
        if redis.exists(env):
            return jsonify(redis.hgetall(env))
        else:
            abort(404)
    if request.method == 'POST':
        if redis.exists(env):
                abort(409)
        else:
            redis.hset(env, 'environment', env)
            redis.hset(env, 'owner', request.form['user'])
            redis.hset(env, 'since', datetime.now())
            redis.hset(env, 'message', request.form.get('message'))
            return jsonify(redis.hgetall(env))
    if request.method == 'DELETE':
        if redis.exists(env):
            redis.delete(env)
            return ''
        else:
            abort(404)

if __name__ == '__main__':
    if not HEROKU:
        app.debug = True

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
