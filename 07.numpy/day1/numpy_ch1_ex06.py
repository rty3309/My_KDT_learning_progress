# 1차원 배열 인덱싱

import numpy as np

arr1 = np.array([10,20,30,40,50])

# 양의 인덱스(0부터 시작)
print(f'첫 번째 원소 : {arr1[0]}')    # 10
print(f'세 번째 원소 : {arr1[2]}')    # 30

# 음의 인덱스(끝에서부터)
print(f'마지막 원소 : {arr1[-1]}')    # 50
print(f'끝에서 두 번째 : {arr1[-2]}')    # 40

# 인덱스 범위 : 0 ~ (길이-1)
print(f'배열 길이 : {len(arr1)}')    # 5