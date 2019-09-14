from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba


def run():
    # -------------------------- 字典数据的抽取 --------------------------
    print("-" * 25, "字典数据的抽取", "-" * 25)
    data = [
        {"city": "北京", "temp": 40, "space": "10w"},
        {"city": "大连", "temp": 30, "space": "8w"},
        {"city": "铁岭", "temp": 10, "space": "5w"},
    ]
    my_dict = DictVectorizer(sparse=False)  # sparse = False，转化为sparse数组
    # 字典数据抽取:八字点钟的类别数据转化为特征    意思是用数字代替具体的文字，类似于之前学过的编译原理的算法
    t = my_dict.fit_transform(data)  #
    print(my_dict.get_feature_names())
    # 前面的二维数组0101那些 叫做 one-hot编码
    print(t)
    # print(my_dict.inverse_transform(t))  # 将数据还原

    # -------------------------- 文本特征的抽取 --------------------------
    print("-" * 25, "文本特征的抽取", "-" * 25)
    data = [
        "I like python and like js!",  # 单个字母不统计
        "Tom like kotlin!",
        "Bob dislike java!",
        "Bob like php!",
    ]
    cv = CountVectorizer()
    t = cv.fit_transform(data)
    print(cv.get_feature_names())
    print(t.toarray())
    # -------------------------- 中文分词jieba --------------------------
    print("-" * 25, "中文分词jieba", "-" * 25)

    data = [
        " ".join(jieba.cut("人生苦短，我用python")),  # 单个字母不统计
        " ".join(jieba.cut("人生漫长，不用python")),
    ]
    cv = CountVectorizer()
    t = cv.fit_transform(data)
    print(cv.get_feature_names())
    print(t.toarray())
    # -------------------------- tf idf 词语频率 逆文档频率 log(库中文档数量/包含该词的文档数) 相乘 --------------------
    print("-" * 25, "tf idf 词语频率 逆文档频率 log(库中文档数量/包含该词的文档数+1) 相乘 ", "-" * 25)
    data = [
        " ".join(jieba.cut("人生苦短，我用python")),  # 单个字母不统计
        " ".join(jieba.cut("人生漫长，不用python")),
    ]
    tf = TfidfVectorizer(stop_words=["忽略", "的词"])
    t = tf.fit_transform(data)
    print(tf.get_feature_names())
    print(t.toarray())


if __name__ == '__main__':
    run()
