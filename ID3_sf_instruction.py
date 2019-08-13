from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
from sklearn import tree
import graphviz
import os

'''
泰坦尼克生存预测，对测试集中的乘客是否幸存进行预测。该怎么知道测试集中每个乘客最终的预测结果？
'''

'''
sklearn中自带的决策树分类器DecisionTreeClassifier
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None, max_features=None, max_leaf_nodes=None,
                        min_impurity_decrease=0.0, min_impurity_split=None, min_samples_leaf=1, min_samples_split=2,
                        min_weight_fraction_leaf=0.0, presort=False, random_state=None, splitter='best')
    class_weight：类别权重；默认为None，dict类型：指定样本各类别的权重，权重大的类别在决策树构造的时候会进行偏倚。
                 balanced类型：算法自己计算权重，样本量少的类别所对应的样本权重会更高。
    criterion：基于特征划分数据集合时，选择特征的标准。默认为gini，即基尼系数；也可以是entropy，即熵
    max_depth：决策树的最大深度，控制深度防止过拟合
    max_features：划分数据集时考虑的最多的特征值数量，为int或float型。int值是每次split时最大特征数；float值是百分数
    max_leaf_nodes：最大叶子节点数。int类型，默认为None。特征多时，通过设置最大叶子节点数防止过拟合
    min_impurity_decrease：节点划分最小不纯度，float型，默认为0.节点不纯度必须大于此值，否则该节点不再生成子节点。
    min_impurity_split：信息增益的阈值，信息增益必须大于这个阈值，否则不分裂
    min_samples_leaf：叶子节点需要的最少样本数。若小于这个阈值，会被剪枝。int类型代表最小样本数;float类型表示百分数
    min_samples_split：默认值为2，当节点的样本数少于该值时，不再分裂。
    min_weight_fraction_leaf：叶子最小权重分数？？
    presort：拟合前是否对数据进行排序来加快树的构建。数据集较小时，presort=True能加快分类器构造速度；数据集庞大时，效果相反。
    random_state：？？
    splitter：构造树时，选择属性特征的原则。best表示在所有的特征中选择最好的，random代表在部分特征中选择最好的。
'''
# 准备阶段：获取数据，并对训练集和测试集的数据进行探索，分析数据质量，对数据进行清洗，选择需要的特征对数据进行降维，方便后续分类运算。
# 分类阶段：对训练集的特征矩阵、分类结果得到决策树分类器；然后将分类器运用于测试集。之后对分类器的准确性进行分析，并对决策树模型可视化。

# 获取数据
train_data = pd.read_csv(r"D:\data\Titanic_Data-master\train.csv")
test_data = pd.read_csv(r"D:\data\Titanic_Data-master\test.csv")
# 数据探索
print(train_data.info())                      # 了解数据表基本情况
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64               # 乘客编号
Survived       891 non-null int64               # 是否幸存
Pclass         891 non-null int64               # 船票等级
Name           891 non-null object              # 乘客姓名
Sex            891 non-null object              # 乘客性别
Age            714 non-null float64             # 乘客年龄
SibSp          891 non-null int64               # 亲戚数量（兄妹、配偶）
Parch          891 non-null int64               # 亲戚数量（父母、子女）
Ticket         891 non-null object              # 船票号码
Fare           891 non-null float64             # 船票价格
Cabin          204 non-null object              # 船舱
Embarked       889 non-null object              # 登陆港口
dtypes: float64(2), int64(5), object(5)
memory usage: 66.2+ KB
None
'''
print(train_data.describe())
'''
PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
'''
print(train_data.describe(include=['O']))                  # 查看字符串类型（非数字）的整体情况
'''
Name   Sex  Ticket    Cabin Embarked
count                 891   891     891      204      889
unique                891     2     681      147        3
top     Fortune, Mr. Mark  male  347082  B96 B98        S
freq                    1   577       7        4      644
'''
print(train_data.head())
'''
PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
'''
print(train_data.tail())                        # 查看数据表的后5行
'''
PassengerId  Survived  Pclass                                      Name     Sex   Age  SibSp  Parch      Ticket   Fare Cabin Embarked
886          887         0       2                     Montvila, Rev. Juozas    male  27.0      0      0      211536  13.00   NaN        S
887          888         1       1              Graham, Miss. Margaret Edith  female  19.0      0      0      112053  30.00   B42        S
888          889         0       3  Johnston, Miss. Catherine Helen "Carrie"  female   NaN      1      2  W./C. 6607  23.45   NaN        S
889          890         1       1                     Behr, Mr. Karl Howell    male  26.0      0      0      111369  30.00  C148        C
890          891         0       3                       Dooley, Mr. Patrick    male  32.0      0      0      370376   7.75   NaN        Q
'''

# 数据清洗 ———— 缺失值处理;从info中可以看出，non-null表示有多少个非缺失值
# 训练集和测试集中，Age均有少量缺失值，这个字段是数值型，可以通过平均值补齐
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
# 测试集中，Fare有少量缺失值，通过平均值补齐
test_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
# 训练集和测试集中，Cabin均有缺失值，训练集中缺失77%，测试集中缺失78%，缺失量太大，无法补齐
# 训练集中，Embarked登陆港口少量缺失，通过计数可以发现一共有三个港口，S港口占比72%，此处用S港口来补齐缺失值
print(train_data.Embarked.value_counts())
train_data['Embarked'].fillna('S', inplace=True)

# 特征选择
# 放弃对分类没有作用的字段以及缺失值太多的Cabin字段，其余字段有船票等级、性别、年龄、亲戚数量以及船票价格，可能会对分类有影响
# 将选择的字段放到特征向量features里
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
test_features = test_data[features]
train_labels = train_data['Survived']
# 特征里的一些字段是字符串，不方便后续运算，需要转成数值类型
# Sex里有male和female两种取值，将其变成Sex=male和Sex=female两个字段，用0和1来表示;Embarked同样
dvec = DictVectorizer(sparse=False)           # 处理符号化的对象，将符号转成数字 0/1 进行表示
# fit_transform将特征向量转化为特征值矩阵
'''
关于fit_transform和transform：
    fit：从一个训练集中学习模型参数，其中就包括了归一化时用到的均值，标准偏差等，可以理解为一个训练过程。
    transform：在fit的基础上，对数据进行标准化，降维，归一化等数据转换操作
    fit_transform: 将模型训练和转化合并到一起，训练样本先做fit，得到mean，standard deviation，然后将这些参数用于transform（归一化训练数据），
    使得到的训练数据是归一化的。
'''
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
test_features = dvec.fit_transform(test_features.to_dict(orient='record'))
# print(dvec.feature_names_)             # 查看dvec的feature_names_属性值
'''
['Age', 'Embarked=C', 'Embarked=Q', 'Embarked=S', 'Fare', 'Parch', 'Pclass', 'Sex=female', 'Sex=male', 'SibSp']
'''
# 构造ID3决策树
clf = DecisionTreeClassifier(criterion='entropy')
# 拟合ID3决策树
clf.fit(train_features, train_labels)
# 预测
pred_labels = clf.predict(test_features)
# 查看预测准确率，因为不知道真实的预测结果，所以无法用预测值和真实的预测结果做比较，只能用训练集中的数据进行模型评估
score_t = clf.score(train_features, train_labels)
print('准确率%.4f'%score_t)
'''
准确率0.9820
'''
# 然而用训练集自身做准确率评估自然会很高，这样的准确率并不代表决策树分类器的准确率
# 使用K折交叉验证。交叉验证是一种常用的验证分类准确率的方法，原理是拿出大部分样本进行训练，少量的用于分类器的验证。
# K折交叉验证，即做K次交叉验证，每次取K分之一的数据作为验证，其余作为训练。轮流K次，取平均值。
score_c = np.mean(cross_val_score(clf, train_features, train_labels, cv=10))
# 函数中cv代表对原始数据划分成多少份，也就是K值；一般K值取10.
print('10次交叉验证准确率 %.4f'%score_c)
'''
10次交叉验证准确率 0.7847
'''
# 多次运行发现score_t准确率保持在0.9820，而交叉验证准确率在0.78左右浮动。因此，对于不知道测试集实际结果的，要用K折交叉验证才能知道模型的准确率。

# 决策树可视化
'''
Graphviz可视化工具
1. 安装Graphviz工具
2. 将Graphviz添加到环境变量PATH中
3. pip install graphviz
'''
# 指定工作路径
os.chdir(r'D:\PY\graph文件')
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
# graph.render('titanic')                # 在工作路径生成tree.pdf文件
graph.view('titanic')                    # 在工作路径生成tree.pdf文件并打开