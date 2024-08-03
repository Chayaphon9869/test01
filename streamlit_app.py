import streamlit as st
import pandas as pd

st.title('Data Display with Streamlit')

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the uploaded file
    try:
        data = pd.read_csv(uploaded_file)
        st.write(data)
    except Exception as e:
        st.error(f"Error: {e}")
