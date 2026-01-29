# Button 위젯 예제 1 : 기본 버튼 생성

import streamlit as st

st.header('st.button 예제')

# st.button(): 처음 False -> 버튼 클릭 : True로 변경
clicked = st.button('Say hello', type='primary')

if clicked == True:
    st.write(f'안녕하세요! ({clicked})')
else:
    st.write(f'버튼을 눌러보세요.({clicked})')