"""
过拟合：
一个假设在训练数据上能够获得比其他假设更好的拟合， 但是在训练数据外的数据集上却不能很好地拟合数据
，此时认为这个假设出现了过拟合的现象。(模型过于复杂)

原因：原始特征过多，存在一些嘈杂特征， 模型过于复杂是因为模型尝试去兼顾各个测试数据点
解决办法：
        进行特征选择，消除关联性大的特征(很难做)
        交叉验证(让所有数据都有过训练)
        正则化(了解)

带有正则化的线性回归-Ridge
sklearn.linear_model.Ridge
sklearn.linear_model.Ridge(alpha=1.0)
具有l2正则化的线性最小二乘法
alpha:正则化力度
coef_:回归系数

"""
"""
欠拟合：
一个假设在训练数据上不能获得更好的拟合， 但是在训练数据外的数据集上也不能很好地拟合数据，
此时认为这个假设出现了欠拟合的现象。(模型过于简单)

原因：学习到数据的特征过少
解决办法：增加数据的特征数量

"""