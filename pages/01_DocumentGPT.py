import streamlit as st
import time

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="🍅"
)

st.title("Document GPT")

# 만약 session_state에서 message의 키가 없다면
if "messages" not in st.session_state:
    #빈 list로 초기화한다.
    st.session_state["messages"] = []


def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state["messages"].append({"message": message, "role": role})

# 과거 캐시된 대화 출력
for message in st.session_state["messages"]:
    send_message(
        message["message"],
        message["role"],
        save=False,
        )

message = st.chat_input("Send a message to the ai")

# 인풋 출력
if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f"You said: {message}", "ai")

    with st.sidebar:
        st.write(st.session_state)