import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Chatbot")
st.title("🤖 Mera AI Assistant")

API_KEY = st.secrets.get("GEMINI_KEY")
if not API_KEY:
    st.error("GEMINI_KEY missing")
    st.stop()

genai.configure(api_key=API_KEY)

# ✅ USE THIS MODEL
model = genai.GenerativeModel('gemini-1.5-flash-latest')

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Yahan likhein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = model.generate_content(prompt)
        ai_text = response.text
    except Exception as e:
        ai_text = f"❌ Gemini Error: {e}"

    with st.chat_message("assistant"):
        st.markdown(ai_text)

    st.session_state.messages.append({"role": "assistant", "content": ai_text})



