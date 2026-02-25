# Numpy의 배열 생성 함수 1 ~ 3

import numpy as np

# zeros(shape, dtype=float, order=‘C’): 0으로 초기화된 배열 생성
a = np.zeros((3,4))    # (row, col) 형태 : 튜플 형태(괄호 안 들어가면 에러남)
print(a)

# ones(shape, dtype=None, order=‘C’): 1로 초기화된 배열 생성
a = np.ones(10)
print(a)

b = np.ones((2,3))    # 2행 3열
print(b)


print('\n')
# 단위 행렬(Identity matrix) 생성 - eye(N): N x N 크기의 단위 행렬 생성
a = np.eye(4)    # 4x4 크기의 단위 행렬
print(a)

# 대각행렬(Diagonal matrix): np.diag(v)
diag_values = [1,4,9]    # 1차원 배열 입력
D = np.diag(diag_values)
print('대각행렬')
print(D)

A =np.array([[1,2,3], [4,5,6], [7,8,9]])
print(A)
diagonal1 = np.diag(A)    # 대각선 요소만 추출
print(f'대각선 요소: {diagonal1}')


print('\n')
# arange(start, stop, step): a(rray) + range
import matplotlib.pyplot as plt

arr1 = np.arange(10)    # 0에서 9까지 step=1 , 이 방식을 제일 많이 씀
print(arr1)

arr2 = np.arange(0,10,0.5)    # 실수 step 가능
print(arr2)

plt.plot(arr2, arr2, marker='o', color='blue')
plt.show()