# 팬시 인덱싱(Fancy indexing) : 1차원 배열 사용

import numpy as np

arr = np.arange(10,90,10)
#arr = np.array([10,20,30,40,50,60,70,80])
print(arr)

# 특정 인덱스들의 원소 선택
indices = [1,3,5,7]    # 또는 indices = np.array([1,3,5,7])
result = arr[indices]    # 새로운 1차원 배열 생성
print(result)    # [20 40 60 80]

# 임의의 순서를 지정해서 선택 가능
indices = [7,2,0,5]
result = arr[indices]
print(result)    # [80 30 10 60]
print(f'원본배열 : {arr}')    # {arr} - 원본 배열은 변경 없음