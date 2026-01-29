# Button 위젯 예제 2 : 버튼 클릭 시 함수 호출

import streamlit as st

def button_write():
    st.write('button activated')

# 모든 버튼 클릭 : 스크립트 재실행
st.button('Reset', type='primary')
st.button('activate', on_click=button_write)