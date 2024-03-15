import redis
ip = '10.12.12.150'
password = 'dslr#2024'

#redis默认连接db0
r1 = redis.Redis(host=ip, password=password, port=6379, db=0, decode_responses=True)
print(r1.get('name'))

