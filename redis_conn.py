import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

redis_client.set('address', 'Azamgarh')

value = redis_client.get('address')

# if we want to see the data in proper way then we use utf-8 in decode method

print(value.decode('utf-8'))
