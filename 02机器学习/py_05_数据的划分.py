from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def run():
    li = load_iris()
    print("获取特征值")
    print(li.data)  # 二维数组
    print("获取目标值")
    print(li.target)  # 一维数组
    print("获取描述信息")
    print(li.DESCR)
    print("分隔数据，分割成训练集和测试集")
    # 返回值说明 xtrain:训练集特征值  xtest:训练集目标值  xtrain:测试集特征值  xtest:测试集目标值,测试时是真实的答案
    print(li.data)
    print(li.target)
    x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)


if __name__ == '__main__':
    run()
