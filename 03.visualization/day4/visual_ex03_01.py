# DataFrame 시각화 1 : 회사 평점 Bar 그래프 그리기

import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import koreanize_matplotlib

def draw_plot(df, title):
    df.plot(kind='bar', title=title)
    plt.xticks(rotation=0)
    #plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1.0))
    plt.tight_layout()
    plt.show()

def main():
    company_score_dict = {'삼성전자' : [3.8,4.2,3.1,3.5,3.5,3.1],
                          'LG전자' : [3.1,3.0,3.1,3.1,3.0,2.5],
                          'SK하이닉스' : [3.6,4.1,3.1,3.3,3.3,3.0],
                          '네이버' : [4.0,4.1,3.6,3.8,3.5,3.2]}
    columns=('전체평점','복지','업무와 삶의 균형','사내문화','승진 기회','경영진')
    company_score_df = pd.DataFrame.from_dict(company_score_dict, orient='index', columns=columns)
    print(tabulate(company_score_df, headers='keys', tablefmt='psql'))

    draw_plot(company_score_df, '회사별 전체 평점 분석')
main()