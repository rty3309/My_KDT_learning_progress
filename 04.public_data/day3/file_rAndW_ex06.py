# 파일 문자 단위로 읽기

infile=open('input.txt','r', encoding='utf-8')
ch=' '
while ch != '':
    ch = infile.read(1)
    print(ch, end='')

infile.close()