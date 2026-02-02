# 파일을 읽고 공백 문자 제거

infile=open('phones.txt', 'r', encoding='utf-8')

for line in infile:
    line=line.rstrip()
    print(line)

infile.close()