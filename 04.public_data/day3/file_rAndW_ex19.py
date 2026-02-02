# 임의 접근 예제

infile=open('proverbs.txt','r+')
str=infile.read(10);    # 파일 포인터가 10바이트 이동
print('읽은 문자열:', str)
position = infile.tell();
print('현재 위치:', position)

position = infile.seek(0,0)    # 파일의 처음으로 이동
str = infile.read(10);
print('다시 읽은 문자열:', str)
infile.close()