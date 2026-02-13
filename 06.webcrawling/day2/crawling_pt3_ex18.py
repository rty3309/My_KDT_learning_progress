# 구글 트렌드 예제 3 : 인기도 변화

from pytrends.request import TrendReq
import matplotlib.pyplot as plt

pytrend = TrendReq(hl='en-US', tz=360)
kw_list = ['Python', 'Java']

# build the payload
pytrend.build_payload(kw_list, cat=0,
                      timeframe='2024-01-01 2026-01-01', geo='US')

# get the interst over time
df = pytrend.interest_over_time()
print(df.head())

df.plot(kind='line')
plt.legend(kw_list)
plt.tight_layout()
plt.show()