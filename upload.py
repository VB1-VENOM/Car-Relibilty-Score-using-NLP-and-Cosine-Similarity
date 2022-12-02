import streamlit as st
import pandas as pd



# c=mydb.cursor()
from sentiment import model
from read import read

def upload():
    st.title("Upload file here")
    uploaded_file = st.file_uploader("Choose a file")

    df=pd.read_csv(uploaded_file)
    
    if df is not None:
        read(df)
    if st.button('Submit'):
        st.success('Submitted successful')
        df2=model(df)
        print("Count of students with physics marks greater than 11 is->",
        df2[df2['SentimentLabel'] == "POSITIVE"]['Unnamed: 0'].count())
        st.write("The Total Number of Sentiments Reviewed are : %s"%(df2['Unnamed: 0'].count()))
        st.write("The Total Positive Sentiments are : %s"%(df2[df2['SentimentLabel'] == "POSITIVE"]['Unnamed: 0'].count()))
        st.write("The Total Number of Negative Sentiments are : %s"%(df2[df2['SentimentLabel'] == "NEGATIVE"]['Unnamed: 0'].count()))
        
        


    