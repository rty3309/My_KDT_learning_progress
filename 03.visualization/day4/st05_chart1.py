# Streamlit 그래프 표현하기 : st.pyplot() 예제

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import koreanize_matplotlib

tips = pd.read_csv('tips.csv')
fig, axes = plt.subplots(1,2,figsize=(12,5))

# 히스토그램
sns.histplot(data=tips, x='total_bill', bins=20, kde=True, ax=axes[0])
axes[0].set_title('식사 금액 분포')

# 박스플롯
sns.boxplot(data=tips, x='day', y='total_bill', hue='smoker', ax=axes[1])    # ax : 그래프의 위치 지정
axes[1].set_title('요일별 흡연 여부에 따른 식사 금액 분포')

plt.tight_layout()

st.pyplot(fig)