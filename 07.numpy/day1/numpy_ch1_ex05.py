# Numpy의 배열 생성 함수 4

import numpy as np
import matplotlib.pyplot as plt

# linspace(start, stop, n, endpoint=True): lin(early) space(d)
arr2 = np.linspace(10,20,6)    # end 포함함
print(arr2)    # (start, end, 구간개수)

arr3=  np.linspace(0,1,5)    # 0~1 사이의 값을 5구간으로 균등하게 생성
print(arr3)

plt.plot(arr3, arr3, 'o', color='tomato')
plt.show()