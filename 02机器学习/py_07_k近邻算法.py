#  KNN

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""
需要做标准化处理

距离的计算公式，又叫欧氏距离:
比如2个样本的3个特征 a(a1, a2, a3) b(b1, b2, b3)
√( (a1-b1)^2 + (a2-b2)^2 + (a3-b3)^2 )
最小即为最近值
"""


def run():
    d = [
        {"x": 2, "y": -2, "time": 470702, "sign": 100, "place_id": 1},
        {"x": 4, "y": -4, "time": 456789, "sign": 10, "place_id": 2},
        {"x": 5, "y": -5, "time": 123865, "sign": 200, "place_id": 3},
        {"x": 8, "y": -8, "time": 876436, "sign": 300, "place_id": 4},
        {"x": 10, "y": -10, "time": 2586908, "sign": 400, "place_id": 5},
        {"x": 12, "y": -12, "time": 234567, "sign": 500, "place_id": 6},
    ]
    # data = pd.read_csv("./data/train.csv")
    data = pd.DataFrame(d)
    #  过滤一些数据  start
    data = data.query("x <= 10 & y <= 10")
    #  处理时间  毫秒转换成秒  字典格式
    time_values = pd.to_datetime(data["time"], unit="s")
    # data.loc[:, "date"] = time_values
    data["day"] = pd.DatetimeIndex(time_values).day  # 存day
    data = data.drop(["time"], axis=1)  # 删除time  pd里面1是列
    # print(data)
    place_id_count = data.groupby(by="place_id").count()  # place_id变成了行索引  就是竖排的
    print(place_id_count)
    sc = place_id_count[place_id_count.sign > 0]  # 把sign <= 0 的去掉,没人签到就不统计了，当然0为任意值
    sc = sc.reset_index()  # 把sign从行索引变成特征
    # print(sc)
    print("\n")
    data = data[data["place_id"].isin(sc.place_id)]
    print(data)
    print("\n")
    #  过滤一些数据  end

    # 分隔训练集和测试集
    x = data.drop(["place_id"], axis=1)
    y = data["place_id"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程 标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 进行算法流程
    knn = KNeighborsClassifier(n_neighbors=2)  # 取2个最近的欧氏距离
    knn.fit(x_train, y_train)

    # 得出预测结果 这里建议用交叉验证和网格搜索
    y_predict = knn.predict(x_test)
    print("预目标的位置为:", y_predict)
    print("准确率:", knn.score(x_test, y_test))


if __name__ == '__main__':
    run()
