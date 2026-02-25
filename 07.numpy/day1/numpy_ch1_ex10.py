# 팬시 인덱싱(Fancy indexing) : 2차원 배열 사용

import numpy as np

arr2d = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])

# 특정 행들 선택 : [0행, 2행]
row_indices = [0,2]
result = arr2d[row_indices]  
print(result)
print('-'*20)

# 행과 열을 동시에 지정 : [0,1], [1,2], [2,3]
row_indices = [0,1,2]
col_indicies = [1,2,3]
result = arr2d[row_indices, col_indicies]
print(result)    # (0,1), (1,2), (2,3) 위치의 원소들
print('-'*20)

# 0, 2행과 1, 3열을 교차 인덱싱(격자 선택)
result = arr2d[np.ix_([0,2], [1,3])]    # [0,2] : 행 인덱스, [1,3] : 컬럼 인덱슨
print(result)