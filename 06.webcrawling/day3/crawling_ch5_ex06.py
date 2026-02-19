# csv 파일에서 특정 컬럼만 text 파일로 저장하기

import pandas as pd
import csv
from tabulate import tabulate

def print_head(title_list, max):
    count = 1
    for title in title_list:
        print(f'[{count:3d}] {title}')
        if count >= max:
            break
        count += 1

def covert_dataframe_totext(in_file, out_file):
    '''
    csv 파일을 DataFrame으로 변환 후 특정 컬럼의 텍스트만 추출
    '''
    # csv에서 특정 컬럼만 읽기 : usecols = ['column1', 'column2']
    news_df = pd.read_csv(in_file, usecols=['title', 'description'],
                          encoding='utf-8-sig')
    # news_df는 ['title', 'description'] 형태
    title_list = news_df.values.tolist()
    new_title_list = []
    for title, desc in title_list:
        total_desc = str(title) + ' ' + str(desc)
        new_title_list.append(total_desc)

    print_head(new_title_list, 5)

    # text file로 문자열을 저장
    with open(out_file, 'w', encoding='utf-8') as file:
        for line in new_title_list:
            file.write(line+'\n')

def covert_csv_totext(in_file, out_file):
    '''
    csv 파일을 읽어서 [title], [description] 컬럼을 읽어서
    문자열만 텍스트 파일로 저장
    '''

    file_in = open(in_file, 'r', encoding='utf-8-sig')
    data = csv.reader(file_in, delimiter=',')
    header = next(data)
    print(header)

    # 저장할 파일 객체 생성
    file_out = open(out_file, 'w', encoding='utf-8-sig')
    title_list = []
    for row in data:
        line = row[2] + ' ' + row[3] + '\n'
        print(line)
        title_list.append(line)    # 리스트로 저장
        file_out.write(line)    # 파일로 저장
    file_out.close()
    file_in.close()
    print(f'title_list len: {len(title_list)}')

def main():
    in_file = '인공지능_naver_news.csv'
    out_file1 = 'news_output1.txt'
    out_file2 = 'news_output2.txt'
    covert_dataframe_totext(in_file, out_file1)
    #covert_dataframe_totext(in_file, out_file2)

main()