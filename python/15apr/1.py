import numpy as np
hi = np.array([5, 6, 7, 8])
print("entered array", hi) 
print("Array with 2 added to each element:", hi + 2)
print("average", np.mean(hi))
print("reshaped array \n", hi.reshape(2,2))