# 파일을 읽어서 단어로 분리하기

infile = open('proverbs.txt','r')

for line in infile:
    line=line.rstrip()    # 오른쪽 '\n' 제거
    word_list=line.split()    # 공백기준으로 분리
    for word in word_list:
        print(word);

infile.close()