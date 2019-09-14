"""

"""
"""
转换器就是之前用到的那些，注意fit/transform/fit_transform的区别
"""
"""
估计器是实现了算法的API，比如k-近邻算法、贝叶斯、决策树与随机森林等
步骤:
1、调用fit(x_train, y_train)建立模型
2、输入预测数据，将测试集的特征值传进去，得到测试集的目标值 y_test = predict(x_test)
3、预测的准确率, score(x_test, y_test)
"""
