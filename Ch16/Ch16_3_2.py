import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
print(kmeans.labels_)
print(y)

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["petal_length"], X["petal_width"],
            color=colmap[y])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Real Classification")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], 
            color=colmap[kmeans.labels_])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("K-means Classification")
plt.show()
