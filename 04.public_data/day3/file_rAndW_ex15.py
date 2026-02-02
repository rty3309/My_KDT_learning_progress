# csv 모듈 사용 예제 : csv.reader()

import csv

f=open('data.csv','r')
csv_reader = csv.reader(f)    # iterator 타입인 reader 객체를 리턴
for line in csv_reader:
    print(line)

    for i in range(len(line)):
        print(f'[{i}]:', line[i])
    print()
f.close()