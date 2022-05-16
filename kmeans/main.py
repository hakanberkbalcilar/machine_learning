import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#We define random class

# class1
x1 = np.random.normal(25,5,300)
y1 = np.random.normal(25,5,300)

# class2
x2 = np.random.normal(55,5,300)
y2 = np.random.normal(60,5,300)

# class3
x3 = np.random.normal(55,5,300)
y3 = np.random.normal(15,5,300)

# We concatenate our 3 type of class to single variable; x and y
x = np.concatenate((x1,x2,x3),axis = 0)
y = np.concatenate((y1,y2,y3),axis = 0)


# We create a dictionary variable from and y
dictionary = {"x":x,"y":y}

#We create a dataframe from our dictionary variable
data = pd.DataFrame(dictionary)

#We show our first 3 type of class on the window so we can see what we see in the graphic before kmeans
plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)
plt.show()


wcss = []

for k in range(1,15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,15),wcss)
plt.xlabel("number of k (cluster) value")
plt.ylabel("wcss")
plt.show()



kmeans2 = KMeans(n_clusters=3)#We define kmeans object with number of cluster
clusters = kmeans2.fit_predict(data)

data["label"] = clusters

# We define each group configuration
plt.scatter(data.x[data.label == 0 ],data.y[data.label == 0],color = "red") 
plt.scatter(data.x[data.label == 1 ],data.y[data.label == 1],color = "green")
plt.scatter(data.x[data.label == 2 ],data.y[data.label == 2],color = "blue")

# We define our centroid configuration
plt.scatter(kmeans2.cluster_centers_[:,0],kmeans2.cluster_centers_[:,1],color = "yellow")
plt.show()