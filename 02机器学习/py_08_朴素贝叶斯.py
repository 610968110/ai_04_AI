# 朴素贝叶斯 预测的是结果的概率，比如某商品是A的概率是80%，是B的概率是11%
# 适用于独立特征

from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report  # 分类报告

"""
概率
联合概率：概率为A并且概率为B的记作 P(A,B),P(A,B) = P(A)P(B)
条件概率：
       1个条件多个结果：在B的条件下，满足A1和A2的概率记作 P(A|B),P(A1,A2|B) = P(A1|B)P(A2|B),此条件成立的条件是A1A2相互独立
       多个条件1个结果：朴素贝叶斯，见README
       
精确率:查的准
召回率:查的全
"""


def run():
    news = fetch_20newsgroups(subset="all")
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test)

    mlt = MultinomialNB(alpha=1.0)  # 拉普拉斯平滑系数,用于防止概率为0的发生
    mlt.fit(x_train, y_train)
    y_predict = mlt.predict(x_test)  # 预测

    print("预测的文章类别为:", y_predict)
    print("准确率为", mlt.score(x_test, y_test))

    print("每个类别的精确率和召回率是:", classification_report(y_test, y_predict, target_names=news.target_names))


if __name__ == '__main__':
    run()
