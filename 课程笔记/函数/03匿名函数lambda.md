```python
'''
lambda的主体是一个表达式，而不是代码块
lambda表达式只有一行，只能封装有限的逻辑进去
lambda不需要函数名
'''
```




    '\nlambda的主体是一个表达式，而不是代码块\nlambda表达式只有一行，只能封装有限的逻辑进去\nlambda不需要函数名\n'




```python
# 小作业
# 1.用lambda创建一个求元素个数的匿名函数
lst = [1, 3, 3, 4, 5, 8]
f = lambda x:len(x)
print(f(lst))

```

    6
    


```python
# 2. 定义一个函数，可将输入的所有数字从大到小依次排序
def shuru():
    try:
        nume = []
        nume2 = []
        nums = eval((input('输入需要排序的所有数字,用,隔开：')))
        for i in nums:
            i = str(i)
            nume.append(i)
            numes = ''.join(nume)
        if numes.isnumeric():
            for i in nume:
                i = int(i)
                nume2.append(i)
            return sorted(nume2, reverse=True)
        else:
            return '含有非数字字符'
    except (NameError,SyntaxError):
        return '非法字符'

print(shuru())
       
'''
问题：
1，从input里输入数字来做比较，在输入方面会出现很多问题，下面这些已解决：
    1）当输入中文标点符号：SyntaxError: invalid character in identifier
    2）当空格的时候：SyntaxError: unexpected EOF while parsing
    3）当输入的字符串缺少引号：SyntaxError: EOL while scanning string literal
    4）当输入字母：NameError：** is not defined.
2，如果是小数，上面的代码无法做出判断
''' 
```

    输入需要排序的所有数字,用,隔开：3,22,9,8
    [22, 9, 8, 3]
    




    '\n问题：\n1，从input里输入数字来做比较，在输入方面会出现很多问题，下面这些已解决：\n    1）当输入中文标点符号：SyntaxError: invalid character in identifier\n    2）当空格的时候：SyntaxError: unexpected EOF while parsing\n    3）当输入的字符串缺少引号：SyntaxError: EOL while scanning string literal\n    4）当输入字母：NameError：** is not defined.\n2，如果是小数，上面的代码无法做出判断\n'




```python
# 2. 定义一个函数，可将输入的所有数字从大到小依次排序   精简版
def s(x):
    return sorted(x,reverse=True)

def shuru():
    while True:
        try:
            nums = eval((input('输入需要排序的所有数字,用,隔开：')))
            return s(nums)
        except (NameError,SyntaxError):
            print('非法字符，请重新输入数字')
print(shuru())
```

    输入需要排序的所有数字,用,隔开：33,99,28.8,31
    [99, 33, 31, 28.8]
    


```python
# 3.定义一个函数，随机输入一个学生的成绩后，学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下用C表示，最后输出成绩评分。

lst = []
def chengji():
    while True:
        dic = {}
        print('是否查询学生成绩？Y/N')
        x = input('')
        if x == 'Y' or x == 'y':
            xm = input('输入学生姓名：')
            cj = input('输入学生成绩：')
            try:
                cj = float(cj)
                dic['name'] = xm
                dic['score'] = cj
                if cj >= 90:
                    dic['grade'] = 'A'
                elif cj < 60:
                    dic['grade'] = 'C'
                else:
                    dic['grade'] = 'B'
                lst.append(dic)
                print('该生评分：%s'%dic['grade'])
            except ValueError:
                print('请输入正确的成绩')
        elif x == 'N' or x =='n':
            break
        else:
            print('查成绩请输入Y，退出请输入N')

chengji()
print('您查询过的学生成绩：\n {}'.format(lst))

'''
出现一个问题，已解决，注意：
dic不能定义为全局变量，且要放到while循环里，这样一次完整查询之后，dic就会清空。
否则key相同，value会替换掉前面的，与此同时，lst里永远存储的是最后一次查询的明细。
'''

```

    是否查询学生成绩？Y/N
    y
    输入学生姓名：x
    输入学生成绩：7
    该生评分：C
    是否查询学生成绩？Y/N
    y
    输入学生姓名：9
    输入学生成绩：99
    该生评分：A
    是否查询学生成绩？Y/N
    y
    输入学生姓名：5
    输入学生成绩：9
    该生评分：C
    是否查询学生成绩？Y/N
    n
    您查询过的学生成绩：
     [{'name': 'x', 'score': 7.0, 'grade': 'C'}, {'name': '9', 'score': 99.0, 'grade': 'A'}, {'name': '5', 'score': 9.0, 'grade': 'C'}]
    




    '\n出现一个问题，已解决，注意：\ndic不能定义为全局变量，且要放到while循环里，这样一次完整查询之后，dic就会清空。\n否则key相同，value会替换掉前面的，与此同时，lst里永远存储的是最后一次查询的明细。\n'




```python
# 4. 定义一个函数，可以统计出输入任意的字符中英文字母、空格、数字或其他字符的个数

def f():
    x = input('输入任意字符\n')
    cn = 0
    ca = 0
    cs = 0
    co = 0
    for i in x:
        if i.isnumeric():
            cn += 1
        elif i.isalpha():
            ca += 1
        elif i.isspace():           # 判断是否是空格
            cs += 1
        else:
            co += 1
    print('{} 中数字有{}个,字母有{}个,空格有{}个,其他字符有{}个'.format(x,cn,ca,cs,co))
f()
```

    输入任意字符
    jdal'dkm@#99  2 kda'
    jdal'dkm@#99  2 kda' 中数字有3个,字母有10个,空格有3个,其他字符有4个
    
