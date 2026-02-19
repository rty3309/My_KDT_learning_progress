# 위키피디아 인구 순위 테이블 크롤링

from urllib.request import urlopen, Request
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(urlrequest)

population_table = pd.read_html(html, header=0)
population_df = pd.DataFrame(data=population_table[0])
# 핵심은 여기 두 줄

# 첫 번째 행에 전체 인구수 저장됨 : 첫 행 삭제
population_df.drop(0, inplace=True)

# Top 10 국가와 ['Location', 'Population']만 따로 분리
top10_df = population_df.iloc[:10, 0:2]

# 100만명으로 나눈 컬럼 생성 : 'Population_M'
top10_df['Population_M'] = (top10_df['Population']/1000000).round(1)    # 단위(10억, 1억)가 커서 100만명으로 나눔
print(top10_df)

colors = plt.cm.tab10(range(top10_df['Location'].size))
# 각 국가별(10개국) 색상을 자동으로 선택 : tab10
plt.bar(top10_df['Location'], top10_df['Population_M'], color = colors, alpha = 0.8)

plt.title('World Population Top10', fontsize=16)
plt.xticks(rotation=60)
plt.xlabel('Country')
plt.ylabel('Population(10^6)')
plt.tight_layout()
plt.show()