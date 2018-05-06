# import redis
# r = redis.StrictRedis(host='tx.zorelu.win', port=6379, db=0,password='123123zz')
# r.set('foo', 'bar')
# print(r.get('foo'))
#
###ConnectionPool
import redis

pool = redis.ConnectionPool(host='tx.zorelu.win',password='123123zz',port=6379)

r = redis.Redis(connection_pool=pool)
r.set('name','Yu chao')
print(r.get('name'))