# Streamlit 주요 API : 텍스트 출력 예제

'''
Text 출력 함수
'''
import streamlit as st

st.title('This is a title.')
st.header('This is a header.')
st.subheader('This is as subheader.')

st.divider()    # 한 줄의 선 표시

st.text('markdown 텍스트')
st.markdown(
'''
This is main text.
This is how to change the color of
text :red[Red,] :blue[Blue,] :green[Green,]
This is **Bold** ans *Italic* text
'''
)

st.divider()    # 한 줄의 선 표시
st.text('Python code 표시')
st.code(
'''
import matplotlib.pyplot as plt

fig, as = plt.subplots()
ax.plot([1,2,3], [1,4,9])
ax.set_title('Simple Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
'''
)