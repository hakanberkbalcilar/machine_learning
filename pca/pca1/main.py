from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd


iris = load_iris()

data = iris.data
feature_names = iris.feature_names
y = iris.target


# We create our dataframe with data and data features_names that provided by sklearn.datasets
df = pd.DataFrame(data,columns = feature_names)
df["sinif"] = y #We define target to 'sinif' tag in our dataframe

x = data

pca = PCA(n_components = 2, whiten= True )  # whitten = normalize
pca.fit(x)

x_pca = pca.transform(x) #We apply dimensionality reduction for 'x' that provided from iris.target

print("variance ratio: ", pca.explained_variance_ratio_)

print("sum: ",sum(pca.explained_variance_ratio_))


df["p1"] = x_pca[:,0]
df["p2"] = x_pca[:,1]

color = ["black","brown","green"]# We define our colors

for each in range(3):
    plt.scatter(df.p1[df.sinif == each],df.p2[df.sinif == each],color = color[each],label = iris.target_names[each])
    
plt.legend()
plt.xlabel("p1")
plt.ylabel("p2")
plt.show()