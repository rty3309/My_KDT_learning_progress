# File uploader 위젯 예제 1 : csv 파일 업로드

import streamlit as st
import pandas as pd

file = st.file_uploader('Choose a file', type='csv', accept_multiple_files=False)

if file is not None:    # csv 파일을 정상 업로드 한 경우 : not None이 됨
    df = pd.read_csv(file)

    st.subheader('데이터 미리 보기')
    st.write(df.head())

    st.subheader('기초 통계')
    st.write(df.describe())