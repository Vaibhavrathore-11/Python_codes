import numpy as np
arr = np.array([1,2,3,4,5,6,7,4,8,9,12,13,16,17,23,25])
print(arr)
arrays = np.array([2,3,4,5,6,7,8,12,13,17,18,23,24,25,201])
Q1 = np.percentile(arrays , 25)
print(Q1)
Q3 = np.percentile(arrays , 75)
print(Q3)

IQR = Q3 - Q1
print(IQR)

UF = Q3 + (1.5*IQR)
print(UF)

LF = Q1 - (1.5*IQR)
print(LF)
l = []
for i in arrays:
    if i >= LF and i<=UF:
        l.append(i)
arr2 = np.array(l)
print(arr2)
print(arrays)

import seaborn as sns
sns.boxploat(arr2)