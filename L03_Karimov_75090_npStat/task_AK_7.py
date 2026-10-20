import statistics
import numpy as np
from scipy import stats

NAME = "Abduvoris"
SURNAME = "Karimov"
ID = "75090"

seed = int(ID[-3:])
digit2 = int(ID[1])
sumID = sum(int(d) for d in ID)

np.random.seed(seed)
x = np.random.randint(digit2, sumID, size=(13, 7))
U = x.flatten().tolist()

print("Mode statistics.mode:          ", statistics.mode(U))
print("Multimode statistics.multimode:", statistics.multimode(U))

m = stats.mode(U)
print("Mode scipy.stats.mode:         ", m.mode, "(count:", m.count, ")")
values, counts = np.unique(U, return_counts=True)
print("Multimode (scipy/numpy):       ", values[counts == counts.max()])
