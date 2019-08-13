from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.datasets import load_iris, load_boston
import numpy
# 准备数据集，导入iris数据集，对其构建一棵分类决策树
iris = load_iris()
# 获取特征集和分类标识
features = iris.data
labels = iris.target
# 随机抽取33%的数据作为测试集，其余为训练集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
# 创建初始化cart分类树
clf = DecisionTreeClassifier(criterion='gini')
# 拟合构造cart分类树，将训练集的特征值和分类标识作为参数进行拟合
clf = clf.fit(train_features, train_labels)
# 用cart分类树做预测，传入测试集的特征值，得到测试结果
test_predict = clf.predict(test_features)
# 预测结果与测试集结果做比对，传入测试集的实际结果和预测结果，得到准确率
score = accuracy_score(test_labels, test_predict)
print('cart分类树准确率 %.4f'%score)


# 使用sklearn自带数据集波士顿房价数据集，该数据集给出了影响房价的一些指标如犯罪率，房产税等，最后给出房价
# 根据这些指标，使用cart回归树对波士顿房价进行预测
# 准备数据集
boston = load_boston()
# print(boston.feature_names)
# 获取特征集和房价
features_b = boston.data
prices = boston.target
# 随机抽取33%作为测试集，其余为训练集
train_features_b, test_features_b, train_prices, test_prices = train_test_split(features_b, prices, test_size=0.33)
# 创建cart回归树
dtr = DecisionTreeRegressor()
# 拟合构造cart回归树
dtr.fit(train_features_b, train_prices)
# 预测测试集中的房价
predict_price = dtr.predict(test_features_b)
# 测试集的结果评价
print('回归树二乘偏差均值：', mean_squared_error(test_prices, predict_price))
print('回归树绝对值偏差均值：', mean_absolute_error(test_prices, predict_price))