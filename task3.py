import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from datetime import datetime

data = pd.read_csv('C:\\Users\\HP\\Downloads\\householdtask3.csv')

print(data.head(20))

#scatter plot with year against own
plt.scatter(data['year'],data['own'])

#adding tittleto the plot
plt.title("Scatter Plot")

#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#adding the legends
plt.show()

#line chart with year against own
plt.plot(data['year'])
plt.plot(data['own'])

#adding tittleto the plot
plt.title("Line Chart")

#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#adding the legends
plt.show()

#bar chart or bar plot
plt.bar(data['year'],data['own'])

#adding tittleto the plot
plt.title("Bar Chart or Bar Plot")

#setting the x and y labe
plt.xlabel('year')
plt.ylabel('own')

#adding the legends
plt.show()

#Histogram
plt.hist(data['income'])

#adding tittle to the plot
plt.title("Histogram")

plt.show()