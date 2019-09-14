import pandas as pd
import numpy as np


def run():
    data = [
        {"name": "张三", "age": 18, "sex": "男"},
        {"name": "李四", "age": 19, "sex": "男"},
        {"name": "王五", "age": 20, "sex": "女"}
    ]
    t = pd.DataFrame(data)
    print(t)
    # -------------------------- 索引 --------------------------
    print("-" * 25, "索引", "-" * 25)
    g = t.groupby(by="sex").count()
    print(g)
    # print(g.index)
    g.index = ["girl", "boy"]
    # print(g.index)
    print(g)
    # -------------------------- reindex 起到过滤作用 --------------------------
    print("-" * 25, "reindex 起到过滤作用", "-" * 25)
    print(g)
    print(g.reindex(["boy", "unknown"]))
    # -------------------------- set_index 将列作为索引--------------------------
    print("-" * 25, "set_index 将列作为索引", "-" * 25)
    print(g)
    print(g.set_index("age", drop=False))  # drop默认为True，True时，age列变为索引后会删除掉age列
    print(g.set_index(["age", "name"], drop=False))  # drop默认为True，True时，age列变为索引后会删除掉age列
    # -------------------------- 对上述多重索引进行取值 --------------------------
    print("-" * 25, "对上述多重索引进行取值", "-" * 25)
    values = t.set_index("age")
    print(values)
    print(values["name"])  # 先声明去name列
    print(values["name"][18])  # 先声明去name列，然后取age中的18
    # -------------------------- 对上述多重索引进行取值2 --------------------------
    print("-" * 25, "对上述多重索引进行取值2", "-" * 25)
    data1 = [
        {"name": "张三", "age": 18, "sex": "男"},
        {"name": "李四", "age": 18, "sex": "男"},
        {"name": "王五", "age": 20, "sex": "女"}
    ]
    t1 = pd.DataFrame(data1)
    values = t1.set_index(["age", "sex"])
    print(values)
    print(values["name"][20]["女"])
    print(values.loc[20].loc["女"]["name"])
    # -------------------------- swaplevel换位置 --------------------------
    print("-" * 25, "swaplevel换位置", "-" * 25)
    values = t1.set_index(["name", "age"])
    print(values)
    print(values.swaplevel())


if __name__ == '__main__':
    run()
