import streamlit as st
import openai

# API 키 불러오기
openai.api_key = st.secrets["openai"]["api_key"]

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 사용자 입력 받기
prompt = st.chat_input("메시지를 입력하세요...")

# 메시지 처리
if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": prompt})

    # GPT API 호출
    with st.spinner("GPT가 응답을 생성 중입니다..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 또는 "gpt-3.5-turbo"
            messages=st.session_state.messages,
        )
        assistant_reply = response.choices[0].message.content

    # GPT 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

# UI 표시
st.markdown("""
    <style>
    .stChatInput {
        position: fixed;
        bottom: 2rem;
        left: 0;
        width: 100%;
        z-index: 100;
        background-color: white;
        padding: 1rem 2rem;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }
    .stChatInput > div {
        max-width: 700px;
        margin: 0 auto;
    }
    .chat-container {
        margin-bottom: 7rem;
    }
    </style>
""", unsafe_allow_html=True)

# 대화 출력
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
st.markdown('</div>', unsafe_allow_html=True)
