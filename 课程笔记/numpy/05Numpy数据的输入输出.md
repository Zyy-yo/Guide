```python
'''
numpy数据读取/写入数组数据、文本数据
'''
```




    '\nnumpy数据读取/写入数组数据、文本数据\n'




```python
# 存储数组数据  .npy文件
import numpy as np
import os
os.chdir(r'D:\PY')

a = np.random.rand(5,5)
print(a)
np.save('arraydata.npy',a)        # np.save(path,arr)
```

    [[0.24976864 0.18990159 0.9323649  0.17523384 0.08030077]
     [0.15415801 0.71328866 0.13142048 0.01802169 0.09608803]
     [0.89497518 0.37317287 0.99417306 0.76453395 0.45473716]
     [0.83981234 0.85302267 0.79396621 0.55439287 0.47401221]
     [0.56467345 0.01990732 0.09315604 0.42874359 0.25252453]]
    


```python
# 读取数组数据  .npy文件

b = np.load('arraydata.npy')      # np.load(path)
print(b)

```

    [[0.24976864 0.18990159 0.9323649  0.17523384 0.08030077]
     [0.15415801 0.71328866 0.13142048 0.01802169 0.09608803]
     [0.89497518 0.37317287 0.99417306 0.76453395 0.45473716]
     [0.83981234 0.85302267 0.79396621 0.55439287 0.47401221]
     [0.56467345 0.01990732 0.09315604 0.42874359 0.25252453]]
    


```python
# 存储/读取文本文件
a = np.random.randn(4,5)
print(a)
np.savetxt('array.txt',a,delimiter=',')
    # np.savetxt(fname, arr, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')：存储为文本txt文件
    
b = np.loadtxt('array.txt', delimiter=',')       # 这里一定要注意，存储的时候有什么设置，读取的时候也要设置
print(b)
```

    [[-1.71502445 -0.67663196  0.35976181 -0.37183584 -0.43382113]
     [ 0.49908257 -0.45579469 -0.99046655  1.1194908   0.34901145]
     [-1.60502758  0.09320076 -0.12380528 -0.9863109  -0.67225483]
     [-0.60597078  0.61525088 -1.39439638  1.34333726  0.23355399]]
    [[-1.71502445 -0.67663196  0.35976181 -0.37183584 -0.43382113]
     [ 0.49908257 -0.45579469 -0.99046655  1.1194908   0.34901145]
     [-1.60502758  0.09320076 -0.12380528 -0.9863109  -0.67225483]
     [-0.60597078  0.61525088 -1.39439638  1.34333726  0.23355399]]
    


```python
# 作业
# 1. 创建一个10*10的整数随机数组，取值范围为0-100，并存为txt文件，用逗号分开	

array = np.random.randint(100,size=(10,10))       # 或randint(0,100,(10,10))
print(array)

np.savetxt('arrytest.txt',array,delimiter=',')

b = np.loadtxt('arrytest.txt',delimiter=',',dtype=np.int)         # 读取时，如果不设置dtype，默认会是浮点型
print(b,b.dtype)
```

    [[32  9 78 84 77  8 97 66 75 64]
     [23 65 67 25 38 48 33  3 70 55]
     [50 70 67 40 62 17 93 74 11 10]
     [65 43 90 70  3 33 97 15 16  6]
     [56 49 75 17 50 62 61 35 52 88]
     [70 52 30 29 18 65 79 57 35 78]
     [55 51 38 18 47 51 96  6 90 87]
     [46 40 91 25 67 21 11 49 28 43]
     [23 23 34 52 91 23 23  7 73 96]
     [62 69 27 50 34  7 29 14 43 26]]
    [[32  9 78 84 77  8 97 66 75 64]
     [23 65 67 25 38 48 33  3 70 55]
     [50 70 67 40 62 17 93 74 11 10]
     [65 43 90 70  3 33 97 15 16  6]
     [56 49 75 17 50 62 61 35 52 88]
     [70 52 30 29 18 65 79 57 35 78]
     [55 51 38 18 47 51 96  6 90 87]
     [46 40 91 25 67 21 11 49 28 43]
     [23 23 34 52 91 23 23  7 73 96]
     [62 69 27 50 34  7 29 14 43 26]] int32
    
