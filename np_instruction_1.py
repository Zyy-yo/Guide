import numpy as np

# numpy:用于高性能科学计算和数据分析，常用的高级数据分析库的基础包
# 数组与数据类型，根据输入数据的类型自动进行转换
arr1 = np.array([2, 3, 4])      # 经过numpy封装，计算效率要高于python自带的列表
print(arr1)                     # [2 3 4]
print(arr1.dtype)               # int32

arr2 = np.array([1, 3.2, 5.9])
print(arr2)                     # [1.  3.2 5.9]
print(arr2.dtype)               # float64

arr3 = arr1 + arr2                # 列表相加
print(arr3)                       # [3.  6.2 9.9]

# 与标量的计算，标量指的是物理中的概念，有大小没有方向的数据，如温度、体积、质量等都属于标量
arr4 = arr1 * 9.3                 # 无需遍历循环，直接计算
print(arr4)                       # [18.6 27.9 37.2]

# 定义多维数组，如二维数组，又称为矩阵
data = [[1, 2, 3], [4, 5, 6]]     # 列表嵌套
print(data)                       # [[1, 2, 3], [4, 5, 6]]
arr5 = np.array(data)             # 将列表转换为numpy的数组形式
print(arr5)                       
'''
[[1 2 3]
 [4 5 6]]
'''

# 二维数组更改数组元素:
ar1 = np.array([[3, 9, 10], [6, 8, 1], [4, 8, 2]])
ar1[1,2] = 29      # [1,2]表示第1个数组第2个元素，即第1行第2列
print(ar1)
'''
[[ 3  9 10]
 [ 6  8 29]
 [ 4  8  2]]
'''
ar1[0:2,1:3] = 0
print(ar1)
'''
[[3 0 0]
 [6 0 0]
 [4 8 2]]
'''
# 查询数组形状
print(ar1.shape)      # (3, 3)

# 定义全部为0的数组
print(np.zeros(5))    # 一维数组，括号内是数组的长度    [0. 0. 0. 0. 0.]
print(np.zeros((2,3)))  # 二维数组，2行3列，以元组形式写成(2,3)
'''
[[0. 0. 0.]
 [0. 0. 0.]]
'''
# np.ones()定义元素全部为1的数组，np.empty()定义空的数组，用法同np.zeros()
print(np.empty((3,2,2)))    # 三维矩阵,虽然设置为空，但矩阵空值对程序计算是不安全的，因此会填充随机值
'''
[[[2.59966340e-276 1.29062229e-306]
  [8.34441742e-308 1.69118923e-306]]

 [[3.72400224e-265 2.86413206e-308]
  [9.57872064e-304 1.04786979e-250]]

 [[3.01177098e-154 7.29290379e-304]
  [7.77178018e-299 1.03615406e+304]]]
'''

'''
连续数组创建：
    np.arange(start, stop, step)      不含stop
    np.linspace(start, stop, num=50, endpoint=True)    endpoint=True，默认包含stop,若想不包含,可改为False；num为元素个数,默认50
    arange()也可以创建浮点数的数组
    linspace()默认为浮点数
'''
a = np.linspace(1, 9, 5)
b = np.arange(1, 10, 2)
print(a)                       #  [1. 3. 5. 7. 9.]
print(a.dtype)                 #  float64
print(b)                       #  [1 3 5 7 9]
print(b.dtype)                 #  int32
# 查询数组大小
print(a.size)                    # 5
print(np.size(b))                # 5

# numpy数组的索引和切片,这里的切片如果是取范围，如[1:5]，不包含右边的临界值
print(np.arange(6))            # [0 1 2 3 4 5]
print(np.arange(6)[3])         # 3
print(np.arange(6)[1:5])       # [1 2 3 4]
ar = np.arange(6)
ar[0] = 9                        # 可以通过索引直接赋值，来改变数组的值
ar[2:4] = 7                      
print(ar)                        # [9 1 7 7 4 5]

# 想要改变数组的值，但又不想原数组的值被改动
ar_r = ar.copy()                 # 将原数组copy到新数组
ar_r[:] = 10                     # [:]表示从第一个到最后一个
print(ar_r)                      # [10 10 10 10 10 10]

'''
numpy中的算术运算：
    np.add()            加
    np.subtract()       减
    np.multiply()       乘
    np.divide()         除
    np.power()          乘方
    np.remainder()      求余        或np.mod()
    np.sum()            求和
'''
a = np.array([1, 2, 5, 8, 4])
b = np.arange(1, 10, 2)
print(a,'\n',b)
print(np.sum(a))                           # 20                         
print(np.add(a, b))                        # [ 2  5 10 15 13]         同print(a+b)
print(np.add(a, 1))                        # [2 3 6 9 5]              同print(a+1) 
print(np.subtract(a, b))                   # [ 0 -1  0  1 -5]         同print(a-b)
print(np.multiply(a, b))                   # [ 1  6 25 56 36]         同print(a*b)
print(np.divide(b, 2))                     # [0.5 1.5 2.5 3.5 4.5]    同print(b/2)
print(np.power(a, 2))                      # [ 1  4 25 64 16]         同print(a ** 2)
print(np.remainder(a, b))                  # [0 2 0 1 4]              同print(a % b)      
print(np.mod(a, b))                        # [0 2 0 1 4]

'''
统计函数
'''
# 计算数组/矩阵中的最大值amax()，最小值amin()
ar2 = np.array([[2, 3, 7, 4], [8, 3, 6, 1], [5, 9, 4, 0]])
print(ar2)
'''
[[2 3 7 4]
 [8 3 6 1]
 [5 9 4 0]]
'''
print(np.amax(ar2))                        # 9
print(np.amin(ar2, 0))                     # [2 3 4 0]   amin(ar2, 0)中，0表示axis=0,轴0表示纵向，可以理解为矩阵中的列
print(np.amax(ar2, 1))                     # [7 8 9]     axis=1,轴1表示横向，可以理解为矩阵中的行

# 计算最大值与最小值之差ptp()
print(np.ptp(ar2))                           # 9        不指定轴，则将二维数组展平，计算展平后的最大值与最小值之差
print(np.ptp(ar2, 0))                        # [6 6 3 4]    axis=0计算纵向；同理，axis=1计算横向

'''
统计数组中的中位数median()，平均数mean()
    中位数:按顺序排在中间位置的数。如果样本是偶数个，则取排在中间的两个数值的平均数作为中位数
'''
print(np.median(ar2))                         # 4.0
print(np.median(ar2, 1))                      # [3.5 4.5 4.5]  
print(np.mean(ar2))                           # 4.333333333333333
print(np.mean(ar2, 0))                        # [5.         5.         5.66666667 1.66666667]

'''
加权平均值：将各数值乘以相应的权数，然后求和得到总体值，再除以总的单位数。日常生活中一般所说的权重就是指的权数。
加权平均值=各数值乘以各自的权数/权数之和
'''
ar3 = np.array([[3, 9, 2], [6, 8, 4]])
w = np.array([[2, 3, 4], [1, 7, 2]])               # 假设权重是w，注意权数形状要与数组一致
print(np.average(ar3))                             # 此时将数组展平处理，且默认权数均为1
print(np.average(ar3, 0))                          # 按照axis=0计算，默认权数均为1：[4.5 8.5 3. ]
print(np.average(ar3, 1, weights=w))               # 按照axis=1计算：[4.55555556 7.        ]

'''
方差var()   标准差std()
标准差能反映一个数据集的离散程度。平均数相同的两组数据，标准差未必相同。一组数据平均值分散程度的一种度量

离均差：各数值与平均数之差的和，和越大离散程度越大。因为其有正负，存在误差，一般取绝对值，
        即|各数值与均值之差|的和；常用的方法是取平方，（各数值与均值之差）的平方的和，即离均差平方和。
👇
方差：离均差平方和与样本个数有关，为了消除个数的影响，对离均差平方和求平均值，这也就是方差。
👇
标准差：因为方差是数据的平方，难以直观衡量，故常用方差开根号换算回来，这就是标准差。

自由度：样本量越大越能反映真实的情况，而算术平均值却完全忽略了这个问题，对此统计学上早有考虑，
        在统计学中样本的均差多是除以自由度（n-1），它的意思是样本能自由选择的程度。
        当选到只剩一个时，它不可能再有自由了，所以自由度是n-1。

标准误：抽样存在的误差，一个总体可以抽取出无数多种样本，代表样本平均数与总体平均数的误差。
        标准误=样本的标准差/样本容量的开平方
受样本量影响，样本量越大，标准误越小，则抽样误差就越小，表示抽取的样本能较好地代表总体。
'''
print('%.2f'%np.var(ar3))             # 6.56        展平处理，为方便观看，控制浮点数，保留2位小数
print(np.var(ar3, 0))                   # [2.25 0.25 1.  ]          size>1，无法采用上面的方式进行格式化输出
print(np.std(ar3, 1))                   # [3.09120617 1.63299316]

'''
numpy中的排序：sort(arrayname,axis,kind,order)
    axis默认为-1，沿最后一个轴排序。也可以指定轴。如果是None，则按扁平化排序。
    kind 种类：'quicksort'、'mergesort'、'heapsort'、'stable'，可选排序算法。
                默认值为“快速排序”。 （快速排序；合并排序；堆排序；stable）
    order，可以对结构化数组指定按照某个字段排序。
'''
ar4 = np.array([[3, 9, 10, 2],[4, 12, 5, 0],[18, 7, 6, 1]])
print(ar4)
print(np.sort(ar4))
'''
[[ 2  3  9 10]
 [ 0  4  5 12]
 [ 1  6  7 18]]
'''
print(np.sort(ar4, axis=None))              # [ 0  1  2  3  4  5  6  7  9 10 12 18]
print(np.sort(ar4, 0))
'''
[[ 3  7  5  0]
 [ 4  9  6  1]
 [18 12 10  2]]
'''

'''
连接多个数组 numpy.concatenate((a1,a2...), axis=0, out=None)
'''

n1 = np.array([[1, 3, 5],[2, 4, 6]])
n2 = np.array([[7, 0, 8]])
print(np.concatenate((n1, n2)))           # 数组要以序列的形式提供；默认按照axis=0连接
'''
[[1 3 5]
 [2 4 6]
 [7 0 8]]
'''
# 连接时，输入的数组要在维度上完全匹配，n1和n2延轴0连接的时候可以成功，但按照轴1则无法连接
n3 = np.array([[5],[9]])
print(np.concatenate((n1, n3),axis=1))
'''
[[1 3 5 5]
 [2 4 6 9]]
'''
print(np.concatenate((n1, n3),axis=None))     # [1 3 5 2 4 6 5 9]       axis=None,则展平数组

n4 = np.array([[2, 3, 3],[3, 9, 2]])
print(np.concatenate((n1, n4)))
'''
[[1 3 5]
 [2 4 6]
 [2 3 3]
 [3 9 2]]
'''
print(np.concatenate((n1, n4),axis=1))
'''
[[1 3 5 2 3 3]
 [2 4 6 3 9 2]]
'''

# 连接具有掩码的数组时，此函数无法保留掩码，若要保留，使用numpy.ma.concatenate()
ms = np.ma.arange(4)                     # 定义掩码数组
ms[:] = np.ma.masked                     # 赋值掩码元素
print(ms)                                # [-- -- -- --]
ms1 = np.arange(2, 6)
print(np.concatenate((ms, ms1)))         # [0 1 2 3 2 3 4 5]
print(np.ma.concatenate((ms, ms1)))      # [-- -- -- -- 2 3 4 5]