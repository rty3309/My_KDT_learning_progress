# Text Editors 테이블 크롤링 : Pandas 사용

from urllib.request import urlopen, Request
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Comparison_of_text_editors'
urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(urlrequest)

# df.droplevel(level=0) 대신에 header=인덱스 사용
# 해당 url에 2개의 테이블 존재 : match는 첫 번째 테이블 구분 용도
editor_table = pd.read_html(html, match='Developer', header=1)    # match='Developer'는 table 내부의 컬럼 이름
# ㄴ리스트 내부에 DataFrame 포함

table_df = pd.DataFrame(data=editor_table[0])
print(table_df.columns)
print('-'*80)
print(table_df.head())

# 불필요한 column 제거(drop)
table_df = table_df.drop(['GUI', 'TUI or CLI'], axis=1)

# table_df를 csv 파일로 저장
table_df.to_csv('text_editors.csv', mode='w', encoding='utf-8')
print('text_editors.csv 파일 저장 완료')