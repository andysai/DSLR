import redis
ip = '10.10.250.176'
password = 'dslr#2022'

#redis默认连接db0
r1 = redis.Redis(host=ip, password=password, port=6379, db=0, decode_responses=True)
print(r1.get('name'))

