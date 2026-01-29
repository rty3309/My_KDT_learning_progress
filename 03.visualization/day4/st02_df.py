# Streamlit에 DataFrame 출력하기

import streamlit as st
import pandas as pd

st.write('Streamlit을 이용하여 DataFrame 출력하기')

df = pd.DataFrame({
    'Country':['USA', 'China', 'India'],
    'Internet_Users': [29000000, 989000000, 658000000],
    'Percentage': [0.892, 0.684, 0.457]
})
st.write(df)    # 단순히 DataFrame 출력

# DataFrame 스타일 지정
styled_df = df.style.format({    # 여러 스타일을 styled_df에 누적해서 적용
    'Internet_Users': '{:,}',    # 천단위 콤마 추가
    'Percentage': '{:.2f}'    # 퍼센트 값: 소수점 2째자리
})

styled_df = styled_df.highlight_max(axis=0, color='lightcoral')
styled_df = styled_df.highlight_min(axis=0, color='lightblue')
# 이렇게 styled_df 이름을 그대로 써서 누적시키는 것

st.write(styled_df)