# Numpy 배열 생성

import numpy as np

list1 = [0,1,2,3,4]
array1 = np.array(list1)    # list를 ndarray로 변경

print(f'{type(list1)}, list1: {list1}')
print(f'{type(array1)}, array1: {array1}')    # <class 'numpy.ndarray'>, array1: [0 1 2 3 4] 이 출력결과인데 [데이터] 사이에 쉼표가 없음

list2 = array1.tolist()    # ndarray를 list로 변경
print(f'{type(list2)} : {list2}')

# 배열의 속성
print(array1.ndim)    # 배열의 차원 수(1차원 배열)
print(array1.shape)    # 배열의 차원(m,n) 형식의 튜플
print(array1.size)    # 배열 원소의 개수
print(array1.dtype)    # 배열 원소의 자료형, int64 - 64bits 정수형
print(array1.itemsize)    # 각 원소의 바이트 크기(8: 64비트)
print(array1.data)    # 배열의 원소를 저장하고 있는 메모리 주소(전형적인 C언어 방법)