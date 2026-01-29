# 2개의 Tab을 가지는 레이아웃 예제

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

tab1, tab2 = st.tabs(['Table', 'Graph'])    # 문자열로 탭 생성

df = pd.read_csv('medical_cost.csv')
region = 'northwest'
northwest_df = df[df['region']==region]    # 여기 3줄은 공통사항

with tab1:
    st.header(f'Medical Cost: {region}', text_alignment='center')
    st.write('')    # 빈 공백 추가

    st.subheader('데이터프레임 : northwest_df')
    st.write(northwest_df.head(10))

with tab2:
    st.header('BMI와 Charges 산점도 그래프', text_alignment='center')
    st.write('')    # 빈 공백 추가

    col1, col2 = st.columns(2)    # 2개의 컬럼 생성

    with col1:
        st.subheader('산점도 컬럼', text_alignment='center')
        fig, axes = plt.subplots(2,1, figsize=(6,10))    # 2행1열로 만듬

        sns.scatterplot(data=northwest_df, x='bmi', y='charges', hue='smoker', ax=axes[0])
        axes[0].set_title('Scatterplot: BMI vs. Charges (Smoker)')

        sns.scatterplot(data=northwest_df, x='bmi', y='charges', hue='sex', ax=axes[1])
        axes[1].set_title('Scatterplot: BMI vs. Charges (Sex)')
        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        st.subheader("박스플롯 컬럼", text_alignment='center')
  
        fig, axes = plt.subplots(2, 1, figsize=(6,10))
        sns.boxplot(data=northwest_df, x='smoker', y='charges', hue='smoker', ax=axes[0])
        axes[0].set_title('Boxplot: 흡연자와 의료 비용')
  
        sns.boxplot(data=northwest_df, x='sex', y='charges', hue='sex', ax=axes[1])
        axes[1].set_title('Boxplot: 성별 의료 비용')
        plt.tight_layout()
        st.pyplot(fig)
  
  
 