import random
# randint(a,b)  随机生成[a, b]范围内的整数
print(random.randint(1,10))           # 6

# uniform(a,b)  随机生成[a, b]范围内的浮点数
print(random.uniform(1,10))           # 7.848065876004576



# random()  随机生成[0,1]范围内的浮点数
# 扩展：round(x, k)  保留x的k位小数
print(round(random.random(),2))                # 0.38

# choice()  从序列中随机选取一个元素返回
l = ['a', 'b', 'c', 3]
print(random.choice(l))          # b 

'''
choices(population[, weights=None, cum_weights=None],k=1) 从population序列里随机返回k大小的元素列表
    k默认为1，即返回拥有一个元素的列表
    weights：相对权重，大小要与population的大小相同
    cum_weights：累积权重，大小要与population的大小相同
    在工作时，如果提供了相对权重，会先计算其累积权重，因此直接提供累积权重可以节省资源。
    weights与cum_weights不能同时提供；两者均不提供，则默认为相同权重
'''

m = '3i08m'
i = 0
while i < 10:
    print(random.choices(m))           # ['0']  ['8']  ['m']  ['0']  ['0']  ['i']  ['0']  ['3']  ['8']  ['3']
    i += 1

i = 0
while i < 10:
    print(random.choices(m, weights=[20,2,20,20,2]))           # ['0']  ['0']  ['3']  ['3']  ['8']  ['8']  ['3']  ['3']  ['3']  ['3']
    i += 1

i = 0
while i < 10:
    print(random.choices(m, cum_weights=[5,25,30,35,55]))           # ['m']  ['8']  ['i']  ['m']  ['3']  ['i']  ['i']  ['i']  ['i']  ['i']
    i += 1

# randrange(start, stop[, step])  # 随机选取范围在[start,stop)，步长为step的整数；start包含，stop不包含
print(random.randrange(1, 4, 2))       

# 扩展：range([start,] stop[, step])   [start, stop)范围内，步长为step的整数,start不写时默认为0，step不写时默认为1。
for i in range(5):
    print(i)           # 0  1  2  3  4
for i in range(2, 7, 2):
    print(i)             # 2  4  6

# sample(population,k)  从population序列随机选择k个值,返回值唯一；若原序列元素不唯一，则返回的元素也可能不唯一
print(random.sample('12l4dq', 3))         # ['d', 'q', '1']

# shuffle(x [,random])   打乱序列x，返回None
a = ['1','2','3','4']
random.shuffle(a)
print(a)                 # ['2', '4', '3', '1']
