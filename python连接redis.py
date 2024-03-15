from rediscluster import RedisCluster

# 假设Redis集群节点的IP和端口信息如下
startup_nodes = [
    {"host": "10.10.250.236", "port": "30379"},
    {"host": "10.10.250.248", "port": "30379"},
    {"host": "10.10.250.249", "port": "30379"}
]

# 连接到Redis集群
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# 设置键值对
rc.set("foo", "bar")

# 获取键的值
value = rc.get("foo")
print(value)  # 输出: bar

# 关闭连接
rc.connection_pool.disconnect()