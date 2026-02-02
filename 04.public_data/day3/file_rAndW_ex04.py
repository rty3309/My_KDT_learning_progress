# 파일의 끝까지 한 줄씩 읽기

infile=open('phones.txt', 'r', encoding='utf-8')
line=infile.readline()

while line != '':    # EOF가 아닐 때까지 반복
    print(line, end='')
    line=infile.readline()
    # line != '' : 파일의 끝(End of File)을 empty string('')로 판단함
    #              아니면 읽고, 맞으면 while문 나감
infile.close()