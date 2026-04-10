import redis

r = redis.Redis(host="localhost", port=6379l) # use redis lib -> use Redis class to make r object

r.set("score", 100)
print(r.get("score"))

r.incr("score")
print(r.get("score"))

