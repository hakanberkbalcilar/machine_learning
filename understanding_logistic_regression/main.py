import pandas as pd
from sklearn.model_selection import train_test_split

# We define our columns that provided in the csv file
columns = ["Pregnancies","Glucose","Blood Pressure","Skin Thickness","Insulin","BMI","Pedigree","Age", "Outcome"]

# We read our csv file and create dataset
pimaDataset = pd.read_csv("understanding_logistic_regression\diabetes.csv", header= None, names=columns)

# We show our dataset with our configs
print(pimaDataset.head())

# we define our feature columns
featureColumns = ["Pregnancies","Insulin","BMI","Age","Glucose","Pedigree","Blood Pressure"]

# We get featureColumns feature from pimaDataset
X = pimaDataset[featureColumns]
Y = pimaDataset.Outcome # We get our column that named as "Outcome"

X_train, X_test, Y_train, Y_Test = train_test_split(X, Y, test_size = .25, random_state = 0)

print(X.head())