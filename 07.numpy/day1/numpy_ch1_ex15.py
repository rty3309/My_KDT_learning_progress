# Numpy 배열 연산

import numpy as np

a = np.array([1,2,3], dtype=np.int32)
b = np.array([4,5,6], dtype=np.int64)

c = a + b
print(c)
print(c.dtype)