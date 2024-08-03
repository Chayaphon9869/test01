import streamlit as st
import pandas as pd


st.title('Automation Patch')

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.write(data)
    except FileNotFoundError:
        st.error("File not found.")
    except pd.errors.EmptyDataError:
        st.error("No data found in the file.")
    except pd.errors.ParserError:
        st.error("Error parsing the file.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

