import streamlit as st
import mysql.connector
import pandas as pd

def analyse():
    result=c.execute("SELECT * FROM table1").fetchall()
    df2=pd.DataFrame(result,columns=['Unnamed: 0', 'Unnamed: 0.1', 'Vehicle_Title', 'Review', 'Rating','Year','Company','SentimentLabel','SentimentScore'])
    print("Count of students with physics marks greater than 11 is->",
    df2[df2['SentimentLabel'] == "POSITIVE"]['Unnamed: 0'].count())
    st.write("The Total Number of Sentiments Reviewed are : %s"%(df2['Unnamed: 0'].count()))
    st.write("The Total Positive Sentiments are : %s"%(df2[df2['SentimentLabel'] == "POSITIVE"]['Unnamed: 0'].count()))
    st.write("The Total Number of Negative Sentiments are : %s"%(df2[df2['SentimentLabel'] == "NEGATIVE"]['Unnamed: 0'].count()))
    menu = ["Group by Year", "Group by Model"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Group by Year":
        menuy = df2.Year.unique()
        choicey = st.selectbox("Year", menuy)
        df3=df2[df2['Year']==choicey]
        t=df3['Unnamed: 0'].count()
        p=df3[df3['SentimentLabel'] == "POSITIVE"]['Unnamed: 0'].count()
        n=df3[df3['SentimentLabel'] == "NEGATIVE"]['Unnamed: 0'].count()
        st.write("The Number of Sentiments Reviewed in this year are : %s"%(t))
        st.write("The Number of Positive Sentiments in this year are : %s"%(n))
        st.write("The Number of Negative Sentiments in this year are : %s"%(p))
        st.write("Therefore, overall sentiment : %s"%("Positive" if (p>=n) else "Negative"))

    elif choice=="Group by Model":
        menum=df2.Vehicle_Title.unique()
        choicem=st.selectbox("Model", menum)
        df3=df2[df2['Vehicle_Title']==choicem]
        t=df3['Unnamed: 0'].count()
        p=df3[df3['SentimentLabel'] == "POSITIVE"]['Unnamed: 0'].count()
        n=df3[df3['SentimentLabel'] == "NEGATIVE"]['Unnamed: 0'].count()
        st.write("The Number of Sentiments Reviews are : %s"%(t))
        st.write("The Number of Positive Sentiments are : %s"%(n))
        st.write("The Number of Negative Sentiments are : %s"%(p))
        st.write("Therefore, overall sentiment : %s"%("Positive" if (p>=n) else "Negative"))