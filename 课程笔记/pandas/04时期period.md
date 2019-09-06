```python
'''
pd.Period()

'''
```




    '\npd.Period()\n\n'




```python
# pd.Period()  创建时期
import pandas as pd

p = pd.Period('2017', freq='M')
print(p, type(p))
  # 生成一个以2017-01开始，月为频率的时间构造器
# pd.Period()参数：一个时间戳 + freq 参数 → freq 用于指明该 period 的长度，时间戳则说明该 period 在时间轴上的位置

 # 通过加减整数，将周期整体移动
    
print(p+1)    # 加1月
print(p-2)    # 减2月

print(pd.Period('2012', freq='A-DEC') - 1)
   
print(pd.Period('2019', freq='D') - 1)
```

    2017-01 <class 'pandas._libs.tslibs.period.Period'>
    2017-02
    2016-11
    2011
    2018-12-31
    


```python
# pd.period_range() 创建时期范围

import numpy as np

ran = pd.period_range('1/1/2001', '1/1/2002', freq='M')   # 'M' 按月,只显示到月
print(ran, type(ran))
print(ran[0], type(ran[0]))      # 数据格式PeriodIndex, 单个数据格式为Period

print(pd.period_range('1/1/2001', '1/1/2002', freq='D'))   # 'D'按天


   # 与date_range()的不同
r = pd.date_range('1/1/2001', '1/1/2002', freq='M')
print(r)


ts = pd.Series(np.random.rand(len(ran)), index=ran)        # 时间序列
print(ts, type(ts))
print(ts.index)

# Timestamp表示一个时间戳，是一个时间截面；Period是一个时期，是一个时间段！！但两者作为index时区别不大

print(pd.period_range('20110102','20220304', freq = 'A'))   # A-DEC
```

    PeriodIndex(['2001-01', '2001-02', '2001-03', '2001-04', '2001-05', '2001-06',
                 '2001-07', '2001-08', '2001-09', '2001-10', '2001-11', '2001-12',
                 '2002-01'],
                dtype='period[M]', freq='M') <class 'pandas.core.indexes.period.PeriodIndex'>
    2001-01 <class 'pandas._libs.tslibs.period.Period'>
    PeriodIndex(['2001-01-01', '2001-01-02', '2001-01-03', '2001-01-04',
                 '2001-01-05', '2001-01-06', '2001-01-07', '2001-01-08',
                 '2001-01-09', '2001-01-10',
                 ...
                 '2001-12-23', '2001-12-24', '2001-12-25', '2001-12-26',
                 '2001-12-27', '2001-12-28', '2001-12-29', '2001-12-30',
                 '2001-12-31', '2002-01-01'],
                dtype='period[D]', length=366, freq='D')
    DatetimeIndex(['2001-01-31', '2001-02-28', '2001-03-31', '2001-04-30',
                   '2001-05-31', '2001-06-30', '2001-07-31', '2001-08-31',
                   '2001-09-30', '2001-10-31', '2001-11-30', '2001-12-31'],
                  dtype='datetime64[ns]', freq='M')
    2001-01    0.837805
    2001-02    0.615841
    2001-03    0.462897
    2001-04    0.255560
    2001-05    0.794671
    2001-06    0.615647
    2001-07    0.633848
    2001-08    0.835795
    2001-09    0.550812
    2001-10    0.042797
    2001-11    0.317493
    2001-12    0.937856
    2002-01    0.437126
    Freq: M, dtype: float64 <class 'pandas.core.series.Series'>
    PeriodIndex(['2001-01', '2001-02', '2001-03', '2001-04', '2001-05', '2001-06',
                 '2001-07', '2001-08', '2001-09', '2001-10', '2001-11', '2001-12',
                 '2002-01'],
                dtype='period[M]', freq='M')
    PeriodIndex(['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                 '2019', '2020', '2021', '2022'],
                dtype='period[A-DEC]', freq='A-DEC')
    


```python
# asfreq   频率转换

p = pd.Period('2017', 'A-DEC')
print(p)

print(p+1)   # 加1年

p1 = p.asfreq('M')  # 转换为月，默认最后一个月，how='E'/'end'
print(p1)
print(p1-3)   # 减3月

p2 = p.asfreq('D', how='S')   # 转换为天，how='S'/'start',因为上面是2017年的时期，这里转换为这年的第一天，即2017-01-01
print(p2)

pp = pd.Period('201808', 'M')        # 2018-08时期
print(pp)

print(pp.asfreq('D', how='S'))       # 2018-08时期的第一天即2018-08-01

print('-'*30)

ran1 = pd.period_range('2017','2018',freq='M')

ts1 = pd.Series(np.random.rand(len(ran1)), index=ran1)
ts2 = pd.Series(np.random.rand(len(ran1)), index=ran1.asfreq('D', how='S'))
print(ran1)

print(ts1, len(ts1))
print(ts2, len(ts2))
```

    2017
    2018
    2017-12
    2017-09
    2017-01-01
    2018-08
    2018-08-01
    ------------------------------
    PeriodIndex(['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
                 '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
                 '2018-01'],
                dtype='period[M]', freq='M')
    2017-01    0.641943
    2017-02    0.962968
    2017-03    0.277485
    2017-04    0.672630
    2017-05    0.518311
    2017-06    0.407710
    2017-07    0.262293
    2017-08    0.093281
    2017-09    0.616941
    2017-10    0.994878
    2017-11    0.360133
    2017-12    0.525839
    2018-01    0.643532
    Freq: M, dtype: float64 13
    2017-01-01    0.264775
    2017-02-01    0.068706
    2017-03-01    0.812309
    2017-04-01    0.644789
    2017-05-01    0.217148
    2017-06-01    0.811103
    2017-07-01    0.491894
    2017-08-01    0.775591
    2017-09-01    0.706333
    2017-10-01    0.539757
    2017-11-01    0.522610
    2017-12-01    0.598580
    2018-01-01    0.743601
    Freq: D, dtype: float64 13
    


```python
# 时间戳与时期之间的转换  pd.to_period()  pd.to_timestamp()

# 要注意不能和pd.to_datetime搞混淆了。

ran = pd.date_range('2017.2.2', periods=10, freq='M')
p = pd.period_range('2017','2018',freq='M')

ts1 = pd.Series(np.random.rand(len(ran)), index=ran)
print(ts1.head())
ts1_top = ts1.to_period()              # datetimenndex 转为 periodindex, 每月最后一日转化为每月
print(ts1_top.head(), type(ts1_top.index))


ts2 = pd.Series(np.random.rand(len(p)), index=p)
print(ts2.head())
print(ts2.to_timestamp().head(), type(ts2.to_timestamp().index))      # periodindex转为datetimeindex, 每月转为每月第一天

#      pd.to_timestamp() 参数how默认='s'/'start'
```

    2017-02-28    0.266143
    2017-03-31    0.892946
    2017-04-30    0.963204
    2017-05-31    0.283418
    2017-06-30    0.866545
    Freq: M, dtype: float64
    2017-02    0.266143
    2017-03    0.892946
    2017-04    0.963204
    2017-05    0.283418
    2017-06    0.866545
    Freq: M, dtype: float64 <class 'pandas.core.indexes.period.PeriodIndex'>
    2017-01    0.451774
    2017-02    0.741128
    2017-03    0.535924
    2017-04    0.879978
    2017-05    0.675888
    Freq: M, dtype: float64
    2017-01-01    0.451774
    2017-02-01    0.741128
    2017-03-01    0.535924
    2017-04-01    0.879978
    2017-05-01    0.675888
    Freq: MS, dtype: float64 <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
    2017-01   1970-01-01
    2017-02   1970-01-01
    2017-03   1970-01-01
    2017-04   1970-01-01
    2017-05   1970-01-01
    2017-06   1970-01-01
    2017-07   1970-01-01
    2017-08   1970-01-01
    2017-09   1970-01-01
    2017-10   1970-01-01
    2017-11   1970-01-01
    2017-12   1970-01-01
    2018-01   1970-01-01
    Freq: M, dtype: datetime64[ns]
    


```python
# 作业
# 请输出以下时间序列，使用pd.period_range()

# 1. 2017-1  长度5

r1 = pd.period_range('2017', periods=5, freq='M')
ts1 = pd.Series(np.random.rand(len(r1)), index=r1)
print(ts1)

# 2. 2017-1-1 00:00  长度5  freq:2H

r2 = pd.period_range('2017', periods=5, freq='2H')
ts2 = pd.Series(np.random.rand(len(r2)), index=r2)
print(ts2)
```

    2017-01    0.499704
    2017-02    0.183032
    2017-03    0.692274
    2017-04    0.834024
    2017-05    0.067098
    Freq: M, dtype: float64
    2017-01-01 00:00    0.772023
    2017-01-01 02:00    0.264724
    2017-01-01 04:00    0.701732
    2017-01-01 06:00    0.044026
    2017-01-01 08:00    0.930654
    Freq: 2H, dtype: float64
    
