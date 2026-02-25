# 3차원 배열 인덱싱 및 슬라이싱

import numpy as np

arr3d = np.array([[[1,2,3],
                   [4,5,6]],
                   [[7,8,9],
                    [10,11,12]]])

print(arr3d)

# 첫 번째 면의 첫 번째 행, 열
print(f'arr3d[0,0,0] : {arr3d[0,0,0]}')

# 첫 번째 면의 첫 번째 행의 모든 열
print(f'arr3d[0,0,:] : \n {arr3d[0,0,:]}')

# 첫 번째 면의 두 번째 열의 모든 행
print(f'arr3d[0,:,1] : \n {arr3d[0,:,1]}')

# 두 번째 면의 모든 행과 모든 열
print(f'arr3d[1,:,:] : \n {arr3d[1,:,:]}')
print(f'arr3d[1,:] : \n {arr3d[1,:]}')

print('\n')
print('모든 차원의 0번째 행의 모든 열')
print(arr3d[:,0,:])

print('두 번째 차원의 0,1행의 0,1 컬럼')
print(arr3d[1,0:2,0:2])

print('모든 차원의 모든 행의 2번째 열')
print(arr3d[:,:,2])