import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
'''
可视化视图：
	根据数据之间的关系，可以分为四类
		比较：比较数据间各类别的关系，或者是它们随着时间的变化趋势，比如折线图；
		联系：查看两个或两个以上变量之间的关系，比如散点图；
		构成：每个部分占整体的百分比，或者是随着时间的百分比变化，比如饼图；
		分布：关注单个变量，或者多个变量的分布情况，比如直方图。
	按照变量的个数，我们可以把可视化视图划分为单变量分析和多变量分析。
		单变量分析指的是一次只关注一个变量。比如我们只关注“身高”这个变量，来看身高的取值分布，而暂时忽略其他变量。
		多变量分析可以让你在一张图上可以查看两个以上变量的关系。比如“身高”和“年龄”，你可以理解是同一个人的两个参数，
			这样在同一张图中可以看到每个人的“身高”和“年龄”的取值，从而分析出来这两个变量之间是否存在某种联系。
'''


# 折线图
# plt.plot([1, 5, 10],[3, 8, 7])				#  matplotlib 
# plt.show()

# sns.lineplot([1, 5, 10],[3, 17, 12])			#  seaborn 
# plt.show()

# 曲线图
# x = np.linspace(-np.pi, np.pi, 100)			#  matplotlib
# plt.plot(x, np.sin(x))                        
# plt.show()

# 同一张图上画多条曲线
# x1 = np.linspace(-np.pi * 2, np.pi *2, 100)
# plt.figure(1, dpi=100)           # 创建图表1，dpi表示精度，精度越大，图越大越清晰
# for i in range(1,5):             # 绘制四条曲线
# 	plt.plot(x1, np.sin(x1/i))
# plt.show()

# 直方图
# x2 = [3, 3, 3, 6, 6, 8, 9, 9, 10, 10, 10]
# plt.hist(x2)									#  matplotlib
# plt.show()

# sns.distplot(x2)								#  seaborn 
# plt.show()


# 散点图
# x3 = np.random.randn(1000)
# y = np.arange(1000)
# plt.scatter(x3, y, c='r', marker='+')         # matplotlib  c即颜色，marker有'+','o','x','>'等，不同的标记符号
# plt.show()

# iris = pd.read_csv(r'D:\PY\excel_file\iris_training.csv')
# # print(iris.head())           # 显示前五行信息
# iris.plot(kind='scatter', x='120', y='4')		#  matplotlib
# plt.show()

# sns.set(style='white', color_codes=True)
# sns.jointplot(x='120', y='4', data=iris)      #  seaborn  kind默认scatter
# plt.show()

# 根据'virginica'中不同分类，使用不同颜色绘制
# sns.FacetGrid(iris, hue='virginica', height=5).map(plt.scatter, '120', '4').add_legend()   	 #  seaborn
# plt.show()

# 条形图
# x 和 y 分别代表了类别和频数
# plt.bar(['cat','dog','bird','hamster'],[9903, 12932, 6923, 5392])		#  matplotlib
# plt.show()

# sns.barplot(['cat','dog','bird','hamster'],[9903, 12932, 6923, 5392])	#  seaborn
# plt.show()

# 箱线图
# 由五个数值点组成：最大值(max)，最小值(min)，中位数(median)和上下四分位数(Q3、Q1)
# 分析数据的差异性、离散程度和异常值
# 生成0-1之间size为10行4列的数据
# data = np.random.normal(size=(10,4))
# labels = ['A','B','C','D']
# plt.boxplot(data, labels=labels)			#  matplotlib
# plt.show()

# df = pd.DataFrame(data, columns=labels)		#  先封装成DataFrame
# sns.boxplot(data=df)						#  seaborn
# plt.show()

# 饼图
# labels1代表高中、本科、硕士、博士和其他几种学历的分类标签;nums代表这些学历对应的人数
# 如何在图中显示每个区域的数量或占比？？？
# nums = [25, 36, 33, 40, 8]
# labels1 = ['High-school','Bachelor','Master','Ph.d','Others']
# plt.pie(nums, labels=labels1)
# plt.show()

# 热力图
# 一种矩阵表示方法，其中矩阵中的元素值用颜色来代表，不同颜色代表不同大小的值。
# 是一种非常直观的多元变量分析方法
# 准备数据，使用seaborn中自带的数据集flights,记录了1949年到1960年期间每个月的航班乘客的数量
# flights = sns.load_dataset('flights')
# data1 = flights.pivot('year','month','passengers')
# sns.heatmap(data1)				                         # seaborn
# plt.show()

# 蜘蛛图，见spider_chart
# 显示一对多关系的方法，蜘蛛图中，一个变量相对于另一个变量的显著性是清晰可见的。

# 二元变量分布
# 看两个变量之间的关系，二元变量分布有多种呈现方式，散点图就是一种
# seaborn中直接使用sns.joinplot函数即可，kind=scatter表示散点图,kde表示核密度图,hex表示Hexbin图，是直方图的二维模拟
# 使用seaborn自带数据集tips，记录了不同顾客在餐厅的消费账单及小费情况
# tips = sns.load_dataset('tips')
# print(tips.head())
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
# plt.show()

# 成对关系
# 探索数据集中的多个成对双变量的分布
# 使用seaborn自带数据集iris，这个数据集也叫鸢尾花数据集。鸢尾花品种：Setosa、Versicolour和Virginica
# iris1 = sns.load_dataset('iris')
# sns.pairplot(iris1)
# plt.show()