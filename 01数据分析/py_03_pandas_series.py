import pandas


def run():
    print(pandas.Series([1, 2, 3, 4, 5]))
    print(pandas.Series([1, 2, 3, 4, 5], index=("a", "b", "c", "d", "e")))
    t = pandas.Series({"name": "小明", "age": 18, "sex": "男"})
    print(t)
    # -------------------------- 取值 --------------------------
    print("-" * 25, "取值", "-" * 25)
    print(t["name"])
    print(t[0])
    # -------------------------- 连续取值 --------------------------
    print("-" * 25, "连续取值", "-" * 25)
    print(t["name":"age"])
    print(t[0:2])
    # -------------------------- 非连续取值 --------------------------
    print("-" * 25, "非连续取值", "-" * 25)
    print(t[[0, 2]])  # 1 3行
    print(t[["name", "sex"]])
    # -------------------------- 读取本地数据 --------------------------
    print("-" * 25, "读取本地数据", "-" * 25)
    l = pandas.read_csv("./test1.txt")
    print(l)
    # 也可以从sql、excel、mongodb、json、html等读取


if __name__ == '__main__':
    run()
