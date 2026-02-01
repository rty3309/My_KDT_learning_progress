# DataFrame에 일반 함수 적용(apply)

import pandas as pd
import numpy as np

df=pd.DataFrame([[1,2],[3,4],[5,6]], columns=['A','B'])
print(df)

def plus_one(x):
    x=x+1
    return x
df['A']=df['A'].apply(plus_one)
df['B']=df['B'].apply(plus_one)
print(df)

df=df.apply(plus_one)
print(df)

####################################################
# DataFrame에 lambda 함수 적용

df['A'] = df['A'].apply(lambda x:x+1)
print(df)

df=df.apply(lambda x:x+1)
print(df)

df['C'] = [10,20,30]    # 새로운 컬럼 추가
print(df)

df[['A','C']]=df[['A','C']].apply(lambda x:x*10)
print(df)