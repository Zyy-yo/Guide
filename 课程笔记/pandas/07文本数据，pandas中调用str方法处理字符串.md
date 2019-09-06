```python
'''
Pandas针对字符串配备的一套方法，使其易于对数组的每个元素进行操作
 
'''
```




    '\nPandas针对字符串配备的一套方法，使其易于对数组的每个元素进行操作\n \n'




```python
import numpy as np
import pandas as pd
```


```python
 # 通过str访问，且自动排除丢失/ NA值

s = pd.Series(['A','b','C','bbhello','123',np.nan,'hj'])
df = pd.DataFrame({'key1':list('abcdef'),
                  'key2':['hee','fv','w','hija','123',np.nan]})
print(s)
print(df)
print('-----')

print(s.str.count('b'))
print(df['key2'].str.upper())
print('-----')
# 直接通过.str调用字符串方法
# Series可以直接调用；DataFrame只能按列使用

# 自动过滤NaN值

df.columns = df.columns.str.upper()
print(df)
# df.columns是一个Index对象，也可使用.str
# 同理，df.index以及Series.index也都可以使用.str

```

    0          A
    1          b
    2          C
    3    bbhello
    4        123
    5        NaN
    6         hj
    dtype: object
      key1  key2
    0    a   hee
    1    b    fv
    2    c     w
    3    d  hija
    4    e   123
    5    f   NaN
    -----
    0    0.0
    1    1.0
    2    0.0
    3    2.0
    4    0.0
    5    NaN
    6    0.0
    dtype: float64
    0     HEE
    1      FV
    2       W
    3    HIJA
    4     123
    5     NaN
    Name: key2, dtype: object
    -----
      KEY1  KEY2
    0    a   hee
    1    b    fv
    2    c     w
    3    d  hija
    4    e   123
    5    f   NaN
    


```python
# 字符串常用方法（1） - lower，upper，len，startswith，endswith

s = pd.Series(['A','b','bbhello','123',np.nan])

print(s.str.lower(),'→ lower小写\n')
print(s.str.upper(),'→ upper大写\n')
print(s.str.len(),'→ len字符长度\n')
print(s.str.startswith('b'),'→ 判断起始是否为a\n')
print(s.str.endswith('3'),'→ 判断结束是否为3\n')

# 可以通过索引只改部分值
s[2] = s[2].upper()        # s[2]的value就是字符串型，所以直接使用.upper()方法
print(s)

```

    0          a
    1          b
    2    bbhello
    3        123
    4        NaN
    dtype: object → lower小写
    
    0          A
    1          B
    2    BBHELLO
    3        123
    4        NaN
    dtype: object → upper大写
    
    0    1.0
    1    1.0
    2    7.0
    3    3.0
    4    NaN
    dtype: float64 → len字符长度
    
    0    False
    1     True
    2     True
    3    False
    4      NaN
    dtype: object → 判断起始是否为a
    
    0    False
    1    False
    2    False
    3     True
    4      NaN
    dtype: object → 判断结束是否为3
    
    0          A
    1          b
    2    BBHELLO
    3        123
    4        NaN
    dtype: object
    


```python
# 字符串常用方法（2） - strip

s = pd.Series([' jack', 'jill ', ' jesse ', 'frank'])
df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '],
                  index=range(3))
print(s)
print(df)
print('-----')

print(s.str.strip())  # 去除字符串首尾空格
print(s.str.lstrip())  # 去除字符串中的左空格
print(s.str.rstrip())  # 去除字符串中的右空格

df.columns = df.columns.str.strip()
print(df)
```

    0       jack
    1      jill 
    2     jesse 
    3      frank
    dtype: object
        Column A    Column B 
    0   -1.279026   -0.895535
    1   -1.478828   -0.145085
    2   -0.370516    0.293117
    -----
    0     jack
    1     jill
    2    jesse
    3    frank
    dtype: object
    0      jack
    1     jill 
    2    jesse 
    3     frank
    dtype: object
    0      jack
    1      jill
    2     jesse
    3     frank
    dtype: object
       Column A  Column B
    0 -1.279026 -0.895535
    1 -1.478828 -0.145085
    2 -0.370516  0.293117
    


```python
# 字符串常用方法（3） - replace

df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '],
                  index=range(3))
df.columns = df.columns.str.replace(' ','-')
print(df)
# 替换

df.columns = df.columns.str.replace('-','hehe',n=1)
print(df)
# n：替换个数
```

       -Column-A-  -Column-B-
    0    0.466806   -0.432552
    1   -0.348389    0.153617
    2    1.269010   -1.026457
       heheColumn-A-  heheColumn-B-
    0       0.466806      -0.432552
    1      -0.348389       0.153617
    2       1.269010      -1.026457
    


```python
# 字符串常用方法（4） - split、rsplit
# 这里split()有个参数expand，如果是True，则会按拆分后的每一个元素生成column

s = pd.Series(['a,b,c','1,2,3',['a,,,c'],np.nan])
print(s.str.split(','))
print('-----')
# 类似字符串的split，注意第三个值['a,,,c']是个列表，返回的直接是NaN

print(s.str.split(',')[0])
print('-----')
# 直接索引得到一个list

print(s.str.split(',').str[0])
print(s.str.split(',').str.get(1))
print('-----')
# 可以使用get或[]符号访问拆分列表中的元素，返回的是Series

print(s.str.split(',', expand=True))
print(s.str.split(',', expand=True, n = 1))
print(s.str.rsplit(',', expand=True, n = 1))
print('-----')
# 可以使用expand可以轻松扩展此操作以返回DataFrame
# n参数限制分割数
# rsplit类似于split，反向工作，即从字符串的末尾到字符串的开头

df = pd.DataFrame({'key1':['a,b,c','1,2,3',[':,., ']],
                  'key2':['a-b-c','1-2-3',[':-.- ']]})
print(df['key2'].str.split('-'))
# Dataframe使用split
```


```python
# 字符串索引

s = pd.Series(['A','b','C','bbhello','123',np.nan,'hj'])
df = pd.DataFrame({'key1':list('abcdef'),
                  'key2':['hee','fv','w','hija','123',np.nan]})

print(s.str[0])  # 取第一个字符串
print(s.str[:2])  # 取前两个字符串
print(df['key2'].str[0]) 
# str之后和字符串本身索引方式相同
```

    0      A
    1      b
    2      C
    3      b
    4      1
    5    NaN
    6      h
    dtype: object
    0      A
    1      b
    2      C
    3     bb
    4     12
    5    NaN
    6     hj
    dtype: object
    0      h
    1      f
    2      w
    3      h
    4      1
    5    NaN
    Name: key2, dtype: object
    
