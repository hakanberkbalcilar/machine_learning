import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("decision_tree\data.csv")

data.drop(["id","Unnamed: 32"],axis=1,inplace=True)

M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]


plt.scatter(M.radius_mean,M.texture_mean,color="red",label="Bad",alpha= 0.5)
plt.scatter(B.radius_mean,B.texture_mean,color="blue",label="Good",alpha= 0.5)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()



data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"],axis=1)


# normalization (Why we use normalization?)
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data))


# train test split
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.15,random_state = 42)


from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)

print("Score: ", dt.score(x_test, y_test))

y_pred = dt.predict(x_test)  
y_pred

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)