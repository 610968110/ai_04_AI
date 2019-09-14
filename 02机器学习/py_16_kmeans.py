"""
聚类k-means.jpg

做在分类之前(没有目标值的时候用聚类)

sklearn.cluster.KMeans(n_clusters=8,init=‘k-means++’)
k-means聚类
n_clusters:开始的聚类中心数量
init:初始化方法，默认为'k-means ++’

labels_:默认标记的类型，可以和真实值比较（不是值比较）

"""
"""
轮廓系数：
Kmeans性能评估指标
对于每一个样本都有一个轮廓系数

公式：轮廓系数.png


sklearn.metrics.silhouette_score(X, labels)
计算所有样本的平均轮廓系数
X：特征值
labels：被聚类标记的目标值


"""

"""
代码见 instacart.ipynb
"""