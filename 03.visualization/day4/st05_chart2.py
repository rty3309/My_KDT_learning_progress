# Streamlit 내장 차트 활용 예제

import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit 내장 차트 예제')

df = pd.DataFrame({
    'date':pd.date_range('2025-01-01', periods=30),
    'Sales':np.random.randint(100,500,30),
    'Costs':np.random.randint(50,300,30)
})

st.subheader('원본 데이터(DataFrame) 요약')
st.write(df.head())

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader('Line Chart')
    st.line_chart(df[['Sales', 'Costs']])

    st.subheader('Area Chart')
    st.area_chart(df[['Sales', 'Costs']])

with col2:
    st.subheader('Bar Chart')
    st.bar_chart(df.tail(7)[['Sales', 'Costs']])

    st.subheader('Scatter Chart')
    st.scatter_chart(df, x='Sales', y='Costs')