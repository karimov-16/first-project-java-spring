import numpy as np
import pandas as pd

# ====== YOUR DATA (change only these lines) ======
NAME = "Abu"
SURNAME = "Karimov"
ID = "123456"            # your student ID
# ==================================================

seed = int(ID[-3:])                  # as in task 2
digit2 = int(ID[1])                  # second digit of ID
sumID = sum(int(d) for d in ID)      # sum of digits of ID

np.random.seed(seed)
x = np.random.randint(digit2, sumID, size=(13, 7))   # [digit2, sumID)
U = x.flatten().tolist()             # 1-D data (Python list) used for statistics

# weighted average
np.random.seed(seed)
weightX = np.random.random(len(U))   # uniform on [0, 1), same size as x
print('sum weightX= ', sum(weightX))
wmean_X = sum(weightX[i] * U[i] for i in range(len(weightX))) / sum(weightX)  # normalization
print('wmean_X= ', wmean_X)

# For large data set it is better to use NumPy or pandas
xx = np.array(U)
xs = pd.Series(U)
wX = np.array(weightX)

wmean_XX = np.average(xx, weights=wX)
print('wmean_XX (np.average, numpy array)= ', wmean_XX)

wmean_XX = np.average(xs, weights=wX)
print('wmean_XX (np.average, pandas series)= ', wmean_XX)

# with the use of dot.function()
print('wmean_XX (dot functions)= ', (wX * xx).sum() / wX.sum())
