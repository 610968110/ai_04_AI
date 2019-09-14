import numpy   as np
import pandas


def run():
    """
    join对行索引进行操作，也就是上边的索引
    merge对列索引进行操作，也就是左边的索引
    :return: null
    """
    # -------------------------- join合并 --------------------------
    print("-" * 25, "join合并", "-" * 25)
    a1 = pandas.DataFrame(np.zeros((3, 3)), columns=list("abc"), index=list("ABC"))
    print(a1)
    a2 = pandas.DataFrame(np.ones((2, 3)), columns=list("xyz"), index=list("AB"))
    print(a2)

    print(a1.join(a2))
    print(a2.join(a1))
    # -------------------------- merge合并 并集 内连接 --------------------------
    print("-" * 25, "merge合并 并集 内连接", "-" * 25)
    a1 = pandas.DataFrame(np.zeros((3, 3)), columns=list("abc"), index=list("ABC"))
    print(a1)
    a2 = pandas.DataFrame(np.ones((2, 3)), columns=list("axy"), index=list("AB"))
    print(a2)

    print(a1.merge(a2, on="a"))  # 默认并集
    # -------------------------- merge合并 并集1 内连接1--------------------------
    print("-" * 25, "merge合并 并集1 内连接1", "-" * 25)
    a1 = pandas.DataFrame(np.arange(0, 9).reshape((3, 3)), columns=list("abc"), index=list("ABC"))
    print(a1)
    a2 = pandas.DataFrame(np.zeros((2, 3)).astype("int"), columns=list("axy"), index=list("AB"))
    print(a2)

    print(a1.merge(a2, on="a"))
    # -------------------------- merge合并 交集Nan补全 外链接 --------------------------
    print("-" * 25, "merge合并 交集Nan补全 外链接", "-" * 25)
    a1 = pandas.DataFrame(np.arange(0, 9).reshape((3, 3)), columns=list("abc"), index=list("ABC"))
    print(a1)
    a2 = pandas.DataFrame(np.ones((2, 3)).astype("int"), columns=list("axy"), index=list("AB"))
    print(a2)

    print(a1.merge(a2, on="a", how="outer"))  # 行数列数相加，列数两个a合并成一列，所以一共5行5列
    print(a2.merge(a1, on="a", how="outer"))  # 相当于两个数组上下拼接起来，用Nan补全
    # -------------------------- merge left 以左边为准 --------------------------
    print("-" * 25, "merge left 以左边为准", "-" * 25)
    a1 = pandas.DataFrame(np.arange(0, 9).reshape((3, 3)), columns=list("abc"), index=list("ABC"))
    print(a1)
    a2 = pandas.DataFrame(np.ones((2, 3)).astype("int"), columns=list("axy"), index=list("AB"))
    print(a2)

    print(a1.merge(a2, on="a", how="left"))
    print(a2.merge(a1, on="a", how="left"))
    # -------------------------- merge right 以右边为准 --------------------------
    print("-" * 25, "merge right 以右边为准", "-" * 25)
    a1 = pandas.DataFrame(np.arange(0, 9).reshape((3, 3)), columns=list("abc"), index=list("ABC"))
    print(a1)
    a2 = pandas.DataFrame(np.ones((2, 3)).astype("int"), columns=list("axy"), index=list("AB"))
    print(a2)

    print(a1.merge(a2, on="a", how="right"))
    print(a2.merge(a1, on="a", how="right"))


if __name__ == '__main__':
    run()
