# 파일에서 한 줄씩 읽기

infile=open('phones.txt', 'r', encoding='utf-8')
s=infile.readline()
print(s)

s=infile.readline()
print(s)

s=infile.readline()
print(s)

infile.close()