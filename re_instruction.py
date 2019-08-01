import re
'''
字符匹配：re.match(pattern,str,flags=0)     从字符串的起始位置开始匹配，若起始位置不匹配，则不匹配
    pattern:模式，即正则表达式
    str:要匹配的字符串
    flags:标志位，控制正则表达式的匹配方式，如是否区分大小写
字符搜索：re.search(pattern,str,flags=0)    搜索整个字符串，并返回第一个成功的匹配
         re.findall(pattern,str,flags=0)    搜索整个字符串，并以列表形式返回所有匹配
字符替换：re.sub(pattern,repl,str,count=0,flags=0)
    repl:替换的字符串
    str:原字符串
    count:模式匹配后替换的最大次数，默认0表示替换所有的匹配项
字符分割：re.split(pattern,str[,maxsplit=0,flags=0])  以pattern模式将str进行分割
    maxsplit:设定最大分割次数，0表示符合正则表达式的则全部分割
'''

'''
常用模式：
    1，匹配位置
        元字符： ^  以……为开头      
                $   以……为结尾           例4
    2，匹配内容
        元字符： .  匹配任何单个字符，除\n以外；    例2
                []  里面的任何一个字符匹配成功，则成功匹配并结束匹配        例1 
                [^] 匹配不在[]里面的字符          例1
                \d  匹配一个数字字符，等价于[0-9]       例1；例2
                \D  匹配一个非数字字符，包括下划线_感叹号等符号，以及空格，等价于[^0-9]        例1；例3
                \s  匹配任何空白字符，包括制表符、空格、换页符，等价于[\f\n\r\t\v]      例2
                \S  匹配任何非空白字符
                \w  匹配包括下划线在内的任何单词字符，等价于[A-Za-z0-9_],可以匹配：汉字  数字  英文  下划线_           例1
                \W  匹配任何非单词字符，相当于[^A-Za-z0-9_]           例1
                |   匹配|左边或右边的字符，意为‘或’             例4
    3，匹配次数
        元字符： *   表示前面的字符出现0次到多次，都可以匹配            例1;例2
                +   表示前面的字符出现1次到多次，都可以匹配            例1；例2；例3
                ?   表示只匹配0次到1次符合正则表达式的字符串，非贪婪模式     例3
                {n} 表示前面的字符出现n次                    例2
                {n,m}  表示前面的字符出现n到m次               例3
    4，分组
        元字符： () 进行分组，分组的内容可以进行提取              例2
                    提取方式：groups()   以元组方式提取组内项
                             group(n)   提取第n个组内项
                             group()    提取所有的匹配，不管是不是在组里
'''
# 例1
s = '我爱你_1314love'
m1 = re.match(r'\w*',s)         # 匹配项：match='我爱你_1314love'
m2 = re.match(r'[\w*]',s)       # 匹配项：match='我'
m3 = re.match(r'[\w]+',s)       # 匹配项：match='我爱你_1314love'

m4 = re.match(r'\W*',s)         # 匹配项：match=''
m5 = re.match(r'[^\W]*',s)      # 匹配项：match='我爱你_1314love'

m6 = re.split(r'[A-Za-z]',s)    # 分割后：['我爱你_1314', '', '', '', '']
m7 = ''.join(m6)                # print：我爱你_1314

m8 = re.match(r'\d+',s)         # 匹配项：None
m9 = re.search(r'\d+',s)        # 匹配项：match='1314'

m10 = re.search(r'\D*',s)       # 匹配项：match='我爱你_'
m11 = re.search(r'[^\d_]+',s)   # 匹配项：match='我爱你'
m12 = re.search(r'[a-z]+',s)    # 匹配项：match='love'
m13 = re.findall(r'[^\d_]+',s)  # 匹配项：['我爱你', 'love']

# 例2
st = '2003-10-1  2003-1-29'
a = re.match(r'(\d+)-(\d+)-(\d+)',st)                # 匹配项： match='2003-10-1'
print(a.group())                                     # 2003-10-1
a1 = re.match(r'(\d{4})-(\d+)-(\d+)\s{2}(\d{4})-(\d+)-(\d+)',st)       # 匹配项：match='2003-10-1  2003-1-29'
a2 = re.match(r'.*',st)                                                # 匹配项：match='2003-10-1  2003-1-29'
print(a1.groups())                # ('2003', '10', '1', '2003', '1', '29')
print(a1.group(1))                # 2003
print(a1.group(6))                # 29
a3 = re.findall(r'(\d{4})-(\d+)-(\d+)',st)            # 匹配项：[('2003', '10', '1'), ('2003', '1', '29')]

# 例3
stri = '520ILoveYou!1314'
t = re.match(r'\d+',stri)                             # 匹配项： match='520'
t1 = re.match(r'\d?',stri)                            # 匹配项： match='5'
t2 = re.search(r'\D*',stri)                           # 匹配项： match=''
t3 = re.search(r'\D{1,5}',stri)                       # 匹配项： match='ILove'

# 例4
strin = '5times'
c = re.match(r'a|5\D',strin)                         # 匹配项： match='5t'
c1 = re.search(r'\D+$',strin)                        # 匹配项： match='times'
c2 = re.sub(r'\D+','次',strin)                       # print: 5次
