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
var_sample_hand = sum((xi - mean) ** 2 for xi in U) / (n - 1)
var_pop_hand = sum((xi - mean) ** 2 for xi in U) / n
print("Sample variance by hand:          ", var_sample_hand)
print("Population variance by hand:      ", var_pop_hand)

print("Sample variance statistics:       ", statistics.variance(U))
print("Population variance statistics:   ", statistics.pvariance(U))

print("Sample variance np.var(ddof=1):   ", np.var(U, ddof=1))
print("Population variance np.var:       ", np.var(U))

xs = pd.Series(U)
print("Sample variance Series.var():     ", xs.var())
print("Population variance var(ddof=0):  ", xs.var(ddof=0))
