import numpy as np

if __name__ == '__main__':
    a = np.arange(1, 28)
    print(type(a))
    a2 = a.reshape(3, 9)
    print(a2)
    print(a2 * 0)
    a3 = a.reshape(3, 3, 3)
    print(a3)
    # -------------------------- 切片 --------------------------
    print("-" * 25, "切片", "-" * 25)

    print(a2[0])  # 第一行
    print(a2[0, :])  # 第一行,列全取
    print(a2[0, :2])  # 第一行,列取前两个
    print(a2[[0, 2]])  # 第1、3行

    print(a2[:, 0])  # 第一列
    print(a2[:, [0, 1]])  # 第1、2列
    print(a2[1, [3]])  # 第二行第四列
    print(a2[0:3, 0:3])  # 第1-3行，第1-3列

    print(a2 < 10)
    a2[a2 < 10] = 100
    print(a2)

    print(np.where(a2 < 20, 0, 1))  # <20的替换为0，否则替换为1

    print(a2.clip(10, 18))  # <10的替换成10，>18的替换成18

    a2 = a2.astype("float")
    a2[0, 0] = np.nan
    print(a2)
    # -------------------------- 获取本地数据 --------------------------
    print("-" * 25, "获取本地数据", "-" * 25)
    load_txt = np.loadtxt("./test.txt", delimiter=",", dtype="int")
    print(load_txt)
    # -------------------------- 拼接数据 --------------------------
    print("-" * 25, "拼接数据", "-" * 25)
    print(np.vstack((load_txt, load_txt)))
    print(np.hstack((load_txt, load_txt)))
    # -------------------------- 数据换行 --------------------------
    print("-" * 25, "数据换行", "-" * 25)
    load_txt[[1, 2], :] = load_txt[[2, 1], :]  # 行交换，选中1、2行,然后换位置
    print(load_txt)
    load_txt = np.loadtxt("./test.txt", delimiter=",", dtype="int")
    load_txt[:, [1, 2]] = load_txt[:, [2, 1]]  # 列交换
    print(load_txt)
    # -------------------------- 初始化 --------------------------
    print("-" * 25, "初始化", "-" * 25)
    load_txt = np.loadtxt("./test.txt", delimiter=",", dtype="int")
    print(np.zeros(load_txt.shape).astype("int"))  # shape为元组，代表行列
    print(np.ones(load_txt.shape).astype("int"))  # shape为元组，代表行列
    print(np.eye(4))
    # -------------------------- 求最值 --------------------------
    print("-" * 25, "求最值", "-" * 25)
    print(np.argmax(load_txt))  # 最大值的index
    print(np.argmax(load_txt, axis=0))  # 每行最大值的index  axis=0代表行，axis=1代表列
    # -------------------------- 随机数 --------------------------
    print("-" * 25, "随机数", "-" * 25)
    randint = np.random.randint(0, 20, (5, 5))
    print(randint)
    # -------------------------- 不为0的个数 --------------------------
    print("-" * 25, "不为0的个数", "-" * 25)
    print(np.count_nonzero(randint))  # 不为0的个数
    # -------------------------- 不为nan的个数 --------------------------
    print("-" * 25, "不为nan的个数", "-" * 25)
    print(np.isnan(randint))  # 不为nan的个数
    print(np.count_nonzero(randint != randint))
    # -------------------------- 比较两个矩阵 --------------------------
    print("-" * 25, "比较两个矩阵", "-" * 25)
    print(randint != randint)
    # -------------------------- sum --------------------------
    print("-" * 25, "sum", "-" * 25)
    print(np.sum(load_txt, axis=0))  # 每行第index的值相加，  axis=0代表行，axis=1代表列,不指定全部加起来
    # -------------------------- 均值 --------------------------
    print("-" * 25, "均值", "-" * 25)
    print(load_txt.mean(axis=1, dtype='int'))
    print(np.median(load_txt, axis=1).astype("int"))  # 中值
    # -------------------------- 最大最小差值 --------------------------
    print("-" * 25, "最大最小差值", "-" * 25)
    print(load_txt.ptp(axis=0))
    # -------------------------- 标准差,离散程度 --------------------------
    print("-" * 25, "标准差,离散程度", "-" * 25)
    print(load_txt.std())
    # -------------------------- []中也可以传列表 --------------------------
    print("-" * 25, "[]中也可以传列表", "-" * 25)
    print(load_txt == load_txt)
    print(load_txt[load_txt == load_txt])
    # -------------------------- 降维 --------------------------
    print("-" * 25, "降维", "-" * 25)
    print(load_txt.flatten())
