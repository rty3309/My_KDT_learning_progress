# gender.csv 헤더 정보 출력

import csv

f=open('gender.csv',encoding='euc_kr')
data=csv.reader(f)
header=next(data)

for i in range(len(header)):
    print(f'[{i:3d}]: {header[i]}', end='')    # end='' 없는게 더 깔끔하게 출력되긴 함

    if (i+1) % 5 ==0:
        print()

f.close()