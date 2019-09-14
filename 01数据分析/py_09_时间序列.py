import pandas as pd


def run():
    # -------------------------- 生成时间范围段 --------------------------
    print("-" * 25, "生成时间范围段", "-" * 25)
    print(pd.date_range(start="20190101", end="20190103", freq="D"))
    print(pd.date_range(start="20130101", end="20190103", freq="2Y"))
    print(pd.date_range(start="20130101", periods=3, freq="2M"))
    # -------------------------- 时间转换成时间戳 --------------------------
    print("-" * 25, "时间转换成时间戳", "-" * 25)
    data = [
        {"name": "joe", "birthday": "20180101"},
        {"name": "peter", "birthday": "20170101"}
    ]
    t = pd.DataFrame(data)
    print(t)
    print("\n")
    t["birthday"] = pd.to_datetime(t["birthday"])
    print(t)
    print("\n")
    t.set_index("birthday", inplace=True)
    print(t)
    print("\n")
    count = t.resample("M").count()  # 重采样
    print(count)
    print("\n")
    _x = [i.strftime("%Y~%m~%d ") for i in count["name"].index]
    print(_x)
    # -------------------------- 时间类型 --------------------------
    print("-" * 25, "时间类型", "-" * 25)
    data1 = [
        {"name": "joe", "year": 2018, "month": 1, "day": 1},
        {"name": "peter", "year": 2017, "month": 1, "day": 1},
    ]
    t1 = pd.DataFrame(data1)
    print(t1)
    print("\n")
    t1["time"] = pd.PeriodIndex(year=t1["year"], month=t1["month"], day=t1["day"], freq="D")
    print(t1)


if __name__ == '__main__':
    run()
