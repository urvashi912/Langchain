import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF !important;
        color: #262730 !important;
    }
    .reportview-container,
    .main,
    .block-container {
        background-color: #FFFFFF !important;
        color: #262730 !important;
    }
    .sidebar .sidebar-content {
        background-color: #F0F2F6 !important;
        color: #262730 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def chatbot_ui():
    st.title("Chatbot Interface")
    
    # Display chat messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    # User input
    user_input = st.text_input("You:", key="user_input")

    if st.button("Send"):
        if user_input:
            # Append user message to chat
            st.session_state.messages.append({"role": "user", "content": user_input})
            # Here you would call the response generator to get the bot's reply
            # For example: bot_response = response_generator(user_input)
            # st.session_state.messages.append({"role": "bot", "content": bot_response})
            st.session_state.user_input = ""  # Clear input after sending