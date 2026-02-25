# 배열의 자료형 지정

import numpy as np

a = np.array([1,2,3], dtype=np.int32)    # 아래 부분과 출력 결과는 같음
b = np.array([4,5,6], dtype=np.int64)    # 이게 아래보다 더 일반적인 표기방식
print(a.dtype)
print(b.dtype)

print('\n')

a = np.array([1,2,3], dtype='int32')
b = np.array([4,5,6], dtype='int64')
print(a.dtype)
print(b.dtype)

print('\n')

arr1 = np.array([1.0, 2.0], dtype=np.float64)    # 64비트 실수
print(arr1.dtype)

arr2 = np.array([True, False], dtype=np.bool_)    # boolean 타입
print(arr2.dtype)

arr3 = np.array(['hello', 'world'], dtype='U5')    # 5글자 유니코드 문자열
print(arr3.dtype)    # < : 리틀 엔디언(little endian), > : 빅 엔디언(big endian)