```python
'''
numpy.random包含多种概率分布的随机样本
'''
```




    '\nnumpy.random包含多种概率分布的随机样本\n'




```python
# 随机数生成   numpy.random.normal()
import numpy as np

samples = np.random.normal(size=(4,4))
print(samples)

   # numpy.random.normal()  随机生成一个标准正太分布的值；size=  设定样本形状
    
a = np.random.normal(size=5)
print(a)
```

    [[-1.10058382 -0.6831947  -1.09636421 -0.38279326]
     [-0.04233499 -0.33511081  0.98194121  1.79135171]
     [-0.1720386  -0.52286865 -0.25156621 -0.39483503]
     [-0.91890956 -0.89637952  0.53069713 -0.60057934]]
    [-0.09310663  0.87479777  1.24461441 -1.11311367 -1.26004878]
    


```python
# 随机数生成   numpy.random.rand(d0,d1,d2,...,dn)  生成一个[0,1)之间的随机浮点数或N维浮点数组 —— 均匀分布

import matplotlib.pyplot as plt
# %matplotlib inline             # jupyter notebook里面的魔法函数，每次运行自动生成图表。报错没有这个功能。但是不用它也可以出图。

a = np.random.rand()          # 随机生成一个浮点数
print(a, type(a))

b = np.random.rand(4)         # 随机生成shape为(4,)的一维数组
print(b, type(b))

c = np.random.rand(2,3)       # 随机生成shape为(2,3)的二维数组
print(c, type(c))


samples1 = np.random.rand(1000)
samples2 = np.random.rand(1000)
plt.scatter(samples1,samples2)
```

    0.628652024139144 <class 'float'>
    [0.90381603 0.61139073 0.6844608  0.36066542] <class 'numpy.ndarray'>
    [[0.0186842  0.17529919 0.59158079]
     [0.85152421 0.8727307  0.13690097]] <class 'numpy.ndarray'>
    




    <matplotlib.collections.PathCollection at 0xba9a1f0>




![png](output_2_2.png)



```python
# 随机数生成   numpy.random.randn(d0,d1,d2,...,dn)   生成一个浮点数或N维浮点数组 —— 正态分布

a = np.random.randn()
print(a, type(a))

b = np.random.randn(2,3)
print(b, type(b))

samples1 = np.random.randn(1000)
samples2 = np.random.randn(1000)
plt.scatter(samples1,samples2)

     # 参数用法和numpy.random.rand()一样
```

    -0.07996959258123396 <class 'float'>
    [[-0.55511166  0.27982681 -0.68501049]
     [-1.84457175  1.09824539  0.89875793]] <class 'numpy.ndarray'>
    




    <matplotlib.collections.PathCollection at 0xbb59770>




![png](output_3_2.png)



```python
# 随机数生成   numpy.random.randint(low, high=None,size=None,dtype='l')   生成一个整数或N维整数数组
# 若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数，且high必须大于low 
# dtype参数：只能是int类型  

a = np.random.randint(3)           # low = 3 ,取[0,3)之间的一个整数
print(a,type(a))

b = np.random.randint(5,size=5)       # 生成[0,5)之间的shape(5,)的一维数组
print(b, type(b))

c = np.random.randint(2,8,size=(2,3))    # low=2, high=8,生成[2,8)之间的shape(2,3)的二维数组
print(c, type(c))


```

    0 <class 'int'>
    [2 3 0 1 2] <class 'numpy.ndarray'>
    [[5 6 2]
     [4 2 7]] <class 'numpy.ndarray'>
    


```python
# 作业
# 1. 请按照要求创建数组ar，再将ar[:2,:2]的值改为[0,1)的随机数

a = np.arange(25, dtype=float).reshape(5,5)
print(a)

a[:2,:2] = np.random.rand(2,2)        # 这里注意，如果不写形状的话，只会是同一个值
print(a)
```

    [[ 0.  1.  2.  3.  4.]
     [ 5.  6.  7.  8.  9.]
     [10. 11. 12. 13. 14.]
     [15. 16. 17. 18. 19.]
     [20. 21. 22. 23. 24.]]
    [[ 0.19235715  0.27567848  2.          3.          4.        ]
     [ 0.42110694  0.78387227  7.          8.          9.        ]
     [10.         11.         12.         13.         14.        ]
     [15.         16.         17.         18.         19.        ]
     [20.         21.         22.         23.         24.        ]]
    


```python
# 2. 创建2个包含10个元素的正太分布一维数组(这题目有点不清晰)

a1 = np.random.randn(2,5)
print(a1,a1.shape)

b1 = np.random.normal(size=(2,5))
print(b1)
```

    [[ 0.88538832 -0.43485524  0.61116375  1.01365262 -0.43320364]
     [ 1.00627576 -0.90673634  0.08252336  0.80665426 -1.27773435]] (2, 5)
    [[-1.04897945 -0.19717317  0.54694459 -1.21266112  1.21725164]
     [ 0.5703237  -0.31818436 -0.71766688  0.10910537  0.57191354]]
    
