import streamlit as st

st.title("Prompt-to-App Demo")

user_input = st.text_input("Describe your idea:")
if user_input:
    st.write("🔧 Here's a prototype:")
    st.markdown(f"**Goal:** {user_input}")
    st.markdown("🚀 This app will be generated soon...")
