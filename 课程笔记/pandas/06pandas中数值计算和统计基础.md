```python
# 基本参数：axis、skipna

import numpy as np
import pandas as pd

df = pd.DataFrame({'key1':[4,5,3,np.nan,2],
                 'key2':[1,2,np.nan,4,5],
                 'key3':[1,2,3,'j','k']},
                 index = ['a','b','c','d','e'])
print(df)
print(df['key1'].dtype,df['key2'].dtype,df['key3'].dtype)
print('-----')

m1 = df.mean()
print(m1,type(m1))
print('单独统计一列:',df['key2'].mean())
print('-----')
# np.nan ：空值
# .mean()计算均值
# 只统计数字列
# 可以通过索引单独统计一列

m2 = df.mean(axis=1)
print(m2)
print('-----')
# axis参数：默认为0，以列来计算，axis=1，以行来计算。此时忽略字符串，计算了每行的均值

m3 = df.mean(skipna=False)
print(m3)
print('-----')
# skipna参数：是否忽略NaN，默认True，如False，有NaN的列统计结果仍未NaN
```

       key1  key2 key3
    a   4.0   1.0    1
    b   5.0   2.0    2
    c   3.0   NaN    3
    d   NaN   4.0    j
    e   2.0   5.0    k
    float64 float64 object
    -----
    key1    3.5
    key2    3.0
    dtype: float64 <class 'pandas.core.series.Series'>
    单独统计一列: 3.0
    -----
    a    2.5
    b    3.5
    c    3.0
    d    4.0
    e    3.5
    dtype: float64
    -----
    key1   NaN
    key2   NaN
    dtype: float64
    -----
    


```python
# 主要数学计算方法，可用于Series和DataFrame（1）

df = pd.DataFrame({'key1':np.arange(10),
                  'key2':np.random.rand(10)*10})
print(df)
print('-----')

print(df.count(),'→ count统计非Na值的数量\n')
print(df.min(),'→ min统计最小值\n',df['key2'].max(),'→ max统计最大值\n')
print(df.quantile(q=0.75),'→ quantile统计分位数，参数q确定位置\n')  # 默认q=0.5
print(df.sum(),'→ sum求和\n')
print(df.mean(),'→ mean求平均值\n')
print(df.median(),'→ median求算数中位数，50%分位数\n')
print(df.std(),'\n',df.var(),'→ std,var分别求标准差，方差\n')
print(df.skew(),'→ skew样本的偏度\n')
print(df.kurt(),'→ kurt样本的峰度\n')

   # 返回Series，也可以通过列索引单独统计一列，单独统计一列返回value
'''
偏度：统计数据分布偏斜方向和程度的度量，是统计数据分布非对称程度的数字特征
     偏度定义中包括正态分布（偏度=0），右偏分布（也叫正偏分布，其偏度>0），左偏分布（也叫负偏分布，其偏度<0）   
峰度：又称峰态系数。表征概率密度分布曲线在平均值处峰值高低的特征数。直观看来，峰度反映了峰部的尖度。
    峰度包括正态分布（峰度值=0），平峰（峰度值<0），尖峰（峰度值>0）
'''
```

       key1      key2
    0     0  1.890748
    1     1  6.437596
    2     2  9.954531
    3     3  4.446885
    4     4  4.664106
    5     5  8.317198
    6     6  3.137610
    7     7  8.908120
    8     8  6.894045
    9     9  4.579031
    -----
    key1    10
    key2    10
    dtype: int64 → count统计非Na值的数量
    
    key1    0.000000
    key2    1.890748
    dtype: float64 → min统计最小值
     9.954531285634678 → max统计最大值
    
    key1    6.750000
    key2    7.961409
    Name: 0.75, dtype: float64 → quantile统计分位数，参数q确定位置
    
    key1    45.000000
    key2    59.229871
    dtype: float64 → sum求和
    
    key1    4.500000
    key2    5.922987
    dtype: float64 → mean求平均值
    
    key1    4.500000
    key2    5.550851
    dtype: float64 → median求算数中位数，50%分位数
    
    key1    3.027650
    key2    2.618132
    dtype: float64 
     key1    9.166667
    key2    6.854615
    dtype: float64 → std,var分别求标准差，方差
    
    key1    0.000000
    key2    0.093599
    dtype: float64 → skew样本的偏度
    
    key1   -1.200000
    key2   -1.029821
    dtype: float64 → kurt样本的峰度
    
    




    '\n偏度：统计数据分布偏斜方向和程度的度量，是统计数据分布非对称程度的数字特征\n     偏度定义中包括正态分布（偏度=0），右偏分布（也叫正偏分布，其偏度>0），左偏分布（也叫负偏分布，其偏度<0）   \n峰度：又称峰态系数。表征概率密度分布曲线在平均值处峰值高低的特征数。直观看来，峰度反映了峰部的尖度。\n    峰度包括正态分布（峰度值=0），平峰（峰度值<0），尖峰（峰度值>0）\n'




```python
# 主要数学计算方法，可用于Series和DataFrame（2）

df['key1_s'] = df['key1'].cumsum()      # 这里还涉及到的一个知识点：添加数据
df['key2_s'] = df['key2'].cumsum()
print(df,'→ cumsum样本的累计和\n')

df['key1_p'] = df['key1'].cumprod()
df['key2_p'] = df['key2'].cumprod()
print(df,'→ cumprod样本的累计积\n')

print(df.cummax(),'\n',df.cummin(),'→ cummax,cummin分别求累计最大值，累计最小值\n')
# 会填充key1，和key2的值
# 累计最大值，一列数据中当遇到的值是最大值是，从最大值数据起，后面所有的数据都被最大值填充。累计最小值同理。

```

       key1      key2  key1_s     key2_s
    0     0  1.890748       0   1.890748
    1     1  6.437596       1   8.328345
    2     2  9.954531       3  18.282876
    3     3  4.446885       6  22.729761
    4     4  4.664106      10  27.393868
    5     5  8.317198      15  35.711065
    6     6  3.137610      21  38.848675
    7     7  8.908120      28  47.756795
    8     8  6.894045      36  54.650839
    9     9  4.579031      45  59.229871 → cumsum样本的累计和
    
       key1      key2  key1_s     key2_s  key1_p        key2_p
    0     0  1.890748       0   1.890748       0  1.890748e+00
    1     1  6.437596       1   8.328345       0  1.217187e+01
    2     2  9.954531       3  18.282876       0  1.211653e+02
    3     3  4.446885       6  22.729761       0  5.388082e+02
    4     4  4.664106      10  27.393868       0  2.513059e+03
    5     5  8.317198      15  35.711065       0  2.090161e+04
    6     6  3.137610      21  38.848675       0  6.558109e+04
    7     7  8.908120      28  47.756795       0  5.842042e+05
    8     8  6.894045      36  54.650839       0  4.027530e+06
    9     9  4.579031      45  59.229871       0  1.844218e+07 → cumprod样本的累计积
    
       key1      key2  key1_s     key2_s  key1_p        key2_p
    0   0.0  1.890748     0.0   1.890748     0.0  1.890748e+00
    1   1.0  6.437596     1.0   8.328345     0.0  1.217187e+01
    2   2.0  9.954531     3.0  18.282876     0.0  1.211653e+02
    3   3.0  9.954531     6.0  22.729761     0.0  5.388082e+02
    4   4.0  9.954531    10.0  27.393868     0.0  2.513059e+03
    5   5.0  9.954531    15.0  35.711065     0.0  2.090161e+04
    6   6.0  9.954531    21.0  38.848675     0.0  6.558109e+04
    7   7.0  9.954531    28.0  47.756795     0.0  5.842042e+05
    8   8.0  9.954531    36.0  54.650839     0.0  4.027530e+06
    9   9.0  9.954531    45.0  59.229871     0.0  1.844218e+07 
        key1      key2  key1_s    key2_s  key1_p    key2_p
    0   0.0  1.890748     0.0  1.890748     0.0  1.890748
    1   0.0  1.890748     0.0  1.890748     0.0  1.890748
    2   0.0  1.890748     0.0  1.890748     0.0  1.890748
    3   0.0  1.890748     0.0  1.890748     0.0  1.890748
    4   0.0  1.890748     0.0  1.890748     0.0  1.890748
    5   0.0  1.890748     0.0  1.890748     0.0  1.890748
    6   0.0  1.890748     0.0  1.890748     0.0  1.890748
    7   0.0  1.890748     0.0  1.890748     0.0  1.890748
    8   0.0  1.890748     0.0  1.890748     0.0  1.890748
    9   0.0  1.890748     0.0  1.890748     0.0  1.890748 → cummax,cummin分别求累计最大值，累计最小值
    
    


```python
# 唯一值：.unique()

# 前面有看到检查值是否唯一的属性：series.is_unique()，注意 dataframe无此方法。
# .unique()方法可以提取出唯一值，返回数组。相当于直接将数据做了去重的处理。同样，dataframe无此方法。

s = pd.Series(list('asdvasdcfgg'))
sq = s.unique()
print(s)
print(sq,type(sq))
print(pd.Series(sq))
# 得到一个唯一值数组
# 通过pd.Series重新变成新的Series

sq.sort()
print(sq)
# 重新排序
```

    0     a
    1     s
    2     d
    3     v
    4     a
    5     s
    6     d
    7     c
    8     f
    9     g
    10    g
    dtype: object
    ['a' 's' 'd' 'v' 'c' 'f' 'g'] <class 'numpy.ndarray'>
    0    a
    1    s
    2    d
    3    v
    4    c
    5    f
    6    g
    dtype: object
    ['a' 'c' 'd' 'f' 'g' 's' 'v']
    


```python
# 值计数：.value_counts()   series方法

sc = s.value_counts(sort = False)  # 也可以这样写：pd.value_counts(sc, sort = False)
print(sc)
# 得到一个新的Series，计算出不同值出现的频率
# sort参数：排序，默认为True
```

    c    1
    v    1
    d    2
    f    1
    g    2
    a    2
    s    2
    dtype: int64
    


```python
# 成员资格：.isin()

s = pd.Series(np.arange(10,15))
df = pd.DataFrame({'key1':list('asdcbvasd'),
                  'key2':np.arange(4,13)})
print(s)
print(df)
print('-----')

print(s.isin([5,14]))
print(df.isin(['a','bc','10',8]))
# 用[]表示
# 得到一个布尔值的Series或者Dataframe


# 结合前面所学的知识，返回满足条件的值
print(s[s.isin([5,14])])
print(df[df.isin(['a','bc','10',8])])
```

    0    10
    1    11
    2    12
    3    13
    4    14
    dtype: int32
      key1  key2
    0    a     4
    1    s     5
    2    d     6
    3    c     7
    4    b     8
    5    v     9
    6    a    10
    7    s    11
    8    d    12
    -----
    0    False
    1    False
    2    False
    3    False
    4     True
    dtype: bool
        key1   key2
    0   True  False
    1  False  False
    2  False  False
    3  False  False
    4  False   True
    5  False  False
    6   True  False
    7  False  False
    8  False  False
    4    14
    dtype: int32
      key1  key2
    0    a   NaN
    1  NaN   NaN
    2  NaN   NaN
    3  NaN   NaN
    4  NaN   8.0
    5  NaN   NaN
    6    a   NaN
    7  NaN   NaN
    8  NaN   NaN
    
