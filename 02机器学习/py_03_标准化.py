from sklearn.preprocessing import StandardScaler, Imputer
import numpy as np


def run():
    data = [
        [90, 2, 10, 40],
        [60, 4, 15, 45],
        [75, 3, 13, 46],
    ]
    std = StandardScaler()
    t = std.fit_transform(data)
    print(t)  # 处理后我们发现每一列的均值为0，标准差为1
    print("原始数据中每列特征的平均值 -> ")
    print(std.mean_)
    print("原始数据每列特征的方差 -> ")
    print(std.var_)
    print(std.scale_)

    # -------------------------- 缺失值的处理 --------------------------
    print("-" * 25, "缺失值的处理", "-" * 25)
    data = [
        [90, 2, 10, 40],
        [60, 4, 15, 45],
        [75, np.nan, 13, 46]
    ]
    ip = Imputer(missing_values="NaN", strategy="mean", axis=0)  # 按列处理，填充平均数
    t = ip.fit_transform(data)
    print(t)


if __name__ == '__main__':
    run()
