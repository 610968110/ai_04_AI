from matplotlib import pyplot as plt, font_manager

# windows、linux设置方法
#
# import matplotlib
# font = {
#     "weight": "bold",
#     "size": "14",
# }
# matplotlib.rc("font", **font)

# 用来显示中文，默认的字体不支持中文
fm = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc", size="large")


def run():
    x = range(2, 26, 2)
    y = [10, 43, 34, 57, 34, 76, 23, 12, 43, 34, 12, 55]
    plt.figure(figsize=(28, 8), dpi=80)
    # plt.plot(x, y, label="啦啦啦", color="pink", linestyle=":", linewidth="5")
    # plt.scatter(x, y)  # 散点图
    # plt.bar(x, y)  # 条形图  barh为横向
    plt.hist(x, 10)  # 直方图，组距

    # plt.xticks(x)
    # plt.xticks(range(2, 25))
    ticks = range(2, 25)
    plt.xticks(ticks, (" %d 点 " % i for i in ticks), rotation=45, fontproperties=fm)
    plt.yticks(range(min(y), max(y) + 1, 5))

    plt.grid(alpha=0.1)  # 增加网格
    plt.legend(prop=fm)  # 显示图例

    plt.title("测试啦", fontproperties=fm)
    plt.xlabel("时间", fontproperties=fm)
    plt.ylabel("温度", fontproperties=fm)

    plt.show()
    # plt.savefig("./img.png")  # 保存的是矢量图


if __name__ == '__main__':
    run()
