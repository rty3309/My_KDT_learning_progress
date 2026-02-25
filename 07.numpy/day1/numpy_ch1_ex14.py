# Numpy 벡터화 연산

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)    # 동일한 인덱스끼리 덧셈
print(a+2)    # 배열의 각 원소에 2를 더함
print(a*2)    # 배열의 각 원소에 *2 (벡터화 연산)
print(a+10)    # 배열의 각 원소에 +10 (벡터화 연산)

list1 = [1,2,3]

print(list1 * 2)    # 리스트 원소 반복
print(list1 + 2)    # TypeError 발생