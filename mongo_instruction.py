import pymongo
import pandas as pd

# 连接mongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# 查询现有数据库
print(myclient.list_database_names())
# 连接数据库，有则连接，无则创建
db = myclient.myNewDatabase
# 查询现有集合
print(db.list_collection_names())
# 连接集合，有则连接，无则创建
table = db.train0

# 创建数据库
db1 = myclient['仓鼠']
table1 = db1['基本数据']
# 创建完之后，在compass里并没有显示，只有插入文档之后才会真正创建
# 插入数据前此代码可以让集合以更新的形式插入数据，而不是重复插入
table1.delete_many({})

# 插入一条文档，当多次运行，就会多次插入同一条数据，可以在插入之前写一行代码来处理这个问题
cs = {'eyes_color':'black', 'hair_color':'brown and white', 'length':7.8, 'weight':45}
table1.insert_one(cs)
# 插入多条文档1，mongodb属于非关系型数据库管理，cs1中第三条数据多了一个键值对，也可以成功插入
cs1 = [{'eyes_color':'black', 'hair_color':'black', 'length':7.57, 'weight':42},
        {'eyes_color':'black', 'hair_color':'white', 'length':7.7, 'weight':48},
        {'eyes_color':'black', 'hair_color':'brown and white', 'length':6.6, 'weight':35, 'age_year':1}]
for i in cs1:
    table1.insert_one(i)
# 插入多条文档2
table1.insert_many(cs1)

# 查询集合里的文档1
result = list(table1.find())
print(result)
# 查询集合里的文档2
for j in table1.find():
        print(j)


# 利用pandas实现excel数据导入到数据库
df = pd.read_excel(r"D:\PY\excel_file\constellation_cleaned.xlsx")
datalst = df.to_dict(orient='records')
# 创建数据库和集合
db2 = myclient['星座']
table2 = db2['2019年7月']
# 将数据插入集合
table2.insert_many(datalst)
