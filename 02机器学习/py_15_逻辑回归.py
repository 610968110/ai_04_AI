"""
逻辑回归:
逻辑回归是解决二分类问题的利器，能得出具体的概率值
比如癌症，良性概率65%，恶性概率34%，而且陆集回归都是用较小概率值的类别做为目标类别，所以这里我们求恶性的概率
公式: 逻辑回归公式.jpg
        输出：[0,1]区间的概率值，默认0.5作为阀值
        注：g(z)为sigmoid函数

优化：梯度下降

需要标准化处理
"""
"""
sklearn.linear_model.LogisticRegression(penalty=‘l2’, C = 1.0)

Logistic回归分类器
coef_：回归系数

"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def logistic():
    """
    逻辑回归做二分类进行癌症预测（根据细胞的属性特征）
    :return: NOne
    """
    # 构造列标签名字
    column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
              'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
              'Mitoses', 'Class']

    # 读取数据
    data = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        names=column)

    print(data)

    # 缺失值进行处理
    data = data.replace(to_replace='?', value=np.nan)

    data = data.dropna()

    # 进行数据的分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25)

    # 进行标准化处理
    std = StandardScaler()

    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 逻辑回归预测
    lg = LogisticRegression(C=1.0)

    lg.fit(x_train, y_train)

    print(lg.coef_)

    y_predict = lg.predict(x_test)

    print("准确率：", lg.score(x_test, y_test))
    # 2代表良性 4代表恶性
    print("召回率：", classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))

    return None


if __name__ == '__main__':
    logistic()
