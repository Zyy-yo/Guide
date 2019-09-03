```python
'''
pickle提供了一个简单的持久化功能，可以将对象以文件的形式存储在硬盘上，这个过程就是数据的序列化
同时，存储的文件也可以用python读取，实现了反序列化的功能
通过pickle模块的序列化操作我们可以将程序运行中的对象信息保存到文件中，永久存储
通过反序列化操作，我们可以在文件中创建上一次程序保存的对象
'''
```




    '\npickle提供了一个简单的持久化功能，可以将对象以文件的形式存储在硬盘上，这个过程就是数据的序列化\n同时，存储的文件也可以用python读取，实现了反序列化的功能\n通过pickle模块的序列化操作我们可以将程序运行中的对象信息保存到文件中，永久存储\n通过反序列化操作，我们可以在文件中创建上一次程序保存的对象\n'




```python
# 写入   基本步骤和文档相同，也是要open，再写入，之后close
import pickle
test = open(r'D:\PY\文本文档\data.pkl','wb')          # 后缀名.pkl，模式用'wb'，它会自己创建这个文件
m = {'name':'上海火车站', 'year':2019, 'address':'上海市...'}
pickle.dump(m,test)              # pickle.dump() ，第一个参数是要写入的对象，第二个参数是文件
test.close()           # 同样，关闭文件

# 执行之后，文件夹里已经生成了data.pkl的文件，用记事本打开是乱码状态，我们来读取试试看

# 读取

test2 = open(r'D:\PY\文本文档\data.pkl','rb')            # 首先open，打开文件，模式用'rb'
data = pickle.load(test2)                    # 读取，用pickle.load()，参数是上面的文件变量
test2.close()
print(data)

# pickle存储的对象会保留原有的数据格式
```

    {'name': '上海火车站', 'year': 2019, 'address': '上海市...'}
    
