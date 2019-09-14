from sklearn.preprocessing import MinMaxScaler
import jieba

"""
归一化算法请看 README.md
"""


def run():
    """
    MinMaxScalar(feature_range=(0,1)…)
    每个特征缩放到给定范围(默认[0,1])
    改变这个参数相当于改变结果中的float范围

    """
    data = [
        [90, 2, 10, 40],
        [60, 4, 15, 45],
        [75, 3, 13, 46],
    ]
    ms = MinMaxScaler()
    t = ms.fit_transform(data)
    print(t)


if __name__ == '__main__':
    run()
