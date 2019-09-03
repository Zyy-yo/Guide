```python
'''
时间模块：datetime

datetime模块，主要掌握：datetime.date(), datetime.datetime(), datetime.timedelta()

日期解析方法：parser.parse

'''
```




    '\n时间模块：datetime\n\ndatetime模块，主要掌握：datetime.date(), datetime.datetime(), datetime.timedelta()\n\n日期解析方法：parser.parse\n\n'




```python
# datetime.date：date对象  
# datetime.date.today()  返回今日

from datetime import date

today = date.today()           # datetime date格式
print(today, type(today))
print(str(today), type(str(today)))

t = date(2019,2,3)          # datetime.date(年，月，日) 返回datetime date格式的日期
print(t, type(t))
```

    2019-09-03 <class 'datetime.date'>
    2019-09-03 <class 'str'>
    2019-02-03 <class 'datetime.date'>
    


```python
# datetime.datetime：datetime对象
from datetime import datetime

now = datetime.now()               # datetime.datetime.now()  返回当前日期和时间  datetime.datetime类格式
print(now, type(now))
print(str(now))                 # 转化为字符串


t1 = datetime(2013,8,10)             # datetime.datetime(年，月，日，时，分，秒)  返回datetime.datetime类格式的日期和时间
t2 = datetime(2013,9,2,11,23,59)
print(t1, type(t1))
print(t2, type(t2))


print(t2 - t1)             # datetime格式可以计算，相减得到时间差
```

    2019-09-03 10:28:01.913740 <class 'datetime.datetime'>
    2019-09-03 10:28:01.913740
    2013-08-10 00:00:00 <class 'datetime.datetime'>
    2013-09-02 11:23:59 <class 'datetime.datetime'>
    23 days, 11:23:59
    


```python
# datetime.timedelta：时间差
import datetime
today = datetime.datetime.today()             # datetime.datetime也有.today()方法
yesterday = today - datetime.timedelta(1)
print(today)
print(yesterday)
print(today + datetime.timedelta(10))           # 时间差主要用来作时间的加减法
```

    2019-09-03 10:30:51.157511
    2019-09-02 10:30:51.157511
    2019-09-13 10:30:51.157511
    


```python
# parser.parse：日期字符串转换
from dateutil.parser import parse
date = '12-21-2016'
t = parse(date)    
# 和datetime.datetime(年，月，日，时，分，秒)转换的结果一样，区别是parse(str)参数是字符串，datetime.datetime()参数是直接输入逗号分隔的数字
print(t, type(t))

print(parse('2009-10-29'),                # 年在前，则依照年月日的顺序
      parse('5/1/2019'),
      parse('5/1/2019', dayfirst=True),       # 年在后，默认月在前，日在后，可以通过dayfirst=True来改变
      parse('29.3.2009 19:32:3'),            # 年在后，月不可能是29，自动识别日月
      parse('Sept 25, 2093 10:42 AM'),            # 不支持中文
      sep='\n')
```

    2016-12-21 00:00:00 <class 'datetime.datetime'>
    2009-10-29 00:00:00
    2019-05-01 00:00:00
    2019-01-05 00:00:00
    2009-03-29 19:32:03
    2093-09-25 10:42:00
    


```python
# 作业
# 1. 请调用datetime模块，输出以下时间信息

# 输出当前日期和时间

import datetime
now = datetime.datetime.now()
print(now)

# 输出时间：2017-05-01 12:30:00
time1 = datetime.datetime(2017,5,1,12,30)
print(time1)

# 输出时间 ： 2000-12-01 00：00：00
time2 = datetime.datetime(2000,12,1)
print(time2)
```

    2019-09-03 10:54:22.554774
    2017-05-01 12:30:00
    2000-12-01 00:00:00
    


```python
# 请创建时间变量‘2000年5月1日’，求出1000天之后是哪年哪月哪日？

import datetime

d = datetime.date(2000,5,1)
print(d)
d2 = d + datetime.timedelta(1000)
print(d2)
```

    2000-05-01
    2003-01-26
    
