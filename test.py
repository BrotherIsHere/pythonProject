import redis

pool = redis.ConnectionPool(host="192.168.188.100", port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# r.set("k1","v1")
# print(r.get("k1"))
# r.set("k1","vv1")
# print(r.get("k1"))
# if r.setnx("k14","v2"):
#     print(1)
#     print(r.get("k14"))
# else:
#     print(2)
#     print(r.get("k1"))
# r.mset({"a":"v1","b":"v2"})
# print(r.mget("a","b"))
# print(r.keys())
# t(r.getrange("cn_name",0,1))
# r.set("foo",123)
# print(r.get("foo"))
# r.incr("foo",amount=3)
# print(r.get("foo"))
r.hset("ha1", "id", "12")
# print(r.hget("ha1","id"))
# r.hset("ha1","name","lining")
# print(r.hmget("ha1","name","id"))
# print(r.hkeys("ha1"))
# print(r.hvals("ha1"))
# r.hset("ha1", mapping={"k4": "4", "k5": "r"})
# print(r.hmget("ha1",["name","id","k2","k1"]))
# print(r.hgetall("ha1"))
# print(r.hexists("ha1","k1"))
# print(r.hscan("ha1"))
# r.lpush("li1", 11, 33, "ll", "p")
# print(r.lrange("li1", 0, -1))
r.flushdb()
r.linsert("li1","before",11,"abc")
print(r.lindex("li1",2))
print(r.lrange("li1",0,-1))
print(r.keys())

