import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA


iris = datasets.load_iris()
X = iris.data[:, 1:3]  # I only get two feature that is between 1 and 3 indexes
y = iris.target

x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(10, 8))
plt.clf()

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="r")

plt.xlabel("Length Of Sepal")
plt.ylabel("Width Of Sepal")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())

fig = plt.figure(1, figsize=(15, 6)) #Window Size
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y,
    cmap=plt.cm.Set1,
    edgecolor="g", # Green Edge
    s=40,
)
ax.set_title("Where Is The Title?")
ax.set_xlabel("Axis X")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("Axis Y")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("Axis Z")
ax.w_zaxis.set_ticklabels([])

plt.show()