# 0차원 배열(스칼라)

import numpy as np

# 0차원 배열 : 원소 1개만 가지는 0차원 배열
a = np.array(1)    # 하난의 원소만 가진 0차원 배열(스칼라 배열)

print(a)
print(type(a))
print(a.shape)
print(a.ndim)

# 브로드캐스팅
b = np.array([1,2,3])
a = np.array(7)
print(a+b)