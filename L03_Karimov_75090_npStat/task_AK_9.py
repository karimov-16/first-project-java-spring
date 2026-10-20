import math
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
mean = sum(U) / n
std_sample_hand = math.sqrt(sum((xi - mean) ** 2 for xi in U) / (n - 1))
std_pop_hand = math.sqrt(sum((xi - mean) ** 2 for xi in U) / n)
print("Sample std by hand:          ", std_sample_hand)
print("Population std by hand:      ", std_pop_hand)

print("Sample std statistics:       ", statistics.stdev(U))
print("Population std statistics:   ", statistics.pstdev(U))

print("Sample std np.std(ddof=1):   ", np.std(U, ddof=1))
print("Population std np.std:       ", np.std(U))

xs = pd.Series(U)
print("Sample std Series.std():     ", xs.std())
print("Population std std(ddof=0):  ", xs.std(ddof=0))
