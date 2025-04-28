import streamlit as st

# - `pages`안에 파일을 생성하면 `sidebar`에 화면 링크가 생긴다. 파일명은 링크 이름이 된다. 
# - `Streamlit`은 매번 첫 줄부터 재 실행되어 상태를 잃어버리는데,
#   `Session State`는 여러 번 재실행되도 data가 보존될 수 있게 한다.

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="🧚",
)

st.title("FullstackGPT Home")

st.markdown(
    """ 
    # Hello!

    Welcome to my FullstackGPT Portfolio!

    Here are the apps I made:

    - [ ] [DocumentGPT](/DocumentGPT)
    - [ ] [PrivateGPT](/PrivateGPT)
    - [ ] [QuizGPT](/QuizGPT)
    - [ ] [SiteGPT](/SiteGPT)
    - [ ] [MeetingGPT](/MeetingGPT)
    - [ ] [InvestorGPT](/InvestorGPT)
    """
    )