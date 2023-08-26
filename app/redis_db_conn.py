

import redis
import logging
from .constants import HOST, PORT, DB, DECODE_RESPONSE

try:
    # Connect to Redis server
    redis_client = redis.StrictRedis(host=HOST, port=PORT, db=DB, decode_responses=DECODE_RESPONSE)

except Exception:
    
    logging.info('Some Error Occured :: {}'.format(Exception))