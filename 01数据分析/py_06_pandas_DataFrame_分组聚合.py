import pandas as pd
import numpy as np


def run():
    data = [
        {"name": "张三", "age": 18, "sex": "男"},
        {"name": "李四", "age": 19, "sex": "男"},
        {"name": "王五", "age": 20, "sex": "女"}
    ]
    t = pd.DataFrame(data)
    # -------------------------- 简单的求数量 --------------------------
    print("-" * 25, "简单的求数量", "-" * 25)
    count = t.groupby(by=["sex"]).count()
    print(count)

    count1 = t.groupby(by=t["sex"]).count()
    print(count1)

    print("男生的数量是%d个" % count.loc["男", "name"])
    count2 = t.groupby(by=[t["sex"], t["name"]]).count()
    print(count2)  # 这是复合索引，后面会将


if __name__ == '__main__':
    run()
