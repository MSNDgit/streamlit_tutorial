import streamlit as st


## Title
st.title('금쪽이의 발자국')

import datetime
today = st.date_input("날짜", datetime.datetime.now())

## MultiSelect
location = st.multiselect("날씨",
                          ("맑음", "비", "눈", "바람","폭풍","안개","쌀쌀", "더움"
                          ))
                          
location = st.multiselect("기분",
                          ("행복", "사랑", "상쾌", "설렘","황홀","긴장","슬픔", "화남",
                          "우울", "그냥", "그리움", "이별","울음","고독","답답", "힘든",
                          "바쁨", "힘든", "피곤", "아픈", "불안"))
                          
st.write(len(location), "가지를 선택했습니다.")
first_name = st.text_input("제목", "Type Here ...")
message = st.text_area("일기내용", "오늘은 어땠나요?")
if st.button("일기저장", key='message'):
    result = message.title()
    st.success(result)



## Return table/dataframe
# table



st.markdown("* * *")




## Radio button
status = st.radio("노래듣기.", ("Active", "Inactive"))
if status == "Active":
    st.success("활성화 되었습니다.")
else:
    st.warning("비활성화 되었습니다.")


st.markdown("* * *")


# Select Box (ex)

## MultiSelect
location = st.multiselect("듣고싶은 음악이 뭐에요?",
                          ("신나는", "즐거운", "잔잔한",
                           "조용한"))
st.write(len(location), "가지를 선택했습니다.")


st.markdown("* * *")


## Buttons
if st.button("분석시작"):
    st.text("감성추천")


## Sidebars
st.sidebar.header("자기소개")
st.sidebar.text_input("","이메일주소")
st.sidebar.text_input("","전화번호를 넣어주세요"
                    )
st.sidebar.header("날짜")
st.sidebar.selectbox("선택하세요.",
                    ["어제",
                     "오늘",
                     "내일"])


# # Text Input
# first_name = st.text_input("이름을 입력하세요.", "Type Here ...")
# if st.button("Submit", key='first_name'):
#     result = first_name.title()
#     st.success(result)


# # Text Area
# message = st.text_area("메세지를 입력하세요.", "Type Here ...")
# if st.button("Submit", key='message'):
#     result = message.title()
#     st.success(result)


# st.markdown("* * *")


# ## Date Input



# # Display Raw Code - one line
# st.subheader("Display one-line code")
# st.code("import numpy as np")

# # Display Raw Code - snippet
# st.subheader("Display code snippet")
# with st.echo():
#     # 여기서부터 아래의 코드를 출력합니다.
#     import pandas as pd
#     df = pd.DataFrame()



# st.markdown("* * *")


# ## Sidebars
# st.sidebar.header("음악")
# st.sidebar.selectbox("선택하세요.",
#                     ["버튼",
#                      "노래",
#                      "코드"])
