
import pandas as pd

data = pd.read_csv('Birthweight.csv')

#task1
num1 = pd.Series(data["Length"])
subarray = num1[1:10:2]
index = ['a', 'b', 'c', 'd', 'e']
subarray = subarray.set_axis(index)
print(subarray)
print(num1.loc[1:4])
print(num1.iloc[1:4])

#task2
num2 = data
data["NewArray"] = data["Length"]/data["Birthweight"]
new_row = pd.DataFrame([{'Length': 55, 'Birthweight': 11, 'Headcirc': 33}])
num2 = pd.concat([num2, new_row])
num2 = num2.drop(33)
num2 = num2.drop(['Length'], axis=1)

print(num2)

#task3
data['Length'] = data['Length'].astype('float64')
index = data.set_index(['ID'])
group = data.groupby('Length').agg({'Birthweight': max, 'fheight': min, 'Headcirc': sum})

print(group[(group.Birthweight > 1.5) & (group.Birthweight < 3.5)])
print(index)
print(data.dtypes.value_counts(), data.describe())

#task4
frame1 = pd.DataFrame({
                       'MotherHeight': [156, 166, 174, 187],
                       'MotherWeight': [61, 66, 77, 88]})
frame2 = pd.DataFrame({'MotherHeight': [156, 166, 174, 167],
                       'MotherWeight': [55, 56, 54, 76]})

num4 = frame1.merge(frame2, on='MotherHeight')
print(num4)





