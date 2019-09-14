"""
线性回归需要标准化

线性模型:
f(x) = w1x1 + w2x2 + ... + wnxn + b
w:权重
x:特征
b:偏置项，可以理解为 w0*1

其中的误差称为损失函数

线性回归怎么求损失？   误差的平方求和(最小二乘法)
降低损失函数的方式？   正规方程和梯度下降，我们经常用`梯度下降`，其中有个超参数是`学习率`，代表下降的速率，根据`学习率`一点一点去试
            sklearn.linear_model.LinearRegression
            正规方程 普通最小二乘线性回归
            coef_：回归系数
            用于小规模数据，不能解决拟合以及其他问题

            sklearn.linear_model.SGDRegressor
            梯度下降  通过使用SGD最小化线性模型
            coef_：回归系数
            用于大规模数据
"""
"""
均方误差：
判断回归的误差。(分类用精确率和召回率)
mean_squared_error(y_true, y_pred)
均方误差回归损失
y_true:真实值
y_pred:预测值
return:浮点数结果
注：真实值，预测值为标准化之前的值

"""

from sklearn.datasets import load_boston
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def mylinear():
    """
    线性回归直接预测房子价格
    :return: None
    """
    # 获取数据
    lb = load_boston()

    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    print(y_train, y_test)

    # 进行标准化处理(?) 目标值处理？
    # 特征值和目标值是都必须进行标准化处理, 实例化两个标准化API
    std_x = StandardScaler()

    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()

    y_train = std_y.fit_transform(y_train)
    y_test = std_y.transform(y_test)

    # 预测房价结果
    model = joblib.load("./tmp/test.pkl")

    y_predict = std_y.inverse_transform(model.predict(x_test))

    print("保存的模型预测的结果：", y_predict)

    # estimator预测
    # 正规方程求解方式预测结果
    # lr = LinearRegression()
    #
    # lr.fit(x_train, y_train)
    #
    # print(lr.coef_)

    # 保存训练好的模型
    # joblib.dump(lr, "./tmp/test.pkl")

    # # 预测测试集的房子价格
    # y_lr_predict = std_y.inverse_transform(lr.predict(x_test))
    #
    # print("正规方程测试集里面每个房子的预测价格：", y_lr_predict)
    #
    # print("正规方程的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_lr_predict))
    #

    # # 梯度下降去进行房价预测
    # sgd = SGDRegressor()
    #
    # sgd.fit(x_train, y_train)
    #
    # print(sgd.coef_)
    #
    # # 预测测试集的房子价格
    # y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    #
    # print("梯度下降测试集里面每个房子的预测价格：", y_sgd_predict)
    #
    # print("梯度下降的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_sgd_predict))
    #

    # # 岭回归去进行房价预测
    # rd = Ridge(alpha=1.0)
    #
    # rd.fit(x_train, y_train)
    #
    # print(rd.coef_)
    #
    # # 预测测试集的房子价格
    # y_rd_predict = std_y.inverse_transform(rd.predict(x_test))
    #
    # print("梯度下降测试集里面每个房子的预测价格：", y_rd_predict)
    #
    # print("梯度下降的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_rd_predict))

    return None


if __name__ == '__main__':
    mylinear()
