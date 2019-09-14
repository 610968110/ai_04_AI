from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import pandas as pd

"""
过滤式
通过删除低方差数据来减少特征数量
"""


def run():
    data = [
        [90, 2, 10, 40],
        [60, 4, 10, 45],
        [75, 3, 10, 46],
    ]
    #  过滤掉地方差的特征
    var = VarianceThreshold(threshold=0.0)  # 默认是删除方差为0的特征
    t = var.fit_transform(data)
    print(t)


"""
一般在特征值过多(100+)的时候需要进行主成分分析来减少特征值
主成分分析(PCA),将特征数据降维，比如二维降一维，一般保存90%~95%的数据
"""


def run1():
    data = [
        [2, 8, 4, 5],
        [6, 3, 0, 8],
        [5, 4, 9, 1],
    ]
    pca = PCA(n_components=0.93)
    t = pca.fit_transform(data)
    print(t)

    # -------------------------- PCA前可以先用交叉表处理下数据 --------------------------
    print("-" * 25, "PCA前可以先用交叉表处理下数据", "-" * 25)
    data = [
        {"uid": 0, "age": 18, "like": "egg"},
        {"uid": 1, "age": 18, "like": "egg"},
        {"uid": 2, "age": 18, "like": "tea"},
        {"uid": 3, "age": 18, "like": "apple"},
        {"uid": 4, "age": 18, "like": "water"},
        {"uid": 0, "age": 18, "like": "egg"},
    ]
    t = pd.DataFrame(data)
    # print(t)
    tt = pd.crosstab(t["uid"], t["like"])  # 交叉表
    print(tt)
    pac = PCA(n_components=0.90)
    ttt = pac.fit_transform(tt)
    print(ttt)


if __name__ == '__main__':
    run()
    run1()
