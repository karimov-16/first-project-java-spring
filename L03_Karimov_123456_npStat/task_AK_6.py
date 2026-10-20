import statistics
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

# 1. median "by hand"
n = len(U)
s = sorted(U)
if n % 2:
    median_hand = s[n // 2]
else:
    median_hand = 0.5 * (s[n // 2 - 1] + s[n // 2])
print("Median by hand:          ", median_hand)

# 2. statistics
print("Median statistics.median:", statistics.median(U))
print("Median_low:              ", statistics.median_low(U))
print("Median_high:             ", statistics.median_high(U))

# 3. numpy
print("Median np.median:        ", np.median(U))

# 4. pandas
print("Median pd.Series.median: ", pd.Series(U).median())
