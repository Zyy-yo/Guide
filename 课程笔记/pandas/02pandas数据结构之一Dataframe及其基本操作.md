```python
'''
Pandas数据结构Dataframe：基本概念及创建

"二维数组"Dataframe：是一个表格型的数据结构，包含一组有序的列，其列的值类型可以是数值、字符串、布尔值等。

Dataframe中的数据以一个或多个二维块存放，不是列表、字典或一维数组结构。

'''
```




    '\nPandas数据结构Dataframe：基本概念及创建\n\n"二维数组"Dataframe：是一个表格型的数据结构，包含一组有序的列，其列的值类型可以是数值、字符串、布尔值等。\n\nDataframe中的数据以一个或多个二维块存放，不是列表、字典或一维数组结构。\n\n'




```python
'''
Dataframe 数据结构
   Dataframe是一个表格型的数据结构，可以理解为“带有标签的二维数组”。
   Dataframe带有index（行标签）和columns（列标签）
'''
import pandas as pd

data = {'name':['Jack','Marry','Tom'],
        'age':[18,19,20],
        'gender':['m','m','w']}
df = pd.DataFrame(data)
print(df)

print(type(df))       # DataFrame数据类型
print('-'*50)

print(df.index, '该数据类型为：',type(df.index))           # .index  查看行标签
print(df.columns, '该数据类型为：',type(df.columns))         # .columns  查看列标签
print(df.values, '该数据类型为：',type(df.values))          # .values     查看值，数据类型为二维数组
```

        name  age gender
    0   Jack   18      m
    1  Marry   19      m
    2    Tom   20      w
    <class 'pandas.core.frame.DataFrame'>
    --------------------------------------------------
    RangeIndex(start=0, stop=3, step=1) 该数据类型为： <class 'pandas.core.indexes.range.RangeIndex'>
    Index(['name', 'age', 'gender'], dtype='object') 该数据类型为： <class 'pandas.core.indexes.base.Index'>
    [['Jack' 18 'm']
     ['Marry' 19 'm']
     ['Tom' 20 'w']] 该数据类型为： <class 'numpy.ndarray'>
    


```python
# DataFrame 创建方法
# 1，由数组/list组成的字典(此法创建时，数组或列表的长度必须一致)
import numpy as np

data1 = {'a':[1,2,3],
         'b':[3,4,5],
         'c':[5,6,7]}              # 字典中的values长度必须保持一致

data2 = {'one':np.random.rand(3),
         'two':np.random.rand(3)}

df1 = pd.DataFrame(data1)         # columns为字典的key,index默认为数字标签
df2 = pd.DataFrame(data2)

print(df1)
print('-'*30)
print(df2)

print('-'*30)
df1 = pd.DataFrame(data1, columns=list('bcAa'))   
                                    # columns参数：可以重新指定列的顺序，格式为list，如果现有数据中没有该列（比如'A'），则产生NaN值
                                                # 可以少于原数据的列
print(df1)
print('-'*30)

df2 = pd.DataFrame(data2, index=['f1','f2','f3']) 
                                    # index参数：更改行标签，格式为list。此处长度必须一致。不能多也不能少。
print(df2)
```

       a  b  c
    0  1  3  5
    1  2  4  6
    2  3  5  7
    ------------------------------
            one       two
    0  0.589499  0.821506
    1  0.747983  0.750552
    2  0.829597  0.891300
    ------------------------------
       b  c    A  a
    0  3  5  NaN  1
    1  4  6  NaN  2
    2  5  7  NaN  3
    ------------------------------
             one       two
    f1  0.589499  0.821506
    f2  0.747983  0.750552
    f3  0.829597  0.891300
    


```python
# DataFrame 创建方法
# 2，由Series组成的字典 （此法创建时，Series的长度可以不一致，生成的DataFrame会出现NaN值）

data1 = {'one':pd.Series(np.random.rand(2)),
         'two':pd.Series(np.random.rand(3))}       # 没有设置index的Series
df1 = pd.DataFrame(data1)
print(data1)
print(df1)
print('-'*50)

data2 = {'one':pd.Series(np.random.rand(2), index=['a','b']),
         'two':pd.Series(np.random.rand(3), index=['a','b','c'])}     # 设置了index的Series

df2 = pd.DataFrame(data2)
print(data2)
print(df2)
          # columns为字典的key,index为Series的标签，若Series没有设置标签，则默认为数字标签
print('-'*50)
df3 = pd.DataFrame(data2,index=['a','b','e'])
print(df3)
```

    {'one': 0    0.913270
    1    0.546365
    dtype: float64, 'two': 0    0.438187
    1    0.178768
    2    0.400377
    dtype: float64}
            one       two
    0  0.913270  0.438187
    1  0.546365  0.178768
    2       NaN  0.400377
    --------------------------------------------------
    {'one': a    0.142170
    b    0.642138
    dtype: float64, 'two': a    0.178812
    b    0.056411
    c    0.974051
    dtype: float64}
            one       two
    a  0.142170  0.178812
    b  0.642138  0.056411
    c       NaN  0.974051
    --------------------------------------------------
            one       two
    a  0.142170  0.178812
    b  0.642138  0.056411
    e       NaN       NaN
    


```python
# DataFrame 创建方法
# 3. 通过二维数组直接创建, index和columns的长度必须和数组形状一致，若不指定则返回默认的数字标签
ar = np.random.rand(9).reshape(3,3)
print(ar)
print('-'*50)

df1 = pd.DataFrame(ar)
print(df1)
print('-'*50)

df2 = pd.DataFrame(ar, index=list('abc'), columns=['one','two','three'])        
print(df2)


```

    [[0.63664588 0.68784835 0.60292496]
     [0.28775214 0.48326967 0.24426837]
     [0.78495157 0.00965889 0.20804647]]
    --------------------------------------------------
              0         1         2
    0  0.636646  0.687848  0.602925
    1  0.287752  0.483270  0.244268
    2  0.784952  0.009659  0.208046
    --------------------------------------------------
            one       two     three
    a  0.636646  0.687848  0.602925
    b  0.287752  0.483270  0.244268
    c  0.784952  0.009659  0.208046
    


```python
# DataFrame 创建方法
# 4. 由字典组成的列表   （与 列表组成的字典的相关规则类似）

data = [{'one':1,'two':2},{'one':5, 'two':10, 'three':20}]
print(data)
df1 = pd.DataFrame(data)
print(df1)
print('-'*50)

df2 = pd.DataFrame(data, index=['a','b'])
print(df2)
print('-'*50)

df3 = pd.DataFrame(data, columns = ['one','two'])
print(df3)
```

    [{'one': 1, 'two': 2}, {'one': 5, 'two': 10, 'three': 20}]
       one  three  two
    0    1    NaN    2
    1    5   20.0   10
    --------------------------------------------------
       one  three  two
    a    1    NaN    2
    b    5   20.0   10
    --------------------------------------------------
       one  two
    0    1    2
    1    5   10
    


```python
# DataFrame 创建方法
# 4. 由字典组成的字典   columns为字典的key，index为子字典的key

data = {'Jack':{'math':30,'english':50,'art':80},
        'Marry':{'math':50,'english':90,'art':19},
        'Tom':{'math':49,'english':68}}
df1 = pd.DataFrame(data)
print(df1)
print('-'*30)

df2 = pd.DataFrame(data, columns=['Jack','Tom','Bob']) # columns参数可以增加或减少列，若出现新的列，值为NaN
print(df2)
print('-'*30)

df3 = pd.DataFrame(data, index=['a','b','c']) 
    # index参数此处用法和Series组成的字典创建DataFrame类似，不能改变原有的标签,而是和columsn用法类似了。若指向新的index，值为NaN
print(df3)
```

             Jack  Marry   Tom
    art        80     19   NaN
    english    50     90  68.0
    math       30     50  49.0
    ------------------------------
             Jack   Tom  Bob
    art        80   NaN  NaN
    english    50  68.0  NaN
    math       30  49.0  NaN
    ------------------------------
       Jack  Marry  Tom
    a   NaN    NaN  NaN
    b   NaN    NaN  NaN
    c   NaN    NaN  NaN
    


```python
# 作业
# 用四种不同的方法，创建以下Dataframe（保证columns和index一致，值不做要求）
# index=['a','b','c','d','e'], columns=['four','one','three','two']

# 方法1：Series组成的字典

df1 = pd.DataFrame({'one':pd.Series(np.random.randint(1,10,5), index=['a','b','c','d','e']),
                    'two':pd.Series(np.random.randint(1,10,5), index=['a','b','c','d','e']),
                    'three':pd.Series(np.random.randint(1,10,5), index=['a','b','c','d','e']),
                    'four':pd.Series(np.random.randint(1,10,5), index=['a','b','c','d','e'])},
                    columns=['four','one','three','two'])
print(df1)

# 方法2：数组组成的字典

data = {'one':np.random.randint(1,10,5),
        'two':np.random.randint(1,10,5),
        'three':np.random.randint(1,10,5),
        'four':np.random.randint(1,10,5)}
df2 = pd.DataFrame(data, index=list('abcde'), columns=['four','one','three','two'])
print(df2)

# 方法3：从列表创建 (上面没有说，列表中的元素个数要和行数相等，子列表中的元素个数要和列数相等,类似数组的创建方式)

data = [[9,2,1,3],
        [3,19,3,8],
        [8,29,7,36],
        [9,8,1,3],
        [3,19,3,2]]
df3 = pd.DataFrame(data, index=list('abcde'), columns=['four','one','three','two'])
print(df3)

# 方法4：从二维数组创建
data = np.random.randint(1,10,(5,4))
df4 = pd.DataFrame(data, index=list('abcde'), columns=['four','one','three','two'])
print(df4)
```

       four  one  three  two
    a     4    7      6    3
    b     4    8      9    3
    c     2    3      5    3
    d     4    8      9    3
    e     7    6      5    7
       four  one  three  two
    a     3    7      9    4
    b     3    6      7    2
    c     2    6      8    8
    d     8    3      8    9
    e     4    3      1    1
       four  one  three  two
    a     9    2      1    3
    b     3   19      3    8
    c     8   29      7   36
    d     9    8      1    3
    e     3   19      3    2
       four  one  three  two
    a     4    6      2    3
    b     6    4      3    6
    c     8    6      5    4
    d     8    4      3    2
    e     2    3      2    2
    


```python
'''
Pandas数据结构Dataframe：索引

Dataframe既有行索引也有列索引，可以被看做由Series组成的字典（共用一个索引）

选择列 / 选择行 / 切片 / 布尔判断

'''
```


```python
# 选择列与行          df[col] 选择列

df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                  index=['one','two','three'],
                  columns=list('abcd'))
print(df)

data1 = df['a']                # 按照列名选择一列，输出Series
data2= df[['a','c']]          # 选择多列
print(data1, type(data1))
print(data2, type(data2))
print('-'*50)

data3 = df[:1]        # 数字时，默认选择行，只能进行切片，不能用此法单独索引 
print(data3, type(data3))      # 输出结果为DataFrame,即使只选择了一行

'''
df[col] 中写列名，一般用来选择列，不能索引index标签名来选择行
'''

```

                   a          b          c          d
    one    82.179350  62.229694  48.436311  18.880669
    two    96.153901  56.324793  10.585613  89.307032
    three   3.641664  86.191893  30.891112  22.003778
    one      82.179350
    two      96.153901
    three     3.641664
    Name: a, dtype: float64 <class 'pandas.core.series.Series'>
                   a          c
    one    82.179350  48.436311
    two    96.153901  10.585613
    three   3.641664  30.891112 <class 'pandas.core.frame.DataFrame'>
    --------------------------------------------------
                a          b          c          d
    one  82.17935  62.229694  48.436311  18.880669 <class 'pandas.core.frame.DataFrame'>
    




    '\ndf[col] 中写列名，一般用来选择列，不能索引index标签名来选择行\n'




```python
# df.loc[]    按index选择行

df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                  index=['one','two','three'],
                  columns=list('abcd'))
data3 = df.loc['one']                # 单行输出Series
data4 = df.loc[['one','two']]       # 多个标签索引，输出DataFrame,若标签不存在，返回NaN.
print(data3, type(data3))
print(data4, type(data4))

print(df.loc['one':'three'])         # 切片索引，末端包含

'''
df.loc[label] 主要针对index选择行，默认的index和重新指定的index都支持

'''
```

    a    82.494935
    b    27.272400
    c    92.841394
    d    26.430158
    Name: one, dtype: float64 <class 'pandas.core.series.Series'>
                 a          b          c          d
    one  82.494935  27.272400  92.841394  26.430158
    two  90.806531  10.371736  67.410975  56.506523 <class 'pandas.core.frame.DataFrame'>
                   a          b          c          d
    one    82.494935  27.272400  92.841394  26.430158
    two    90.806531  10.371736  67.410975  56.506523
    three   8.135428  11.868672   8.448514  80.969009
    


```python
# df.iloc[]   按照整数位置（从轴的0到length-1）选择行
# 类似list的索引，其顺序就是dataframe的整数位置，从0开始计

ar = np.random.rand(16).reshape(4,4)*100
df = pd.DataFrame(ar, index=['one','two','three','four'],
                  columns=['a','b','c','d'])
print(df)
print('-'*50)

print(df.iloc[0])     #  单位置索引，输出Series
print(df.iloc[-1])
print('-'*50)

print(df.iloc[1:3])   # 切片索引，末端不包含
print(df.iloc[::2])


```

                   a          b          c          d
    one    92.365000  38.095210   5.230583  94.085018
    two    11.022131  40.640090  85.263325  51.576126
    three  57.116972  27.575301  84.740687  62.951662
    four   41.238809  25.594731  85.830885  90.738890
    --------------------------------------------------
    a    92.365000
    b    38.095210
    c     5.230583
    d    94.085018
    Name: one, dtype: float64
    a    41.238809
    b    25.594731
    c    85.830885
    d    90.738890
    Name: four, dtype: float64
    --------------------------------------------------
                   a          b          c          d
    two    11.022131  40.640090  85.263325  51.576126
    three  57.116972  27.575301  84.740687  62.951662
                   a          b          c          d
    one    92.365000  38.095210   5.230583  94.085018
    three  57.116972  27.575301  84.740687  62.951662
    


```python
# 布尔型索引  和Series的原理相同
ar = np.random.rand(16).reshape(4,4)*100
df = pd.DataFrame(ar, index=['one','two','three','four'],
                  columns=['a','b','c','d'])
print(df)
print('-'*50)

b1 = df > 50
print(b1, type(b1))
print('-'*50)

print(df[b1])     # 不做索引会对每个值进行判断，索引结果保留所有数据，True返回原数据，False返回NaN
print('-'*50)


b2 = df['a'] < 50        # 单列判断
print(b2, type(b2))        # 索引结果保留单列判断为True的数据，及其所在行所对应的其他列
print('-'*50)

print(df[b2])
print('-'*50)

b3 = df[['a','c']] > 50      # 多列判断
print(b3, type(b3))
print(df[b3])              # 索引结果保留所有数据，True返回原数据，False返回NaN
print('-'*50)

b4 = df.loc[['one','three']] < 50     # 多行判断
print(b4, type(b4))
print(df[b4])         # 索引结果保留所有数据，True返回原数据，False返回NaN
```

                   a          b          c          d
    one    62.231743  34.142421  74.474051  63.240026
    two    36.355859  29.235768  11.793123  48.796643
    three   6.809870  32.827935  96.691744  15.761536
    four   22.813033  27.163390  14.991566  77.237789
    --------------------------------------------------
               a      b      c      d
    one     True  False   True   True
    two    False  False  False  False
    three  False  False   True  False
    four   False  False  False   True <class 'pandas.core.frame.DataFrame'>
    --------------------------------------------------
                   a   b          c          d
    one    62.231743 NaN  74.474051  63.240026
    two          NaN NaN        NaN        NaN
    three        NaN NaN  96.691744        NaN
    four         NaN NaN        NaN  77.237789
    --------------------------------------------------
    one      False
    two       True
    three     True
    four      True
    Name: a, dtype: bool <class 'pandas.core.series.Series'>
    --------------------------------------------------
                   a          b          c          d
    two    36.355859  29.235768  11.793123  48.796643
    three   6.809870  32.827935  96.691744  15.761536
    four   22.813033  27.163390  14.991566  77.237789
    --------------------------------------------------
               a      c
    one     True   True
    two    False  False
    three  False   True
    four   False  False <class 'pandas.core.frame.DataFrame'>
                   a   b          c   d
    one    62.231743 NaN  74.474051 NaN
    two          NaN NaN        NaN NaN
    three        NaN NaN  96.691744 NaN
    four         NaN NaN        NaN NaN
    --------------------------------------------------
               a     b      c      d
    one    False  True  False  False
    three   True  True  False   True <class 'pandas.core.frame.DataFrame'>
                 a          b   c          d
    one        NaN  34.142421 NaN        NaN
    two        NaN        NaN NaN        NaN
    three  6.80987  32.827935 NaN  15.761536
    four       NaN        NaN NaN        NaN
    


```python
# 多重索引   同时索引行和列
# 先选择列再选择行  —— 相当于先筛选字段，再选择数据量
ar = np.random.rand(16).reshape(4,4)*100
df = pd.DataFrame(ar, index=['one','two','three','four'],
                  columns=['a','b','c','d'])

print(df)
print('-'*50)

print(df['a'].loc[['one','three']])    # 选择a列的one，three行
print('-'*50)


print(df[['a','b','c']].iloc[1:-1])       # 选择a, b，c列的two，three行
print('-'*50)

print(df[df['a'] < 50].iloc[:2])     # 选择满足判断索引的前两行数据，如果只有一行也可以返回，没有的话，返回空dataframe


```

                   a          b          c          d
    one    63.410650  65.299583  11.667762  64.900418
    two    80.297522  45.755656  19.058355  43.136931
    three  94.816552  54.847275  70.778571  65.104440
    four   53.826586  22.938729  71.094783  50.865473
    --------------------------------------------------
    one      63.410650
    three    94.816552
    Name: a, dtype: float64
    --------------------------------------------------
                   a          b          c
    two    80.297522  45.755656  19.058355
    three  94.816552  54.847275  70.778571
    --------------------------------------------------
    Empty DataFrame
    Columns: [a, b, c, d]
    Index: []
    


```python
# 作业
# 如图创建Dataframe(4*4，值为0-100的随机数)，通过索引得到以下值
# ① 索引得到b，c列的所有值
# ② 索引得到第三第四行的数据
# ③ 按顺序索引得到two，one行的值
# ④ 索引得到大于50的值

ar = np.random.rand(16).reshape(4,4)*100
df = pd.DataFrame(ar, index=['one','two','three','four'],
                  columns=list('abcd'))
print(df)
print('-'*50)

print(df[['b','c']])          # 索引得到b，c列的所有值
print('-'*50)

print(df.iloc[2:4])            # 索引得到第三第四行的数据
print('-'*50)

print(df.loc[['two','one']])      # 按顺序索引得到two，one行的值(按顺序？？)
print('-'*50)

print(df[df>50])                 # 索引得到大于50的值
```

                   a          b          c          d
    one    46.575061  74.599435  48.221285  81.107635
    two    93.162112  19.213331  46.002770  10.322195
    three  94.996317  46.828615  86.161178   0.355242
    four   41.289152   5.778042  74.673209  63.840821
    --------------------------------------------------
                   b          c
    one    74.599435  48.221285
    two    19.213331  46.002770
    three  46.828615  86.161178
    four    5.778042  74.673209
    --------------------------------------------------
                   a          b          c          d
    three  94.996317  46.828615  86.161178   0.355242
    four   41.289152   5.778042  74.673209  63.840821
    --------------------------------------------------
                 a          b          c          d
    two  93.162112  19.213331  46.002770  10.322195
    one  46.575061  74.599435  48.221285  81.107635
    --------------------------------------------------
                   a          b          c          d
    one          NaN  74.599435        NaN  81.107635
    two    93.162112        NaN        NaN        NaN
    three  94.996317        NaN  86.161178        NaN
    four         NaN        NaN  74.673209  63.840821
    


```python
'''
Pandas数据结构Dataframe：基本技巧

数据查看、转置 / 添加、修改、删除值 / 对齐 / 排序
'''
```


```python
# 数据查看/转置
import numpy as np
import pandas as pd
ar = np.random.rand(16).reshape(8,2)*100
df = pd.DataFrame(ar, columns=['a','b'])
print(df.head(2))
print(df.tail())

df2 = df.T          # 行与列的转换
print(df2)
```

               a          b
    0  21.260974  17.929474
    1  93.063212  19.445128
               a          b
    3  14.712306  37.139824
    4  96.726453  53.558474
    5  59.611305  39.465506
    6  85.984804   6.935089
    7  16.746756  68.169544
               0          1          2          3          4          5  \
    a  21.260974  93.063212  75.668339  14.712306  96.726453  59.611305   
    b  17.929474  19.445128  95.261651  37.139824  53.558474  39.465506   
    
               6          7  
    a  85.984804  16.746756  
    b   6.935089  68.169544  
    


```python
# 添加与修改
ar = np.random.rand(16).reshape(4,4)*100
df = pd.DataFrame(ar, columns=['a','b','c','d'])
print(df)

df['e'] = 10      # 添加列
df.loc[4] = 20        # 添加行
print(df)

df['e'] = 100            # 修改单列
df[['a','c']] = 50          # 修改多列
print(df)


df.loc[3] = 0            # 修改单行
df.loc[[2,4]] = 1111          # 修改多行
print(df)
```

               a          b          c          d
    0   9.284434  26.467916  21.132383  50.312229
    1  99.654096  24.586862   3.208791  15.938164
    2  28.313597  45.427967  70.016885  81.912265
    3  68.110588  63.223829  13.289634  85.752741
               a          b          c          d   e
    0   9.284434  26.467916  21.132383  50.312229  10
    1  99.654096  24.586862   3.208791  15.938164  10
    2  28.313597  45.427967  70.016885  81.912265  10
    3  68.110588  63.223829  13.289634  85.752741  10
    4  20.000000  20.000000  20.000000  20.000000  20
        a          b   c          d    e
    0  50  26.467916  50  50.312229  100
    1  50  24.586862  50  15.938164  100
    2  50  45.427967  50  81.912265  100
    3  50  63.223829  50  85.752741  100
    4  50  20.000000  50  20.000000  100
          a            b     c            d     e
    0    50    26.467916    50    50.312229   100
    1    50    24.586862    50    15.938164   100
    2  1111  1111.000000  1111  1111.000000  1111
    3     0     0.000000     0     0.000000     0
    4  1111  1111.000000  1111  1111.000000  1111
    


```python
# 删除  del  / drop()

ar = np.random.rand(16).reshape(4,4)*100
df = pd.DataFrame(ar, columns=['a','b','c','d'])
print(df)

del df['a']       # 删除列, 直接改变原数据
print(df)

df1 = df.drop(0)    # 删除行，inplace=False，不改变原数据，返回新的dataframe
print(df1)
df1 = df1.drop([1,3])   # 删除多行
print(df1)
print('--'*20)

df2 = df.drop(['b'],axis=1)        # axis=1, 删除列
print(df2)
df2 = df.drop(['b','d'], axis=1)     # 删除多列
print(df2)
print('--'*20)


df3 = df.drop(columns=['b'])          # axis=0, 删除列
print(df3)
df3 = df.drop(columns=['b','c'])        # 删除多列
print(df3)


```

               a          b          c          d
    0  44.557202  38.467413  17.468630  24.897095
    1  25.790174  29.749454  69.463346  64.430462
    2  82.125952  95.167029  19.353708  94.674357
    3  63.939938  97.136571  36.712765  73.580059
               b          c          d
    0  38.467413  17.468630  24.897095
    1  29.749454  69.463346  64.430462
    2  95.167029  19.353708  94.674357
    3  97.136571  36.712765  73.580059
               b          c          d
    1  29.749454  69.463346  64.430462
    2  95.167029  19.353708  94.674357
    3  97.136571  36.712765  73.580059
               b          c          d
    2  95.167029  19.353708  94.674357
    ----------------------------------------
               c          d
    0  17.468630  24.897095
    1  69.463346  64.430462
    2  19.353708  94.674357
    3  36.712765  73.580059
               c
    0  17.468630
    1  69.463346
    2  19.353708
    3  36.712765
    ----------------------------------------
               c          d
    0  17.468630  24.897095
    1  69.463346  64.430462
    2  19.353708  94.674357
    3  36.712765  73.580059
               d
    0  24.897095
    1  64.430462
    2  94.674357
    3  73.580059
    


```python
# 对齐
df1 = pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
df2 = pd.DataFrame(np.random.randn(7,3), columns=['a','b','c'])
print(df1)
print(df2)
print('--'*20)

print(df1 + df2)

    # DataFrame对象之间的数据自动按照列和索引（行标签）对齐
```

              a         b         c         d
    0  0.481294  0.261715  0.117177  1.416551
    1 -1.862800  1.183450 -0.674149  0.903817
    2 -0.109332  0.621422 -1.763519  0.279812
    3 -0.230191 -1.306377  0.124010 -1.319277
    4  0.604104  2.647721  1.358882  0.365744
    5 -1.352434 -1.100404 -0.010238  0.633290
    6  1.780080  0.594678 -2.239993  1.253864
    7 -1.103951  1.894543  1.636045  0.709878
    8  0.468176 -0.945796 -0.522232  0.908860
    9 -0.855043  1.162385 -2.059452 -1.259957
              a         b         c
    0 -1.108042  0.691599 -1.678493
    1 -2.082820 -0.836385 -0.530340
    2 -1.315705  0.881954 -0.054636
    3  0.734078  1.276265  0.105188
    4 -0.514659 -0.634916  0.068234
    5 -0.712549 -1.037422  0.554575
    6 -1.188228  0.466822 -0.833621
    ----------------------------------------
              a         b         c   d
    0 -0.626747  0.953314 -1.561316 NaN
    1 -3.945620  0.347065 -1.204489 NaN
    2 -1.425037  1.503375 -1.818155 NaN
    3  0.503888 -0.030112  0.229199 NaN
    4  0.089445  2.012805  1.427116 NaN
    5 -2.064983 -2.137826  0.544337 NaN
    6  0.591852  1.061500 -3.073615 NaN
    7       NaN       NaN       NaN NaN
    8       NaN       NaN       NaN NaN
    9       NaN       NaN       NaN NaN
    


```python
# 排序1 —— 按值排序   .sort_values     (同样适用于Series)
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100, columns=list('abcd'))
print(df1)
print('--'*20)

df1_1 = df1.sort_values(['a'])   # 默认ascending=True，升序，默认inplace=False,不就地操作
df1_2 = df1.sort_values(['a'], ascending=False)   # ascending=False  降序

print(df1_1, df1_2, sep='\n\n')
print('--'*30)

data = {'a':[1,2,3,1,2,2,2,1],
        'b':list(range(8)),
        'c':list(range(8,0,-1))}
df2 = pd.DataFrame(data)
print(df2)

df2_1 = df2.sort_values(['a','c'])       # 多列排序
print(df2_1)

```

               a          b          c          d
    0  75.354345  52.347291  15.020651  77.798644
    1  42.683183  18.031919  28.197187  28.921660
    2  27.165237  32.848112  23.724364  93.022989
    3  23.540589  73.558738  59.346053  25.640154
    ----------------------------------------
               a          b          c          d
    3  23.540589  73.558738  59.346053  25.640154
    2  27.165237  32.848112  23.724364  93.022989
    1  42.683183  18.031919  28.197187  28.921660
    0  75.354345  52.347291  15.020651  77.798644
    
               a          b          c          d
    0  75.354345  52.347291  15.020651  77.798644
    1  42.683183  18.031919  28.197187  28.921660
    2  27.165237  32.848112  23.724364  93.022989
    3  23.540589  73.558738  59.346053  25.640154
    ------------------------------------------------------------
       a  b  c
    0  1  0  8
    1  2  1  7
    2  3  2  6
    3  1  3  5
    4  2  4  4
    5  2  5  3
    6  2  6  2
    7  1  7  1
       a  b  c
    7  1  7  1
    3  1  3  5
    0  1  0  8
    6  2  6  2
    5  2  5  3
    4  2  4  4
    1  2  1  7
    2  3  2  6
    


```python
# 排序2 —— 索引排序   .sort_index

df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  index=[5,4,3,2],
                  columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  index=list('hsxg'),
                  columns=list('abcd'))

print(df1)
print(df1.sort_index())        # 默认ascending=True, inplace=False
print('--'*30)

print(df2)
print(df2.sort_index(ascending=False))       # 降序
```

               a          b          c          d
    5  74.417559  12.756046  25.069596  85.327548
    4  73.121751  50.546952  65.363520   0.415470
    3  98.239652  47.088418  65.830938  88.178154
    2  93.835377   3.979123  89.020123   0.147966
               a          b          c          d
    2  93.835377   3.979123  89.020123   0.147966
    3  98.239652  47.088418  65.830938  88.178154
    4  73.121751  50.546952  65.363520   0.415470
    5  74.417559  12.756046  25.069596  85.327548
    ------------------------------------------------------------
               a          b          c          d
    h  77.319727  72.404463  81.214709  94.371731
    s  46.344738  70.097134  26.996986   5.613875
    x  30.752910  72.482810   0.733236  65.480046
    g  72.839298  50.912353  66.576689  51.239822
               a          b          c          d
    x  30.752910  72.482810   0.733236  65.480046
    s  46.344738  70.097134  26.996986   5.613875
    h  77.319727  72.404463  81.214709  94.371731
    g  72.839298  50.912353  66.576689  51.239822
    


```python
# 作业
# 1. 创建一个3*3，值在0-100区间随机值的Dataframe（如图），分别按照index和第二列值大小，降序排序
# index=['a','b','c'], columns=['v1','v2','v3']

ar = np.random.rand(9).reshape(3,3)*100
df = pd.DataFrame(ar, index=['a','b','c'], columns=['v1','v2','v3'])
print(df)

print(df.sort_index(ascending=False))       # 按照index降序排列

print(df.sort_values(['v2'], ascending=False))     # 按照第二列值大小降序排列

```

              v1         v2         v3
    a  38.278828  72.474694  73.351398
    b  83.192704  57.296368  30.750088
    c  51.183448  77.293436  29.444948
              v1         v2         v3
    c  51.183448  77.293436  29.444948
    b  83.192704  57.296368  30.750088
    a  38.278828  72.474694  73.351398
              v1         v2         v3
    c  51.183448  77.293436  29.444948
    a  38.278828  72.474694  73.351398
    b  83.192704  57.296368  30.750088
    


```python
# 2. 创建一个5*2，值在0-100区间随机值的Dataframe（如图）df1，通过修改得到df2(v1,v2行，a到d列)

ar = np.random.rand(10).reshape(5,2)*100
df1 = pd.DataFrame(ar, index=list('abcde'), columns=['v1','v2'])
print(df1)

df1.drop('e', inplace=True)
df2 = df1.T
print(df2)
```

              v1         v2
    a  29.750075  62.031835
    b  38.592896  50.319211
    c   2.361046  59.138098
    d  67.887734  27.921484
    e  58.399575  90.459279
                a          b          c          d
    v1  29.750075  38.592896   2.361046  67.887734
    v2  62.031835  50.319211  59.138098  27.921484
    
