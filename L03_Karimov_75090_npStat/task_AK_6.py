import statistics
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

n = len(U)
s = sorted(U)
if n % 2:
    median_hand = s[n // 2]
else:
    median_hand = 0.5 * (s[n // 2 - 1] + s[n // 2])
print("Median by hand:          ", median_hand)

print("Median statistics.median:", statistics.median(U))
print("Median_low:              ", statistics.median_low(U))
print("Median_high:             ", statistics.median_high(U))

print("Median np.median:        ", np.median(U))

print("Median pd.Series.median: ", pd.Series(U).median())
