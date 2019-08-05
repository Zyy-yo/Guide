import pandas as pd
import numpy as np
import re
# ———— Series ————
# Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
a = pd.Series([3, 9, 10, 6])
print(a)
'''
0     3
1     9
2    10
3     6
dtype: int64
'''
# 可以直接获取Series中的索引和值
print(a.index)                   # RangeIndex(start=0, stop=4, step=1)
print(a.values)                  # [ 3  9 10  6]

# 可以对Series指定索引
a1 = pd.Series([10, 2, 5, 8], index=['A','B','C','D'])
print(a1)
'''
A    10
B     2
C     5
D     8
dtype: int64
'''
print(a1.index)                    # Index(['A', 'B', 'C', 'D'], dtype='object')

# 可以通过索引直接赋值，来改变Series中的值
a1['B'] = 1
print(a1)
'''
A    10
B     1
C     5
D     8
dtype: int64
'''
a1['A','C'] = 32
print(a1)
'''
A    32
B     1
C    32
D     8
dtype: int64
'''
# 也可以通过切片改变Series中的值
a1[1:3] = 5
print(a1)
'''
A    32
B     5
C     5
D     8
dtype: int64
'''
# 字典转化位Series,字典中的key转化为index
dic = {'guangzhou':2305, 'shenzhen':2940, 'beijing':3193, 'shanghai':2943}
dic_s = pd.Series(dic)
print(dic_s)
'''
guangzhou    2305
shenzhen     2940
beijing      3193
shanghai     2943
dtype: int64
'''
# 修改索引名
dic_s.index = ['GZ','SZ','BJ','SH']
print(dic_s)
'''
GZ    2305
SZ    2940
BJ    3193
SH    2943
dtype: int64
'''

# Series中是否包含某字符串
'''
Series.str.contains(self, pat, case=True, flags=0, na=nan, regex=True)
   pat:模式，字符或正则表达式
   case=True:区分大小写
   regex=True:将pat看作正则表达式；False则将pat看作字符串
'''
a2 = pd.Series(['Mouse','pig','DOG','20','1.8','buterfly',None])
print(a2.str.contains('og'))             # 默认区分大小写
'''
0    False
1    False
2    False
3    False
4    False
5    False
6     None
dtype: object
'''
print(a2.str.contains('og',case=False))     # case=False, 不区分大小写
print(a2.str.contains('og',flags=re.IGNORECASE))    # 忽略大小写
'''
0    False
1    False
2     True
3    False
4    False
5    False
6     None
dtype: object
'''
print(a2.str.contains('.0'))       # regex=True,'.0'看作是正则表达式
'''
0    False
1    False
2    False
3     True
4    False
5    False
6     None
dtype: object
'''
print(a2.str.contains('.0', regex=False))        # regex=False,'.0'看作是字符串
'''
0    False
1    False
2    False
3    False
4    False
5    False
6     None
dtype: object
'''
# 提取包含某个字符串的值
b = a2.str.contains(r'\d', na=False)      # 若有空值，必须先处理
print(a2[b])                             # 提取方式
'''
3     20
4    1.8
dtype: object
'''
# Series中的多重索引
s1 = pd.Series(np.random.randn(10),
            index=[[1, 1, 1, 2, 2, 2, 3, 3, 4, 4],
                    ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'a', 'b']])
print(s1)
'''
1  a   -0.478700
   b   -0.932857
   c   -0.183406
2  a    0.589403
   b   -2.206126
   c    0.884077
3  a    0.144808
   b   -0.596608
4  a    0.570762
   b    0.131367
dtype: float64
'''
s = s1.unstack()                 # 多层次索引下的Series转化为DataFrame，一级索引是索引，二级索引转变为column
print(s)
'''
          a         b         c
1  0.677861 -0.003082 -0.587209
2  1.144549  0.211008 -0.138527
3  0.907053  0.753469       NaN
4 -0.961919  1.081254       NaN
'''
print(s.stack())                # 转回Series


# ———— DataFrame ———— 可以理解为由相同索引的Series组成的字典类型
# DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# 创建方式1，data为字典形式，key为列名，values为每列里的数据，等长的列表形式
data = {'city':['shanghai','shanghai','shanghai','beijing','beijing'],
        'year':[2016, 2017, 2018, 2017, 2018],
        'pop':[1.8, 2.3, 3.4, 2.7, 3.6]}
df = pd.DataFrame(data)
print(df)
'''
       city  year  pop
0  shanghai  2016  1.8
1  shanghai  2017  2.3
2  shanghai  2018  3.4
3   beijing  2017  2.7
4   beijing  2018  3.6
'''
# 改变索引和列的顺序
df1 = pd.DataFrame(data, index=[1, 2, 3, 4, 5], columns=['year','city','pop'])
print(df1)
'''
   year      city  pop
1  2016  shanghai  1.8
2  2017  shanghai  2.3
3  2018  shanghai  3.4
4  2017   beijing  2.7
5  2018   beijing  3.6
'''
# 创建方式2，data为等长的序列列表，每个序列中的数据对应着DataFrame中的columns
data1 = [[2016, 'shanghai', 1.8],[2017,'shanghai', 2.3], 
        [2018,'shanghai', 3.4], [2017,'beijing', 2.7], [2018,'beijing', 3.6]]
df2 = pd.DataFrame(data1, index=[1, 2, 3, 4, 5], columns=['year','city','pop'])
print(df2)
'''
   year      city  pop
1  2016  shanghai  1.8
2  2017  shanghai  2.3
3  2018  shanghai  3.4
4  2017   beijing  2.7
5  2018   beijing  3.6
'''
# 提取二维DataFrame中的一维Series数据
print(df2['year'])                    # 提取方式1
'''
1    2016
2    2017
3    2018
4    2017
5    2018
Name: year, dtype: int64
'''
print(df2.city)                         # 提取方式2
'''
1    shanghai
2    shanghai
3    shanghai
4     beijing
5     beijing
Name: city, dtype: object
'''
# DataFrame中增加新的一列，看具体需要，可以像字典一样直接赋值
df2['new'] = [23, 93, 29, 39, 20]
print(df2)
'''
   year      city  pop  new
1  2016  shanghai  1.8   23
2  2017  shanghai  2.3   93
3  2018  shanghai  3.4   29
4  2017   beijing  2.7   39
5  2018   beijing  3.6   20
'''
# 增加新的一列，如果是北京，则为True，否则为False
df2['cap'] = df2.city == 'beijing'
print(df2)
'''
   year      city  pop  new    cap
1  2016  shanghai  1.8   23  False
2  2017  shanghai  2.3   93  False
3  2018  shanghai  3.4   29  False
4  2017   beijing  2.7   39   True
5  2018   beijing  3.6   20   True
'''
# DataFrame创建方式3，嵌套字典
pop = {'beijing':{2008:3.6, 2009:4.9},
        'shanghai':{2008:3.8, 2009:5.1}}
df3 = pd.DataFrame(pop)
print(df3)
'''
      beijing  shanghai
2008      3.6       3.8
2009      4.9       5.1
'''
print(df3.T)                  # .T  行、列互换
'''
          2008  2009
beijing    3.6   4.9
shanghai   3.8   5.1
'''
# 设置索引
# DataFrame.set_index(self, keys, drop=True, append=False, inplace=False, verify_integrity=False)
t1 = {'year':[2012, 2013, 2014, 2015],
    'month':[1, 3, 5, 8],
    'sale':[391, 350, 659, 728]}
dt1 = pd.DataFrame(t1)
print(dt1)
'''
   year  month  sale
0  2012      1   391
1  2013      3   350
2  2014      5   659
3  2015      8   728
'''
dt2 = dt1.set_index('year')     # 以year作为索引
print(dt2)
'''
      month  sale
year
2012      1   391
2013      3   350
2014      5   659
2015      8   728
'''
dt3 = dt1.set_index(['year','month'])          # 以year和month为索引
print(dt3)
'''
            sale
year month
2012 1       391
2013 3       350
2014 5       659
2015 8       728
'''
dt4 = dt1.set_index([pd.Index([1, 2, 3, 4]), 'year'])     # 以index和year为索引
print(dt4)
'''
        month  sale
  year
1 2012      1   391
2 2013      3   350
3 2014      5   659
4 2015      8   728
'''
s = pd.Series(['a', 'b', 'c', 'd'])               # 以Series作为索引
dt5 = dt1.set_index(s)
print(dt5)
'''
   year  month  sale
a  2012      1   391
b  2013      3   350
c  2014      5   659
d  2015      8   728
'''

# 重设索引
# DataFrame.reset_index(self, level=None, drop=False, inplace=False, col_level=0, col_fill='')
t2 = pd.DataFrame([('bird',389),('bird',109),('mammal',25),('mammal',None)],
                index=['falcon','parrot','lion','monkey'],
                columns=['class','max_speed'])
print(t2)
'''
         class  max_speed
falcon    bird      389.0
parrot    bird      109.0
lion    mammal       25.0
monkey  mammal        NaN
'''
dt2_1 = t2.reset_index()                         # drop默认为False，重设索引后，原索引变成了column
print(dt2_1)
'''
    index   class  max_speed
0  falcon    bird      389.0
1  parrot    bird      109.0
2    lion  mammal       25.0
3  monkey  mammal        NaN
'''
dt2_2 = t2.reset_index(drop=True)                # drop=True，删除原索引
print(dt2_2)
'''
    class  max_speed
0    bird      389.0
1    bird      109.0
2  mammal       25.0
3  mammal        NaN
'''
# reset_index也可以用来修改多重索引
# 多重索引MultiIndex设置，pandas.MultiIndex.from_tuples(tuples, sortorder=None, names=None)
index = pd.MultiIndex.from_tuples([('bird','falcon'),
                                   ('bird','parrot'),
                                   ('mammal','lion'),
                                   ('mammal','monkey')],
                                   names=['class','name'])
columns = pd.MultiIndex.from_tuples([('speed','max'),('species','type')])
t3 = pd.DataFrame([(389,'fly'),(24,'fly'),(80,'run'),(None,'jump')],
                    index=index, columns=columns)
print(t3)
'''
               speed species
                 max    type
class  name
bird   falcon  389.0     fly
       parrot   24.0     fly
mammal lion     80.0     run
       monkey    NaN    jump
'''
 # 将多重索引中的一个进行reset，drop默认False，此时class成为列之后，class被放到顶层
dt3_1 = t3.reset_index(level='class')  
print(dt3_1)
'''
         class  speed species
                  max    type
name
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.0     run
monkey  mammal    NaN    jump
'''
# 可以将上面的class放到另一个层次
dt3_2 = t3.reset_index(level='class', col_level=1)
print(dt3_2)
'''
                speed species
         class    max    type
name
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.0     run
monkey  mammal    NaN    jump
'''
# 当索引class被放到另一个层级下时，可以使用col_fill来填充这个层级下的空缺,如果指定层级不存在，则创建
dt3_3 = t3.reset_index(level='class', col_level=1, col_fill='genus')
print(dt3_3)
'''
         genus  speed species
         class    max    type
name
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.0     run
monkey  mammal    NaN    jump
'''

# 删除行或列
# DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
'''
t3:
               speed species
                 max    type
class  name
bird   falcon  389.0     fly
       parrot   24.0     fly
mammal lion     80.0     run
       monkey    NaN    jump
'''
dt3_4 = t3.drop(['speed'], axis=1, level=0)         # 或   dt3_4 = t3.drop(columns='speed', level=0)
print(dt3_4)
'''
              species
                 type
class  name
bird   falcon     fly
       parrot     fly
mammal lion       run
       monkey    jump
'''
dt3_5 = t3.drop(columns='max', level=1)    # 效果同t3.drop(columns='speed', level=0)
print(dt3_5)
'''
              species
                 type
class  name
bird   falcon     fly
       parrot     fly
mammal lion       run
       monkey    jump
'''
dt3_6 = t3.drop(index='bird')
print(dt3_6)
'''
              speed species
                max    type
class  name
mammal lion    80.0     run
       monkey   NaN    jump
'''
dt3_7 = t3.drop(index=['parrot','lion'], level=1)
print(dt3_7)
'''
               speed species
                 max    type
class  name
bird   falcon  389.0     fly
mammal monkey    NaN    jump
'''

# 删除重复行
# DataFrame.drop_duplicates(self, subset=None, keep='first', inplace=False)
t4 = pd.DataFrame({'name':['yao','shun','yu','yu'],
                   'math':[79, 79, 90, 90],
                   'chinese':[80, 103, 69, 69],
                   'english':[103, 113, 110, 110]})
print(t4)
'''
   name  math  chinese  english
0   yao    79       80      103
1  shun    79      103      113
2    yu    90       69      110
3    yu    90       69      110
'''
dt4_1 = t4.drop_duplicates()      # subset=None,默认删除整行重复，keep='first',保留第一次出现的值;'last'保留最后一次出现的值;False不保留重复的项
print(dt4_1)
'''
   name  math  chinese  english
0   yao    79       80      103
1  shun    79      103      113
2    yu    90       69      110
'''
dt4_2 = t4.drop_duplicates(subset='math')    # 子集math中出现重复值，则删除该行
print(dt4_2)
'''
  name  math  chinese  english
0  yao    79       80      103
2   yu    90       69      110
'''

# 删除缺失值
# DataFrame.dropna(self, axis=0, how='any', thresh=None, subset=None, inplace=False)
t5 = pd.DataFrame({'name':['liu',None,'zhao','kun','tong'],
                'age':[24, None, None, 28, 24],
                'math':[None, None, 83, 70, 108]})
print(t5)
'''
   name   age   math
0   liu  24.0    NaN
1  None   NaN    NaN
2  zhao   NaN   83.0
3   kun  28.0   70.0
4  tong  24.0  108.0
'''
print(t5.dropna())         # 默认how='any',axis=0, 任何缺失值所在行都要删除
'''
   name   age   math
3   kun  28.0   70.0
4  tong  24.0  108.0
'''
print(t5.dropna(axis=1))   # axis=1,默认how='any',任何缺失值所在列都要删除
'''
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]
'''
print(t5.dropna(how='all'))   # how='all',若行或列所有值都缺失，则删除该行或列
'''
   name   age   math
0   liu  24.0    NaN
2  zhao   NaN   83.0
3   kun  28.0   70.0
4  tong  24.0  108.0
'''
print(t5.dropna(subset=['math']))       # 删除子集math中有缺失值的行，此处subset必须是列表形式
'''
   name   age   math
2  zhao   NaN   83.0
3   kun  28.0   70.0
4  tong  24.0  108.0
'''
print(t5.dropna(thresh=2))       # 出现2个及以上空值，则删除该行
'''
   name   age   math
0   liu  24.0    NaN
2  zhao   NaN   83.0
3   kun  28.0   70.0
4  tong  24.0  108.0
'''
