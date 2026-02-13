# 구글 트렌드 예제 2 : 관련 검색어 조사

from pytrends.request import TrendReq
import pandas as pd

# pytrend = TrendReq(h1='ko', tz=540)
pytrend = TrendReq()
result = pytrend.suggestions(keyword='Python')
print(type(result))
print(result)

df = pd.DataFrame(result)
if df['mid'] is not None:
    df = df.drop(columns='mid')    # mid : Google trend에서 사용하는 고유 식별자
print(df)