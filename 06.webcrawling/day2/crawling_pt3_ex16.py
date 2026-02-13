# 구글 트렌드 예제 1 : related_queries() 연관 검색어

from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

pytrend = TrendReq()

kw_list = ['K-pop']

pytrend.build_payload(kw_list, geo='US', timeframe='now 7-d', gprop='')
result_dict = pytrend.related_queries()

top_df = result_dict[kw_list[0]]['top']

print(top_df.head())

top5_df = top_df.head(5)

top5_df.plot(x='query', y='value', kind='bar',
             title=f'{kw_list[0]} 연관 검색어', legend=False)

plt.xticks(rotation=30)
plt.xlabel('Query')
plt.ylabel('Value')
plt.tight_layout()
plt.show()