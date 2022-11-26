import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('Birthweight.csv')

length = np.array(data['Length']) #task1
mnocig = np.array(data['mnocig']) #task2
motherage = np.array(data['mage35']) #task3

gestation = np.array(data['Gestation'])
mppwt = np.array(data['mppwt'])
pirson = stats.pearsonr(gestation, mppwt)


def normal(array):
    check = stats.normaltest(array)
    if check[1] > 0.05:
        return 'Розподілено нормально'
    else:
        return 'Розподілено не нормально'


def child(arr1, arr2):
    moth = stats.ttest_ind(arr1, arr2, alternative="less")
    if moth[1] > 0.05:
        return 'Не можна відхилити основну гіпотезу: У матерів старше 35 діти мають таку саму вагу, що й у матерів молодше 35'
    else:
        return 'Відхиляємо основну гіпотезу: У матерів старше 35 діти легше'


motherOlder35 = data.loc[data["mage35"] == 1]
motherYounger35 = data.loc[data["mage35"] == 0]
motherOlder35Weight = motherOlder35["Birthweight"]
motherYounger35Weight = motherYounger35["Birthweight"]

print('Середній зріст дітей', np.mean(length)) #task1
print('Медіана', np.median(length)) #task1
print(normal(mnocig)) #task2
print(child(motherOlder35Weight, motherYounger35Weight))#task3
print('Коефіцієнт кореляції Пірсона становить',  pirson[0])
