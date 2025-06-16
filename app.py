import streamlit as st

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# CSS로 입력창을 하단에 고정
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
        margin-bottom: 6rem; /* 아래 입력창 영역 확보 */
    }
    </style>
""", unsafe_allow_html=True)

# 챗 메시지 출력 (상단)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
st.markdown('</div>', unsafe_allow_html=True)

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요..."):
    # 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 응답 생성 (임시 응답)
    response = f"'{prompt}'에 대한 답변입니다."
    st.session_state.messages.append({"role": "assistant", "content": response})

