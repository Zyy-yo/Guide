```python
# 字符串str也是有序的序列，属于文本序列
# 字符串需要用到引号，单引号和双引号都可以，当字符串里也有引号时，需要用单双引号区分
# 三引号可以定义需要换行的字符串
```


```python
# 作为序列，序列的通用操作也都适用
# 成员运算符
# 基本内置全局函数
# 连接和重复
# 索引和切片
```


```python
# 字符串常用操作——替换
s = 'abcdaxf'
sr = s.replace('a','0')      # 返回一个新的字符串；默认count=-1,替换掉字符串里所有指定的字符
print(sr)

s = '01230390120'
sr = s.replace('0','-',2)     # count=2, 替换掉2个
print(sr)
```

    0bcd0xf
    -123-390120
    


```python
# 字符串常用操作——拆分
s = '213.59,103.28902'
ss = s.split(',')             # 拆分字符串，生成列表
print(ss)
```

    ['213.59', '103.28902']
    


```python
# 字符串常用操作——连接
s = ['133','0809','920']
m = '-'
sj = m.join(s)              # join()连接字符串，参数对象可以是列表和元组类型
print(sj)


s = ['318','is bigger than','300']
sj = ' '.join(s)
print(sj)

s = ('3','f')
s = '2'.join(s)
print(s)
```

    133-0809-920
    318 is bigger than 300
    32f
    


```python
# 判断是否以某个字符开头或结尾
s = '138kdls9lad'
print(s.startswith('3'))
print(s.endswith('d'))
```

    False
    True
    


```python
# 字符串常用操作——大小写
s = 'That is true!'
s = s.upper()         # 全部大写     此类方法会生成新的字符串
print(s)
print(s.lower())       # 全部小写    直接打印时，并不会改变之前的字符串s
print(s)
print('-'*20)

w = 'KLDKSdksdkm'
print(w.capitalize())   # 首字母大写
print(w.swapcase())     # 大小写互换
```

    THAT IS TRUE!
    that is true!
    THAT IS TRUE!
    --------------------
    Kldksdksdkm
    kldksDKSDKM
    


```python
# 字符串常用操作——删除首尾空格
s = '      90293     '
print(len(s))

s1 = s.strip()                    # 删除首尾空格
print(len(s1), s1, sep='    :')

s2 = s.rstrip()
print(len(s2), s2, sep='    :')   # 删除尾部空格

s3 = s.lstrip()
print(len(s3), s3, sep='    :')   # 删除首部空格

# strip()方法本质上是字符串里删除字符的操作，只不过空格是比较特殊的字符而已

print('='*20)

w = '---258.920@'
w1 = w.lstrip('-')
print(w1)

w2 = w1.rstrip('@')
print(w2)
```

    16
    5    :90293
    11    :      90293
    10    :90293     
    ====================
    258.920@
    258.920
    


```python
s = '2392ldk'
s1 = '90293'
s2 = 'kdlskd'

print(s.isnumeric())
print(s1.isnumeric())    # 判断字符串里是否全是数字，只有全是数字时才为True
print(s2.isnumeric())

print('-'*20)

print(s.isalpha())
print(s1.isalpha())
print(s2.isalpha())      # 判断字符串里是否全是字母，只有全是字母时才为True
```

    False
    True
    False
    --------------------
    False
    False
    True
    


```python
# 格式化字符—— %

'''
%i  整数
%d  整数
%f  浮点数
%s  字符串
%e/%E   科学计数法
%g  当数字复杂的时候会使用科学计数法，否则就用原来的类型
'''
a = 'she'
print('%s is good.'%a)

a = 3.6903
print('%i'%a)      # 只是取整数部分
print('%.0f'%a)     # 四舍五入的方式

m = 100
n = -0.39
print('正数 %+i'%m)    # 显示正号，在 %i 之间加上 + 字符
print('负数 %.2f'%n)   # 负号会直接显示
print('-'*20)

print('正数% i'%m)       # 显示空格：% i
print('正数% +i'%m)      # 空格和正号并存时，只显示正号
print('负数% .2f'%n)      # 这里本身是负数，当% .2f有空格时，也只显示负号，而不会出现空格

print('-'*20)
m = 239.291097385
print('%s 科学计数法结果是 %e'%(m,m))          # e和E都可以， 2.3929E+02 表示2.3929 * 10**2
print('%s 科学计数法结果是 %.4E'%(m,m))

print('-'*20)
m = 29301935894839293
n = 203.2933013
f = 232
print('%g'%m)
print('%.2g'%m)            # 这里比较有意思的是,%.2g中的2表示有效位数，而不是保留的小数位数
print('%g'%n)
print('%g'%f)

print('-'*20)
print('%.2f%%'%23.92039)          # 显示百分号，%.2f%%，后面要加两个%
```

    she is good.
    3
    4
    正数 +100
    负数 -0.39
    --------------------
    正数 100
    正数+100
    负数-0.39
    --------------------
    239.291097385 科学计数法结果是 2.392911e+02
    239.291097385 科学计数法结果是 2.3929E+02
    --------------------
    2.93019e+16
    2.9e+16
    203.293
    232
    --------------------
    23.92%
    


```python
# 格式化方法——format()
print('扶摇直上{}'.format('九万里'))
print('{0}{1}{0}{2}'.format('a','b','c'))
  # {}叫做占位符，可以为空；可以加数字，指定format()里的字符

s = 'good {}'
s1 = s.format('job')
print(s1)
print('-'*20)

# 可以用变量来指示，但是要注意下面这两种写法是有差别的
s = '学海无涯'
print('{}苦作舟'.format(s))            # 先定义变量，此时占位符要为空{}

print('{s}苦作舟'.format(s = '学海无涯'))   # 变量在format()里来定义，此时占位符要指定该变量{s}


# 有意思的是，当占位符为空，个数又少于format里字符串个数时，会按占位符个数顺序显示对应字符串；但是占位符不能多于format里字符串个数
print('{},{}'.format('a','b','c'))        # 会输出a, b
    # print('{},{}'.format('a'))    错误 × 
    
print('{0},{3},{4}'.format('a','b','c','d','e'))    # 占位符里有数字来指定字符串时
print('{1},{0},{1}'.format('a','b'))

print('-'*20)

a = 'abc{}'
print(a.format('e'))          # format()不在原字符串上改动，而是生成新的字符串
print(a)

print('-'*20)

# 数字格式控制
a = 32093.69310
print('{:.0f}'.format(a))        # 使用%i可以将浮点数直接取整数，但是format里不可以，format里严格按照相同的数据类型来执行
print('{:d}'.format(10))       # 整数只能用d，不支持i
print('{:.2e}'.format(339109393.9201903))
print('{:.2g}'.format(339109393.9201903))
print('{:.2%}'.format(0.003))   
    # 百分号,注意它会将format()里的数字换算回去，也就是说如果想要输出98.2%，要写format(0.982),而不能写format(98.2)
print('{:.1%}'.format(0.982))
```

    扶摇直上九万里
    abac
    good job
    --------------------
    学海无涯苦作舟
    学海无涯苦作舟
    a,b
    a,d,e
    b,a,b
    --------------------
    abce
    abc{}
    --------------------
    32094
    10
    3.39e+08
    3.4e+08
    0.30%
    98.2%
    


```python
# 小作业
# 1. 三引号创建一个有替行的文本，用print输出
txt = '''君不见，
黄河之水天上来，
奔流到海不复还；
君不见，
高堂明镜悲白发，
朝如青丝暮成雪。
'''
print(txt)
print('-'*20)

# 2. 申明一个字符串变量，值为文件路径
a = r'd:\py\python'
b = 'd:/py/python'
c = 'd:\\py\\python'
print(a, b, c, sep='\n')
print('-'*20)

# 3. 以下输出分别是多少：33 + '22', 33 + int('22'), '22' + str(55)      : 错误；55；2255
print(33+int('22'))
print('22'+str(55))

# 4. m = 'a,b,c', m.split()会输出什么结果？     : 将'a,b,c'作为一个元素生成列表
m = 'a,b,c'
print(m.split())
m = 'a, b, c'
print(m.split())        # 将'a,' 'b,' 'c'作为三个元素生成列表
print('-'*20)

# 5. split()和join()分别输出什么类型的数据        ： 前者列表，后者字符串

# 6. 如果想打%怎么办？
print('%.1f%%'%21.903)
print('{:.1%}'.format(0.21903))
print('-'*20)

# 7. 这样书写正确吗？为什么？ print('abc%s')%'nn'      ：错误，print()作为函数，需要接收参数
print('abc%s'%'nn')
print('-'*20)

# 8. 这样书写正确吗？为什么？ print(245%f%123)         ；错误，%属于格式化字符，是字符串类型
print('245%f'%123)
print('-'*20)

# 9. 我的工作是...我喜欢...，将...替换成正确答案
print('我的工作是{work},我喜欢{like}'.format(work='数据分析师',like='python'))

```

    君不见，
    黄河之水天上来，
    奔流到海不复还；
    君不见，
    高堂明镜悲白发，
    朝如青丝暮成雪。
    
    --------------------
    d:\py\python
    d:/py/python
    d:\py\python
    --------------------
    55
    2255
    ['a,b,c']
    ['a,', 'b,', 'c']
    --------------------
    21.9%
    21.9%
    --------------------
    abcnn
    --------------------
    245123.000000
    --------------------
    我的工作是数据分析师,我喜欢python
    


```python
x = '{:.2%}'.format(0.982)
print(x)
```

    98.20%
    
