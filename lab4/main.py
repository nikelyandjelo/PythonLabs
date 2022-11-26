import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

data = pd.read_csv("bike.csv")

#task1
sns.countplot(data=data, x="Occupation")
plt.title('Кількість покупців різних професій')
plt.xlabel('Occupation')
plt.ylabel('Number of People')
plt.show()

sns.barplot(data=data, x="Occupation", y="Income", estimator = np.median)
plt.title('Медіанний дохід покупців різних професій')
plt.xlabel('Occupation')
plt.ylabel('Income')
plt.show()

sns.barplot(data=data, x="Occupation", y="Age", hue = "Purchased Bike")
plt.title('Середній вік покупців різних професій')
plt.xlabel('Occupation')
plt.ylabel('Age')
plt.show()

#task2
sns.histplot(data=data, x="Children", binwidth=1)
plt.title('Кількість дітей')
plt.xlabel('Children age')
plt.ylabel('Number of children')
plt.show()

sns.histplot(data=data, x="Children", hue = "Purchased Bike", binwidth=1)
plt.title('Кількість дітей в залежності від покупки велосипеду')
plt.xlabel('Children age')
plt.ylabel('Number of children')
plt.show()

#task3
sns.boxplot(data=data, x="Income")
plt.title('Розмах доходу')
plt.show()

sns.boxplot(data=data, x="Income", y="Education")
plt.title('Розмах доходу в залежності від рівня освіти')
plt.xlabel('Income')
plt.show()

#task4
corr1 = stats.pearsonr(data["Income"], data["Age"])
print("Коефіцієнт кореляції для доходу і віку\n", corr1)
sns.scatterplot(data=data, x="Income", y="Age")
plt.title('Залежність між доходом і віком')
plt.xlabel('Income')
plt.ylabel('Age')
plt.show()

corr2 = stats.pearsonr(data["Children"], data["Cars"])
print("Коефіцієнт кореляції для кількості дітей та машин\n", corr2)
sns.scatterplot(data=data, x="Children", y="Cars")
plt.title('Залежність між кількістю дітей і машин')
plt.xlabel('Number of Children')
plt.ylabel('Cars')
plt.show()