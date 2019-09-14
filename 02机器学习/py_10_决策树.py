"""
信息熵，单位为比特:
H = -(p1logp1 + p2logp2 + ... + p32log32)
公式i：mg/001.jpg

信息增益:
当得知一个特征条件之后，减少的信息熵的大小
信息增益表示得知特征X的信息而使得类Y的信息的不确定性减少的程度
特征A对训练数据集D的信息增益g(D,A),定义为集合D的信息熵H(D)与特征A给定条件下D的信息条件熵H(D|A)之差，即公式为：
g(D,A) = H(D) - H(D`|A)
   g(D,A)：信息增益
   H(D`):初始信息熵大小


基尼系数：比信息增益更加细致，sklearn默认就是用的基尼系数
"""

"""
class sklearn.tree.DecisionTreeClassifier(criterion=’gini’, max_depth=None,random_state=None)
决策树分类器
criterion:默认是’gini’系数，也可以选择信息增益的熵’entropy’
max_depth:树的深度大小
random_state:随机数种子

method:
decision_path:返回决策树的路径
"""
"""
决策树的结构和本地保存
1、sklearn.tree.export_graphviz() 该函数能够导出DOT格式
tree.export_graphviz(estimator,out_file='tree.dot’,feature_names=[‘’,’’])

2、工具:(能够将dot文件转换为pdf、png)
安装graphviz
ubuntu:sudo apt-get install graphviz                    Mac:brew install graphviz

3、运行命令
然后我们运行这个命令
$ dot -Tpng tree.dot -o tree.png

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from pandas import DataFrame
from sklearn.tree import DecisionTreeClassifier


def run():
    # data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    data = pd.read_csv("./data/泰坦尼克号.txt")

    # 取出对存货有关系的特征,得到特征值和目标值
    x: DataFrame = data[["age", "pclass", "sex"]]
    y = data[["survived"]]

    # 填充年龄的缺失值
    x["age"].fillna(x["age"].mean(), inplace=True)  # inplace会在原有的数组上进行修改

    # 特征工程处理,不是纯数字,先进行one-hot编码
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)  # 先进行数据划分，因为对于我们来说我们不知道测试集
    d = DictVectorizer(sparse=False)
    # format -> [{'age': 2.0, 'pclass': '2nd', 'sex': 'female'}, {'age': 8.0, 'pclass': '2nd', 'sex': 'male'}, ...]
    x_train_dict = x_train.to_dict(orient="records")  # 转化成字典，固定写法
    x_train = d.fit_transform(x_train_dict)
    x_test_dict = x_test.to_dict(orient="records")
    x_test = d.transform(x_test_dict)

    # print(d.get_feature_names())
    # print(x_train)

    # 用决策树进行预测
    dec = DecisionTreeClassifier(max_depth=5)  # max_depth控制树的深度
    dec.fit(x_train, y_train)

    print("预测的准确率为:", dec.score(x_test, y_test))

    return x_train, x_test, y_train, y_test


if __name__ == '__main__':
    run()
