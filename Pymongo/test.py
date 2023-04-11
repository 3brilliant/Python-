from pymongo import *

# 创建连接
client = MongoClient()

# 创建数据库或访问
db = client.pymongo_test

# 创建student集合
s = db.student

# 向集合中插入一条文档
result1 = s.insert_one({'name':'lisi','sex':'nan'})

# 向集合中插入多条文档,通过列表的形式
result2 = s.insert_many([{'name':'lisi','sex':'nan'},{'age':12}])

print('result1的结果为:',result1)
print('result2的结果为:',result2)

# 查询所有文档对象
result3 = s.find()

# 对跟新前返回的结果进行取出
for column1 in result3:
    print('更新前取出结果为:',column1)

# 更新一条数据，多条数据一样的原理，这里就不过多的阐述了
s.update_one({'age':12},{'$set':{'age':21}})

# 查询更新后的所有文档对象
result4 = s.find()

# 对更新后的数据进行取出
for column2 in result4:
    print('更新后取出结果为:',column2)


# 删除数据
# s.delete_many({})