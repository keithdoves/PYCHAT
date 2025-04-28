import streamlit as st
from langchain.prompts import PromptTemplate
from datetime  import datetime


# 콘솔에 `source env/bin/activate`를 입력하여 환경 안으로 들어감
# - `streamlit run 21.introductionOfStreamlit.py`를 실행
# - `Command + C`를 눌러 서버를 끌 수 있음
# - `stream.write()`로 출력을 해야하지만, 그냥 변수만 놓아도 화면에 출력된다(`Magic`)
# - `Streamlit`에서 데이터가 바뀌면, 전체 py파일이 재실행된다. 슬라이더를 옮기면, 전체 파일이 다시 실행된다.

today = datetime.today().strftime("%H:%M:%S")
st.title(today)

# write()에 Swiss Army knife라는 설명이 있음
# 이 메서드는 넘겨주는 무엇이든 화면에 나타내려고 함
st.write("hello")
st.write([1,2,3,4])
st.write({"x":1})

# class difinition와 comment, property를 보여줌
#st.write(PromptTemplate)
p = PromptTemplate.from_template("xxxx")

p # Magic st.write하지 않아도 화면에 출력됨.

model = st.selectbox("Choose your model", ("GPT-4 mini", "GPT-1o"))

if model == "GPT-4 mini":
    st.write("cheap")
elif model == "GPT-1o":
    st.write("expensive")
else:
    st.write("")

name = st.text_input("What is your name?")

st.write(name)

value =st.slider("temperatura", min_value=0.1, max_value=1.0,)

st.write(value)
