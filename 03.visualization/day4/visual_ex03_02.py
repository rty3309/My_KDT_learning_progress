# DataFrame 시각화 2: 사내 문화 정렬 및 bar 그래프 그리기

import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import koreanize_matplotlib

def print_dataframe(dataframe, title=''):
    print(title)
    print(tabulate(dataframe, headers='keys', tablefmt='psql'))
    # psql : PostgreSQL 데이터베이스와 상호작용하기 위한 오픈 소스 명령줄 도구
    print()

def draw_barchart(df, title):
    colors=['deepskyblue', 'lightcoral', 'darkorange', 'royalblue']

    sorted_df = df.sort_values(by=['사내문화'], ascending=False)
    #sorted_df = df.sort_values(by=df.columns[3], ascending=True)

    print_dataframe(sorted_df, '사내문화 내림차순')
    sorted_df['사내문화'].plot(kind='bar', title=title, color=colors)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()