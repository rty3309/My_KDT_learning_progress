# age.csv 파일의 나이별 인덱스 확인하기

import csv

def get_index_of_age_csv():
    f=open('age.csv', encoding='euc-kr')
    data= csv.reader(f)
    header= next(data)

    print('--------------------------------------------')
    print(' age.csv index')
    print('--------------------------------------------')

    for i in range(len(header)):
        print(f'[{i:4}]: {header[i]}')
    f.close()

get_index_of_age_csv()