# 파일에서 읽기 #1

infile=open('phones.txt', 'r', encoding='utf-8')    # euc-kr : 한글
s=infile.read(10)    # s: 파일에서 읽은 문자열 저장
print(s);
infile.close()