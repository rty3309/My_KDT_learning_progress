# File uploader 위젯 예제 2 : 이미지 파일 업로드

import streamlit as st
from PIL import Image

st.header('이미지 업로드')

uploaded_image = st.file_uploader('이미지 선택', type=['png', 'jpg', 'jpeg'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption=uploaded_image.name)
    st.info(f'파일 크기: {uploaded_image.size} bytes')