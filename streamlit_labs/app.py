import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

st.set_page_config(
    page_icon="",
    page_title="스트림릿 배포하기",
    layout="wide",
)

st.header("스트림릿연습중.")
st.subhearder("스트림릿 기능 맛보기")
cols = st.columns((1,2,3))
col[0].metric("10/11","15 C","2")
col[0].metric("10/12","15 C","2 F")
col[0].metric("10/13","15 C","2")
col[1].metric("10/11","15 C","2")
col[1].metric("10/12","15 C","2 F")
col[1].metric("10/13","15 C","2")

chart_data=pd.DataFrame(
    np.random.randm.(20,3),
    columns=['a','b','c']
)

cols[2].line_chart(chart_data)