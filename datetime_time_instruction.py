import time
import datetime 
print(time.time())  # 1970年1月1日到现在所经历的秒数
print(time.localtime())         # 当前时间的结构化输出，tm_wday从0到6，0代表周一；tm_yday从1月1日到现在的天数; tm_isdst是否为夏令时，取值为-1，0，1
print(time.strftime(r'%Y-%m-%d %H:%M:%S'))    # 当前时间的格式化输出，输出字符串格式

print(datetime.datetime.now())   # 当前日期与时间
# 计算日期的加减
oneday = datetime.datetime(2008,2,21)   # 2008年2月21日，datetime格式
day = datetime.timedelta(days=20,hours=3,minutes=20,seconds=48)      # 相差20天3小时20分钟48秒
newday = oneday + day
print(newday)           # 新的日期的datetime格式输出
  
print(datetime.datetime.now() - newday)    # 现在与newday的时间差

aday = datetime.datetime.strptime('20190801',r'%Y%m%d')  # 传入字符串格式日期，格式化输出datetime格式的日期
print(type(aday))

