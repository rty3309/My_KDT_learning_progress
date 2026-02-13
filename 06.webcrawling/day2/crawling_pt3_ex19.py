# 구글 트렌드 예제 4 : 인공지능 서비스 인기도

from pytrends.request import TrendReq
import matplotlib.pyplot as plt

pytrend = TrendReq()
kw_list = ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'Perplexity']
pytrend.build_payload(kw_list=kw_list, geo='KR', timeframe='today 1-m')

df = pytrend.interest_over_time()
df = df.drop(columns='isPartial')
print(df.head())

xtick_list = df.index.strftime('%m-%d').tolist()

plt.figure(figsize=(10,4))
plt.title('AI Interest')
plt.plot(xtick_list, df)
plt.xticks(range(len(xtick_list)), xtick_list, rotation=80)
plt.legend(kw_list)
plt.tight_layout()
plt.show()