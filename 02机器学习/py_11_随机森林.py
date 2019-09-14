"""
集成学习方法——随机森林
随机森林可以解决决策树的过拟合(过于复杂的树),另外一种方式是剪枝
"""

"""
集成学习通过建立几个模型组合的来解决单一预测问题。它的工作原理是生成`多个分类器/模型`，各自独立地学习和作出预测。
这些预测最后结合成单预测，因此`优于任何一个单分类的做出预测`。
"""
"""
随机森林建⽴多个决策树的过程：
单个树建⽴过程：
N个样本， M个特征
1、随机在N个样本当中选择⼀个样本，以上重复N次,样本有可能重复
2、随机在M个特征当中选出m个特征 m取值
建⽴10颗决策树，样本，特征⼤多不⼀样 随机⼜放回的抽样 bootstrap
随机森林：n_estimator决策树的数量
max_depth:每颗树的深度限制
"""
"""
学习算法
根据下列算法而建造每棵树：
用N来表示训练用例（样本）的个数，M表示特征数目。
输入特征数目m，用于确定决策树上一个节点的决策结果；其中m应远小于M。
从N个训练用例（样本）中以有放回抽样的方式，取样N次，形成一个训练集（即bootstrap取样），并用未抽到的用例（样本）作预测，评估其误差。
"""
"""
API：
class sklearn.ensemble.RandomForestClassifier(n_estimators=10, criterion=’gini’,
 max_depth=None, bootstrap=True, random_state=None)
随机森林分类器
n_estimators：integer，optional（default = 10） 森林里的树木数量
criteria：string，可选（default =“gini”）分割特征的测量方法
max_depth：integer或None，可选（默认=无）树的最大深度 
bootstrap：boolean，optional（default = True）是否在构建树时使用放回抽样 
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from py_10_决策树 import run as get_data


def run():
    x_train, x_test, y_train, y_test = get_data()

    # 随机森林进行预测(超参数调优)
    rf = RandomForestClassifier()

    # 网格搜索与交叉验证
    params = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}
    gc = GridSearchCV(rf, param_grid=params, cv=2)
    gc.fit(x_train, y_train)

    print("预测的准确率为:", gc.score(x_test, y_test))
    print("查看选择的参数模型:", gc.best_params_)


if __name__ == '__main__':
    run()
