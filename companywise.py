from sentiment import model

import streamlit as st
import pandas as pd

from sentiment import model
from read import read

def upload4():
    st.title("Upload file here")
    uploaded_file = st.file_uploader("Choose a file")
    
    df2=pd.read_csv(uploaded_file)
    menuy = df2.Company.unique()
    choicey = st.selectbox("Company", menuy)
    df4=df2[df2['Company']==choicey]
    rate = df4["Rating"].mean()
    
    

    if st.button('Submit'):
        st.success('Submitted successful')
        df3=model(df4)
        t=df3['Unnamed: 0'].count()
        p=df3[df3['SentimentLabel'] == "POSITIVE"]['Unnamed: 0'].count()
        n=df3[df3['SentimentLabel'] == "NEGATIVE"]['Unnamed: 0'].count()
        st.write("The Number of Sentiments Reviewed are : %s"%(t))
        st.write("The Number of Positive Sentiments year are : %s"%(p))
        st.write("The Number of Negative Sentiments year are : %s"%(n))
        st.write("Therefore, overall sentiment : %s"%("Positive" if (p>=n) else "Negative"))
        st.write("Reliability score : ",((p/t)*rate)*20)

