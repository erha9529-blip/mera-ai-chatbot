import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 Mera AI Assistant")

# 2. API Key (Yahan apni key likhein ya sidebar mein option dein)
API_KEY = st.secrets["GEMINI_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# 3. Chat History initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Purani baatein screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input aur AI Response
if prompt := st.chat_input("Yahan kuch likhein..."):
    # User ka message save aur show karna
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI se jawab mangna
   # AI se jawab mangna (SAFE WAY)
try:
    response = model.generate_content(prompt)
    ai_response = response.text
except Exception as e:
    ai_response = f"❌ Error: {e}"


    
    # AI ka message save aur show karna
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})







