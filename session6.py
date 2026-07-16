import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.title("AI Chat with Chat History")

MAX_MESSAGES = 5  # Maximum user messages allowed

@st.cache_resource
def get_ai_client():
    return genai.Client(api_key=os.getenv("GENAI_API_KEY"))

client = get_ai_client()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0

if "gemini_chat" not in st.session_state:
    st.session_state.gemini_chat = client.chats.create(
        model="gemini-2.5-flash"
    )

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Disable chat input after limit
placeholder = (
    "Out of tokens. Please refresh or start a new chat."
    if st.session_state.user_message_count >= MAX_MESSAGES
    else "Say something"
)

user_message = st.chat_input(
    placeholder,
    disabled=st.session_state.user_message_count >= MAX_MESSAGES
)

if user_message:

    # Check limit
    if st.session_state.user_message_count >= MAX_MESSAGES:
        st.error(" Out of tokens! You have reached the free limit of 5 messages.")
        st.stop()

    # Increase counter
    st.session_state.user_message_count += 1

    # Display user message
    with st.chat_message("user"):
        st.write(user_message)

    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    # Gemini response
    with st.spinner("Thinking..."):
        response = st.session_state.gemini_chat.send_message(user_message)

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response.text)

    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )

# Sidebar
st.sidebar.markdown(f"### Messages Used")
st.sidebar.progress(st.session_state.user_message_count / MAX_MESSAGES)
st.sidebar.write(
    f"**{st.session_state.user_message_count}/{MAX_MESSAGES}** messages used"
)

if st.session_state.user_message_count >= MAX_MESSAGES:
    st.sidebar.error(" Token limit reached.")

# Download chat history
output = "CHAT HISTORY:\n\n"
for msg in st.session_state.messages:
    output += f"{msg['role']}: {msg['content']}\n\n"

st.sidebar.download_button(
    label="Download Chat History",
    data=output,
    file_name="chat_history.txt",
    mime="text/plain"
)