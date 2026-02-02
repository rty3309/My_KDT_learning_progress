# 파일 전체 읽기

# read()함수 - 권장 방법은 아님
infile = open('phones.txt','r', encoding='utf-8')
s=infile.read()
print(s)
infile.close()

print('\n')

# readlines()함수 - 각 라인이 저장된 리스트를 반환
infile = open('phones.txt','r', encoding='utf-8')
lines=infile.readlines()
print(lines)
for line in lines:
    print(line)
infile.close()