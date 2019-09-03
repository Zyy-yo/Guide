```python
'''
pandas —— 数据分析核心工具包

基于numpy构建，为数据分析而存在。

数据结构Series,可以看作是一维的数组；Dataframe,可以看作是二维数组（它们都属于数据结构，属于同一层级的关系，这里只是方便理解）

可直接读取数据并做处理（高效简单）

兼容各种数据库

支持各种分析算法

'''
```




    '\npandas —— 数据分析核心工具包\n\n基于numpy构建，为数据分析而存在。\n\n数据结构Series,可以看作是一维的数组；Dataframe,可以看作是二维数组（它们都属于数据结构，属于同一层级的关系，这里只是方便理解）\n\n可直接读取数据并做处理（高效简单）\n\n兼容各种数据库\n\n支持各种分析算法\n\n'




```python
# Series 数据结构
# 是带有标签的一维数组，可以保存任何数据类型（整数，字符串，浮点数，Python对象等）,轴标签统称为索引

import numpy as np
import pandas as pd

s = pd.Series(np.random.rand(5))
print(s, type(s))

print(s.index, type(s.index))         # .index属性查看Series索引，类型为rangeindex
print(s.values, type(s.values))       # .values查看series值，类型是ndarray

'''
核心：series相比于ndarray，是一个自带索引index的数组 → 一维数组 + 对应索引
所以当只看series的值的时候，就是一个ndarray
series和ndarray较相似，索引切片功能差别不大
series和dict相比，series更像一个有顺序的字典（dict本身不存在顺序），其索引原理与字典相似（一个用key，一个用index）
'''

print(s[2:4])
s[0] = 100
s[3:] = 200
print(s)

s2 = pd.Series(np.random.randn(10),index=range(1,11))
print(s2)
s2[5] = 100            # 用index来索引
print(s2)
```

    0    0.014750
    1    0.503750
    2    0.194202
    3    0.543016
    4    0.927176
    dtype: float64 <class 'pandas.core.series.Series'>
    RangeIndex(start=0, stop=5, step=1) <class 'pandas.core.indexes.range.RangeIndex'>
    [0.0147503  0.50375015 0.19420169 0.54301637 0.92717649] <class 'numpy.ndarray'>
    2    0.194202
    3    0.543016
    dtype: float64
    0    100.000000
    1      0.503750
    2      0.194202
    3    200.000000
    4    200.000000
    dtype: float64
    1     0.735373
    2     0.466664
    3    -1.225433
    4    -0.361148
    5     0.352472
    6    -0.241559
    7     0.490592
    8     0.821595
    9     1.388064
    10    0.676488
    dtype: float64
    1       0.735373
    2       0.466664
    3      -1.225433
    4      -0.361148
    5     100.000000
    6      -0.241559
    7       0.490592
    8       0.821595
    9       1.388064
    10      0.676488
    dtype: float64
    


```python
# 创建Series 
# 方法一：由字典创建，字典的key就是index，values就是values

dic = {'a':1,'b':2,'c':3,'d':4}
s = pd.Series(dic)
print(s)


dic1 = {'a':1,'b':2,'c':3,'d':4,'e':'hello','f':[3,8],'g':{0:10}}
s1 = pd.Series(dic1)
print(s1)

  # values可以是任意数据类型，此时Series的数据类型就变成了对象object
```

    a    1
    b    2
    c    3
    d    4
    dtype: int64
    a          1
    b          2
    c          3
    d          4
    e      hello
    f     [3, 8]
    g    {0: 10}
    dtype: object
    


```python
# 创建Series 
# 方法二：由数组创建(一维数组)
ar = np.random.randn(5)
s = pd.Series(ar)
print(ar, s, sep='\n')

s1 = pd.Series(ar, index=list('abcde'),dtype=np.object)   # 创建Series时可以设置index和dtype(此处我设置dtype=np.int不管用)
print(s1)

print(s1[:].astype(np.int))         # 这种方法可以改变Series的数据类型，返回新的Series    
```

    [-0.34223972  1.23162784  0.11722298  0.66656205 -0.5729891 ]
    0   -0.342240
    1    1.231628
    2    0.117223
    3    0.666562
    4   -0.572989
    dtype: float64
    a    -0.34224
    b     1.23163
    c    0.117223
    d    0.666562
    e   -0.572989
    dtype: object
    a    0
    b    1
    c    0
    d    0
    e    0
    dtype: int32
    


```python
# 创建Series 
# 方法三：由标量创建

s = pd.Series(10)     # 注意，此处必须提供index，否则只会出现一个值
print(s)

s1 = pd.Series(10, index=range(5))     # 标量会重复，来匹配索引的长度
print(s1)
```

    0    10
    dtype: int64
    0    10
    1    10
    2    10
    3    10
    4    10
    dtype: int64
    


```python
# Series 名称属性：name

s1 = pd.Series(np.random.randn(5))
print(s1)
print('-'*50)
s2 = pd.Series(np.random.randn(5),name='test')    # name为Series的一个参数，创建一个数组的名称
print(s2)
print('-'*50)

print(s1.name, s2.name, type(s2.name))       # .name：输出数组的名称，输出格式为str，如果没定义名称，输出为None
print('-'*50)
  
s3 = s2.rename('haha')        # .rename()重命名一个数组的名称，并且指向一个新数组，原数组不变
print(s3)
print('-'*50)

print(s2.name, s3.name)



```

    0    1.011934
    1    0.447185
    2   -0.081442
    3   -0.109112
    4    1.432715
    dtype: float64
    --------------------------------------------------
    0    0.199055
    1    0.945141
    2    0.637731
    3   -0.740200
    4   -0.810908
    Name: test, dtype: float64
    --------------------------------------------------
    None test <class 'str'>
    --------------------------------------------------
    0    0.199055
    1    0.945141
    2    0.637731
    3   -0.740200
    4   -0.810908
    Name: haha, dtype: float64
    --------------------------------------------------
    test haha
    


```python
# 作业
# 分别由字典、数组的方式，创建以下要求的Series

dic = {'Jack':90, 'Marry':92, 'Tom':89, 'Zack':65}    # 字典创建
s1 = pd.Series(dic, name='作业1',dtype=float)
print(s1)

ar = np.array([90,92,89,65],dtype=float)        # 数组创建
s2 = pd.Series(ar, index=['Jack','Marry','Tom','Zack'], name='作业1')
print(s2)
```

    Jack     90.0
    Marry    92.0
    Tom      89.0
    Zack     65.0
    Name: 作业1, dtype: float64
    Jack     90.0
    Marry    92.0
    Tom      89.0
    Zack     65.0
    Name: 作业1, dtype: float64
    


```python
'''
Pandas数据结构Series：索引

位置下标 / 标签索引 / 切片索引 / 布尔型索引
'''
```




    '\nPandas数据结构Series：索引\n\n位置下标 / 标签索引 / 切片索引 / 布尔型索引\n'




```python
# 位置下标，类似序列

s = pd.Series(np.random.rand(5))
print(s)

print(s[0], type(s[0]), s[0].dtype)    # 注意这里s[0]是numpy.float64类型
print(float(s[0]), type(float(s[0])))    # 可以通过float()转换为python float格式


  # numpy.float 与python float占用字节不同
# index是数字的时候，直接print(s[-1])会出现错误，但是可以用切片
print(s[:-1])
```

    0    0.559265
    1    0.391840
    2    0.747910
    3    0.370566
    4    0.510996
    dtype: float64
    0.5592645631143631 <class 'numpy.float64'> float64
    0.5592645631143631 <class 'float'>
    0    0.559265
    1    0.391840
    2    0.747910
    3    0.370566
    dtype: float64
    


```python
# 标签索引
s2 = pd.Series(np.random.randn(5), index=list('abcde'))
print(s2)
print(s2['a'], type(s2['a']), s2['a'].dtype)
s3 = s2[['b','e']]          # 选择带有多个标签的值，需要用[[]]来表示，结果是新的Series
print(s3, type(s3))

    # 此时index是字符串
```

    a    1.987204
    b    1.277399
    c    0.174604
    d    0.671785
    e    0.242950
    dtype: float64
    1.9872040630405543 <class 'numpy.float64'> float64
    b    1.277399
    e    0.242950
    dtype: float64 <class 'pandas.core.series.Series'>
    


```python
# 切片索引
ar = np.random.rand(5)
s1 = pd.Series(ar)
s2 = pd.Series(ar, index=list('abcde'))

print(s1[1:4], s1[4])
print('-'*50)

print(s2['a':'c'], s2['c'])       # 标签索引，末端包含
print('-'*50)

print(s2[0:3], s2[3])         # 位置索引，左闭右开
print('-'*50)

print(s2[:-1])      # 下标索引做切片，写法和列表一样，左闭右开
print(s2[::2])         # 步长2
print(s2[-1])       # 当index是字符串的时候，可以用s2[-1]来索引到最后一个值
```

    1    0.117480
    2    0.433264
    3    0.551919
    dtype: float64 0.07314175161747338
    --------------------------------------------------
    a    0.347287
    b    0.117480
    c    0.433264
    dtype: float64 0.4332637556236588
    --------------------------------------------------
    a    0.347287
    b    0.117480
    c    0.433264
    dtype: float64 0.5519190441524567
    --------------------------------------------------
    a    0.347287
    b    0.117480
    c    0.433264
    d    0.551919
    dtype: float64
    a    0.347287
    c    0.433264
    e    0.073142
    dtype: float64
    0.07314175161747338
    


```python
# 布尔型索引

s = pd.Series(np.random.randn(5)*100)
s[4] = None       # 添加一个空值
print(s)

b1 = s > 50
b2 = s.isnull()                 # .isnull()    空值返回True
b3 = s.notnull()                # .notnull()      非空值返回True

print(b1, type(b1), b1.dtype)
print(b2, type(b2), b2.dtype)
print(b3, type(b3), b3.dtype)

   # 数组做判断之后，返回的是一个由布尔值组成的新的数组
    # .isnull() / .notnull() 判断是否为空值 (None代表空值，NaN代表有问题的数值，两个都会识别为空值)

print('-'*50)

print(s[s < 30])
print(s[b3])
   # 布尔型索引方法：用[判断条件]表示，其中判断条件可以是 一个语句，或者是 一个布尔型数组！
```

    0   -72.193222
    1    11.260394
    2    23.002014
    3   -59.141536
    4          NaN
    dtype: float64
    0    False
    1    False
    2    False
    3    False
    4    False
    dtype: bool <class 'pandas.core.series.Series'> bool
    0    False
    1    False
    2    False
    3    False
    4     True
    dtype: bool <class 'pandas.core.series.Series'> bool
    0     True
    1     True
    2     True
    3     True
    4    False
    dtype: bool <class 'pandas.core.series.Series'> bool
    --------------------------------------------------
    0   -72.193222
    1    11.260394
    2    23.002014
    3   -59.141536
    dtype: float64
    0   -72.193222
    1    11.260394
    2    23.002014
    3   -59.141536
    dtype: float64
    


```python
# 作业
# 创建一个Series，包含10个元素，且每个值为0-100的均匀分布随机值，index为a-j，请分别筛选出：
# ① 标签为b，c的值为多少
# ② Series中第4到6个值是哪些？
# ③ Series中大于50的值有哪些？

ar = np.random.rand(10)*100
s = pd.Series(ar, index=list('abcdefghij'))
print(s)
print('-'*20)

print(s[['b','c']])       # 标签为b，c的值
print('-'*50)

print(s[3:6])           # 第4到6个值
print('-'*50)

print(s[s>50])         # 大于50的值
```

    a    55.282575
    b    70.190754
    c    70.357434
    d    53.192149
    e    39.680635
    f    30.800810
    g    34.490367
    h    43.103612
    i    51.953012
    j    52.869864
    dtype: float64
    --------------------
    b    70.190754
    c    70.357434
    dtype: float64
    --------------------------------------------------
    d    53.192149
    e    39.680635
    f    30.800810
    dtype: float64
    --------------------------------------------------
    a    55.282575
    b    70.190754
    c    70.357434
    d    53.192149
    i    51.953012
    j    52.869864
    dtype: float64
    


```python
'''
Pandas数据结构Series：基本技巧

数据查看 / 重新索引 / 对齐 / 添加、修改、删除值

'''
```


```python
# 数据查看

s = pd.Series(np.random.rand(50))
print(s.head(10))
print(s.tail())

# .head()查看头部数据
# .tail()查看尾部数据
# 默认查看5条
```

    0    0.029442
    1    0.964736
    2    0.746534
    3    0.451289
    4    0.808858
    5    0.406253
    6    0.160435
    7    0.921571
    8    0.741789
    9    0.086006
    dtype: float64
    45    0.518455
    46    0.818324
    47    0.962800
    48    0.046575
    49    0.178300
    dtype: float64
    


```python
# 重新索引  reindex
# .reindex()将会根据索引重新排序，如果当前索引不存在，则引入缺失值

s = pd.Series(np.random.rand(5), index=list('abcde'))
print(s)
print('-'*30)

s1 = s.reindex(['c','b','a','D','e'])      
print(s1)
   # .reindex()中也是写列表
   # 这里'D'索引不存在，所以值为NaN

s2 = s.reindex(['c','b','a','D','e'], fill_value=0)       # fill_value参数：填充缺失值的值
print(s2)
```

    a    0.982636
    b    0.181197
    c    0.464494
    d    0.613954
    e    0.820201
    dtype: float64
    ------------------------------
    c    0.464494
    b    0.181197
    a    0.982636
    D         NaN
    e    0.820201
    dtype: float64
    c    0.464494
    b    0.181197
    a    0.982636
    D    0.000000
    e    0.820201
    dtype: float64
    


```python
# Series  对齐
a1 = np.random.rand(3)
s1 = pd.Series(a1, index=['Jack','Marry','Tom'])
s2 = pd.Series(a1, index = ['Wang','Jack','Marry'])
print(s1)
print('-'*30)
print(s2)
print('-'*30)
print(s1+s2)

'''
Series 和 ndarray 之间的主要区别是，Series 上的操作会根据标签自动对齐：
    index顺序不会影响数值计算，以标签来计算
    缺失值也不会影响计算，只要一方缺失，则计算结果就是缺失值
'''
```

    Jack     0.030170
    Marry    0.837090
    Tom      0.340762
    dtype: float64
    ------------------------------
    Wang     0.030170
    Jack     0.837090
    Marry    0.340762
    dtype: float64
    ------------------------------
    Jack     0.867260
    Marry    1.177852
    Tom           NaN
    Wang          NaN
    dtype: float64
    


```python
# 删除  .drop

s = pd.Series(np.random.rand(5), index=list('kdald'))    # 发现index可以重复
print(s)
s1 = s.drop('k')      # 默认inplace=False,删除元素之后返回新的Series
print(s1)

s.drop('d',inplace=True)       # inplace=True,就地操作，直接改变原Series
print(s)

s2 = s.drop(['a','l'])         # 删除多个标签及其值
print(s2)
```

    k    0.213151
    d    0.285280
    a    0.806598
    l    0.263909
    d    0.709608
    dtype: float64
    d    0.285280
    a    0.806598
    l    0.263909
    d    0.709608
    dtype: float64
    k    0.213151
    a    0.806598
    l    0.263909
    dtype: float64
    k    0.213151
    dtype: float64
    


```python
# 添加

s1 = pd.Series(np.random.rand(5))
s2 = pd.Series(np.random.rand(5), index=list('kdald'))
print(s1)
print(s2)
print('='*20)

s1[5] = 100
s2['C'] = 100
          # 直接通过下标索引/标签index添加值
print(s1)
print(s2)

s3 = s1.append(s2)       # .append()方法，直接添加一个Series
print(s3)
```

    0    0.754753
    1    0.953537
    2    0.337932
    3    0.110627
    4    0.134661
    dtype: float64
    k    0.255794
    d    0.179987
    a    0.512569
    l    0.773891
    d    0.469427
    dtype: float64
    ====================
    0      0.754753
    1      0.953537
    2      0.337932
    3      0.110627
    4      0.134661
    5    100.000000
    dtype: float64
    k      0.255794
    d      0.179987
    a      0.512569
    l      0.773891
    d      0.469427
    C    100.000000
    dtype: float64
    0      0.754753
    1      0.953537
    2      0.337932
    3      0.110627
    4      0.134661
    5    100.000000
    k      0.255794
    d      0.179987
    a      0.512569
    l      0.773891
    d      0.469427
    C    100.000000
    dtype: float64
    0         0.754753
    1         0.953537
    2         0.337932
    3         0.110627
    4         0.134661
    5       100.000000
    aaa    1111.000000
    dtype: float64
    


```python
# 修改   通过索引或切片直接修改，类似序列
s = pd.Series(np.random.rand(5), index=list('abcde'))
print(s)

s['a'] = 100
s[['b','c']] = -200
print(s)

print('-'*30)

s['c':'e'] = 25
print(s)
```

    a    0.550547
    b    0.448815
    c    0.506037
    d    0.827600
    e    0.219851
    dtype: float64
    a    100.000000
    b   -200.000000
    c   -200.000000
    d      0.827600
    e      0.219851
    dtype: float64
    ------------------------------
    a    100.0
    b   -200.0
    c     25.0
    d     25.0
    e     25.0
    dtype: float64
    


```python
# 作业
# 1. 如图创建Series，并按照要求修改得到结果(10个元素，0-9，索引‘a-j')

ar = np.arange(10)
s = pd.Series(ar, index=list('abcdefghij'))
print(s)

# 删除第二个值

s1 = s.drop('b')

# 修改'a''e''f'为100

s1[['a','e','f']] = 100

print(s1)
```

    a    0
    b    1
    c    2
    d    3
    e    4
    f    5
    g    6
    h    7
    i    8
    j    9
    dtype: int32
    a    100
    c      2
    d      3
    e    100
    f    100
    g      6
    h      7
    i      8
    j      9
    dtype: int32
    


```python
# 2. 已有s1，s2（值为0-10的随机数），请求出s1+s2的值

s1 = pd.Series(np.random.rand(5)*10, index=list('abcde'))
s2 = pd.Series(np.random.rand(5)*10, index=list('cdefg'))
print(s1)
print(s2)

print('-'*30)
print(s1+s2)
```

    a    5.594130
    b    5.906033
    c    8.333152
    d    0.840407
    e    3.307386
    dtype: float64
    c    5.928550
    d    8.242786
    e    4.065885
    f    5.112033
    g    7.257388
    dtype: float64
    ------------------------------
    a          NaN
    b          NaN
    c    14.261702
    d     9.083194
    e     7.373271
    f          NaN
    g          NaN
    dtype: float64
    
