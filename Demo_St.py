# Demo_St.py
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Streamlit Demo", layout="centered")
st.title("Streamlit Demo ✔️")
st.write("This is a minimal Streamlit app to confirm your setup.")

st.markdown("**Current time:**")
st.write(datetime.now().isoformat())

name = st.text_input("Enter your name", value="Shandosh")
if st.button("Greet"):
    st.success(f"Hello, {name}! Streamlit is working 🎉")

st.markdown("---")
st.write("If this page loads in your browser, Streamlit is correctly installed.")

