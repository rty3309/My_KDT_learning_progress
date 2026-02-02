# Lab : csv 파일 읽기 Solution

f=open('data.csv','r')

for line in f.readlines():
    line = line.strip()    # 공백 문자를 없앰
    print(line)
    parts=line.split(',')    # 한 줄의 데이터를 쉼표로 분리

    # 각 줄의 필드를 출력
    for part in parts:
        print('   ', part)