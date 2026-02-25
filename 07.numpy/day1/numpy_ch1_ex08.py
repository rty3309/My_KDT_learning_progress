# 불리언 인덱싱(Boolean indexing) / 논리적 인덱싱

import numpy as np

arr = np.array([1,2,3,4,5,6])

# 조건에 맞는 원소만 선택
mask = arr > 3    # 조건  # [False False False True True True]
print(f'3보다 큰 원소 : {arr[mask]}')    # [4 5 6]

# 직접 조건 사용
even_numbers = arr[arr % 2 == 0]    # 조건
print(f'짝수 : {even_numbers}')    # [2 4 6]

# 2차원에서의 Bollean 인덱싱
arr2d = np.array([[1,2,3], [4,5,6]])
print(arr2d > 2)    # 조건식 출력

result = arr2d[arr2d > 2]    # 1차원 배열을 반환
print(f'2보다 큰 값 : {result}')    # [3 4 5 6]