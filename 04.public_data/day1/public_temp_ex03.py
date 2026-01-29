# 대구 기온 데이터 수정 (utf-8-sig 및 ‘\t’ 제거)

import csv

# encoding='utf-8-sig'로 '\ufeff' 제거
# -sig : signature(서명)의 약자, 맨 처음에 이 파일이 어떤 인코딩으로 작성되었는지 알려주는 표식
fin = open('daegu.csv', 'r', encoding='utf-8-sig')
# 'utf-8-sig' : \ufeff 삭제
data=  csv.reader(fin, delimiter=',')

# newline='' : 한 라인씩 건너 뛰며 저장되는 현상 없앰
fout = open('daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig')
wr = csv.writer(fout)

for row in data:    # csv reader 객체를 이용해서 daegu.csv 파일을 한 라인씩 읽음
    for i in range(len(row)):
        row[i] = row[i].replace('\t', '')
    print(row)
    wr.writerow(row)    # 한 행씩 파일(daegu-utf8.csv)로 저장

fin.close()
fout.close()
print('파일 저장 완료')