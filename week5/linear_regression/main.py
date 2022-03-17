import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# We read csv file from currentdirectory and seperate csv files content from ";" operator
df = pd.read_csv("week5\linear_regression\linear_regression_dataset.csv", sep=";")

# Defines our graphic
plt.scatter(df.experience, df.salary)

# Sets label
plt.xlabel("Experience")
plt.ylabel("Salary")

# Shows graphic
plt.show()

# Create lreg object from LinearRegression class
lreg = LinearRegression()


# Defines x and y axis
x = df.experience.values.reshape(14,1)
y = df.salary.values.reshape(14,1)

# Fits x and y axis to linear model
lreg.fit(x,y)

# Predicts 15 years experienced worker salary
b0 = lreg.predict([[15]])
print(f"b0 = {b0}")

# Gets the value of interception on y-axis
b0_ = lreg.intercept_
print("b0_: ",b0_) # So 0 year experienced salary predicton is equal to interception of y-axis

# Gets Salary value per expreince year without start value
# THe start value is equal to iterception of y-axis
b1 = lreg.coef_
print("b1: ",b1)

# So we can predit salary of the exprience value manually like that
new_salary = 1663 + b1*11
print(new_salary)