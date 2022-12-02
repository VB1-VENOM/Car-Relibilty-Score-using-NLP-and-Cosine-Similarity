import pandas as pd
import streamlit as st

def read(df):
    with st.expander("View all Cars"):
        st.dataframe(df)