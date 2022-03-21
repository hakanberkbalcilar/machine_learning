import numpy as np
import pandas as pd


# Create 2 Dimensional array for data
my_data = np.array([[0, 3], [10, 7], [20, 9], [34, 5], [30, 14], [40, 15]])

# Create columns for my_data array's second dimension that has arrays with 2 items so we create two columns
my_column_names = ['temperature', 'activity']

# Now we combine data and columns so we can visualize our data to make more readable
my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)

print(my_dataframe)

# We add new column named adjusted and we add activity all activity data to this column after 3 multiplication
my_dataframe["adjusted"] = my_dataframe["activity"] * 3

print(my_dataframe)


# We get first 4 rows which are 0,1,2,3 indexed rows
print("\nFirst 4 Row: ")
print(my_dataframe.head(4))

# We get a specific row which is 4 indexed row
print("\nFourth Row: ")
print(my_dataframe.iloc[[4]])

# We get rows between given indexes which is between 2 an 5 for now
print("\nRow Between Indexes: ")
print(my_dataframe[2:5])

# We get whole column
print("\nTemperature Column:")
print(my_dataframe["temperature"])


#Task
tags = ['Eleanor', 'Chidi', 'Tahani', 'Jason'] # We Create a list of given column names

randomData = np.random.randint(low=0, high=101, size=(3, 4)) # We create a list from random values which has 3x4 dimension


dataFrame = pd.DataFrame(data=randomData, columns=tags) # We define our dataframe

print(dataFrame)

print("\nSecond row of the Eleanor column: %d\n" % dataFrame['Eleanor'][1])

dataFrame['Janet'] = dataFrame['Tahani'] + dataFrame['Jason']

print(dataFrame)