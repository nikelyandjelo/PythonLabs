import random
import numpy as np
import pandas as pd

data = pd.read_csv('iris.csv')
petal_width = np.array(data['petal_width'])

array = np.array([[random.randint(2, 10) for i in range(7)] for e in range(5)])
orange = np.arange(2, 17, 3)
ones = np.ones((5, 7))
zeros = np.zeros((5, 7))
lspace = np.linspace(2, 4, 5)
randomArr = np.random.random((5, 7))
randintArr = np.random.randint(20, 40, (5, 7))
empty = np.empty(7)

print('Arrange:', '\n', orange,
      '\nRandom array(cycle):', '\n', array,
      '\nOnes array:', '\n', ones,
      '\nZeros array:', '\n', zeros,
      '\nLinspace array:', '\n', lspace,
      '\nRandom Array:', '\n', randomArr,
      '\nRandint array:', '\n', randintArr,
      '\nEmpty array:', '\n', empty)

print('Звернення до елементу масиву за індексом: ', randintArr[3][2],
      '\nЗвернення до елементу масиву за відємним індексом: ', randintArr[-2][-1])
print('Виділення одновимірного підмасиву: ', orange[1: 7: 2],
      '\nВиділення багатовимірного підмасиву: ', array[1: 5: 2, 1: 4: 1])

print('Додавання:', '\n', np.add(array, randintArr),
      '\nВіднімання:', '\n', np.subtract(array, randintArr),
      '\nМноження:', '\n', np.multiply(array, randintArr),
      '\nДілення:', '\n', np.divide(array, randintArr),
      '\nПіднесення до ступеня:', '\n', np.power(array, 2),
      '\nДілення за модулем:', '\n', np.mod(array, randintArr),
      '\nЗміна знаку на протилежний:', '\n', np.negative(array))
print('Reduce:',  np.subtract.reduce(array),
      '\nAccumulate:', np.subtract.accumulate(array),
      '\nOuter:', np.outer(array, ones))
print('Мінімальне значення:', np.min(petal_width),
      '\nМаксимальне значення:', np.max(petal_width),
      '\nВибіркове середнє:', np.mean(petal_width),
      '\nДисперсія:', np.var(petal_width),
      '\nСереднєквадратичне відхилення:', np.std(petal_width),
      '\nМедіана: ', np.median(petal_width),
      '\nПерсинтил 25:', np.percentile(petal_width, 25),
      '\nПерсинтил 75:', np.percentile(petal_width, 75))

