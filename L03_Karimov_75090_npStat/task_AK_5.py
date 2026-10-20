import numpy as np
import pandas as pd

NAME = "Abduvoris"
SURNAME = "Karimov"
ID = "75090"

seed = int(ID[-3:])
digit2 = int(ID[1])
sumID = sum(int(d) for d in ID)

np.random.seed(seed)
x = np.random.randint(digit2, sumID, size=(13, 7))
U = x.flatten().tolist()

np.random.seed(seed)
weightX = np.random.random(len(U))
print('sum weightX= ', sum(weightX))
wmean_X = sum(weightX[i] * U[i] for i in range(len(weightX))) / sum(weightX)
print('wmean_X= ', wmean_X)

xx = np.array(U)
xs = pd.Series(U)
wX = np.array(weightX)

wmean_XX = np.average(xx, weights=wX)
print('wmean_XX (np.average, numpy array)= ', wmean_XX)

wmean_XX = np.average(xs, weights=wX)
print('wmean_XX (np.average, pandas series)= ', wmean_XX)

print('wmean_XX (dot functions)= ', (wX * xx).sum() / wX.sum())
