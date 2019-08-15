NoSQL:MongoDB ———— 非关系型数据库管理系统

关系型数据库管理系统与mongodb中的概念对应关系：
    数据库 - 数据库
    表格 - 集合
    行 - 文档   （一条数据）
    列 - 字段

mongodb默认有三个数据库：
    admin：从权限的角度来看，这是‘root’数据库，若将一个用户添加到这个数据库，这个用户自动继承所有
        数据库的权限。
    local：可以用来存储仅限于本地单台服务器的任意集合，永远不会被复制
    config：待补充

数据库表/集合：collection

数据记录行/文档：document
    文档是一组键值对（key-value)
    文档中的键值对是有序的
    不能有重复键
    键是字符串，除特殊情况，键可以使用任意utf-8字符
    区分类型和大小写
    
    {"author":"liuwei","time":20190814}

数据字段/域：field
索引：index
主键：primary key

mongodb数据类型
    string      字符串，在mongodb中，utf-8编码的字符串才是合法的
    integer     整型数值，用于存储数值
    boolean     布尔值
    double      双精度浮点值，用于存储浮点值
    timestamp   时间戳，记录文档修改或添加的具体时间
    min/max keys    将一个值与BSON(二进制的JSON)元素的最低值/最高值相对比
    array       用于将数组或列表或多个值存储为一个键
    object      用于内嵌文档
    null        用于创建空值
    symbol      符号，该数据类型基本上等同于字符串类型，但是它一般用于采用特殊符号类型的语言
    date        日期时间
    objectID   对象id，用于创建文档的id
    binary data 用于存储二进制数据
    code        代码类型，用于在文档中存储JavaScript代码
    regular expression  存储正则表达式

后续如何使用mongodb
    python做数据采集 → 存储数据进入mongodb
    通过pymongo，调用mongo数据进行分析、处理
    可以通过python导出本地文件，或者以新的集合继续存入mongodb

基本语法
    数据库：
        创建数据库：use database_name，有则切换到该数据库，无则创建
        删除数据库：db.dropDatabase()，首先切换到需要删除的数据库
        查看当前数据库：db
        查看所有数据库：show dbs
    集合：
        创建集合：db.createCollection(name,options) name要加双引号
        查看已有集合：show collections 或 show tables
        删除集合：db.collection.drop() 待补充
    文档：
        插入文档：db.colletion_name.insert(document) 或 db.colletion_name.insertOne(document)
        查看已插入文档：db.collection_name.find();db.collection_name.find().pretty()
        删除文档：db.collection.remove(<query>,<justOne>) 待补充
    数据导入导出
        从csv文件导入：在cmd里进入mongoimport.exe程序：要写bin的完整路径，后面接上命令：
            mongoimport -d test -c table03 --type csv --headerline --file 文件路径
            -d test 数据库名 test
            -c table03 集合名 table03

        数据库导出csv文件：在cmd里进入mongoexport.exe程序，后面接上命令：
             mongoexport -d test -c table03 --type csv -f"_id,等要导出的字段"--out 路径 (测试时
             总出现位置参数太多的错误提示，直接使用python更方便)

        python实现数据导入导出
            DataFrame.to_dict(orient='')输出字典列表，再通过insert_many()导入数据库
            orient参数有：
                dict    :默认；{column-> {index -> value}}
                list    :{column->[value]}
                series  :{column -> Series(values)}
                split   :{'index'->[index],'columns'->[columns],'data'->[values]}
                records :推荐；[{column->value},...,{column->value}]
                index   :{index->{column->value}} 

Python中使用mongodb
    创建MongoClient对象，连接mongo：
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    查看现有数据库：
        myclient.list_database_names()
    读取数据库：
        db = myclient[数据库名] 或 myclient.数据库名
    查看现有集合：
        db.list_collection_names()
    读取集合：
        table = db[集合名] 或 db.集合名
    查询文档：
        result = table.find()   输出可迭代对象，想要打印出来，可以for循环，或封装为list格式
        result = table.find_one()   查询单条数据，输出字典
    插入文档：
        insert_one()    插入单个文档
        insert_many()   通过字典列表插入多个文档
    删除文档：
        delete_one()    删除单个文档
        delete_many()   删除多个文档
    删除集合：
        table.drop()

基于爬虫的Mongodb运用
    get_data(ui,d_h,d_c,table)  通过函数做数据采集并入库
        ui:数据信息网页
        d_h:user-agent信息
        d_c:cookies信息
        table:mongo集合对象


