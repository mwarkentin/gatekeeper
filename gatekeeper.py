import logging
import os
import urlparse
from datetime import datetime

from flask import Flask, abort, jsonify, request
from redis import StrictRedis

from decorators import token_required

app = Flask(__name__)

redis = StrictRedis.from_url(os.getenv('REDIS_URL'))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
app.logger.addHandler(stream_handler)

# Keys which should not be considered locks
LOCK_BLACKLIST = ('ElastiCacheMasterReplicationTimestamp', )


@app.route('/locks/')
def all_locks():
    locks = []
    for lock in redis.keys():
        # Skip blacklisted keys
        if lock in LOCK_BLACKLIST:
            continue

        print "Looping through locks:"
        print "  lock: {}".format(lock)
        print "    {}".format(redis.hgetall(lock))
        locks.append(redis.hgetall(lock))
    return jsonify(locks=locks)


@app.route('/locks/<env>/', methods=['GET', 'POST', 'DELETE'])
@token_required
def environment_lock(env):
    if request.method == 'GET':
        print "Checking for lock: {}".format(env)
        if redis.exists(env):
            print "  Found: {}".format(redis.hgetall(env))
            return jsonify(redis.hgetall(env))
        else:
            print "  Not found."
            abort(404)
    if request.method == 'POST':
        if redis.exists(env):
                abort(409)
        else:
            redis.hset(env, 'environment', env)
            redis.hset(env, 'owner', request.json.get('user'))
            redis.hset(env, 'since', datetime.now())
            redis.hset(env, 'message', request.json.get('message'))
            return jsonify(redis.hgetall(env))
    if request.method == 'DELETE':
        if redis.exists(env):
            redis.delete(env)
            return ''
        else:
            abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
