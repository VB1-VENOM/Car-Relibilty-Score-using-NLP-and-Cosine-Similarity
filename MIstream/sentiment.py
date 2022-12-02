import os
import glob
import streamlit as st
import pandas as pd
from transformers import pipeline
from read import read
from analyse import analyse

#import pymysql

def model(df):
    
    sentiment_pipeline = pipeline("sentiment-analysis")
    Label=[]
    Score=[]
    df2=df.loc[0:100]
    for i in df2['Review']:
        p=sentiment_pipeline(i[:512])[0]
        Label.append(p.get('label'))
        Score.append(p.get('score'))
    df2['SentimentLabel']=Label
    df2['SentimentScore']=Score   
    read(df2)
    return (df2)
       
   
    

# import pandas as pd
# import mysql.connector as sql
# db_connection = sql.connect(host='124685.eu-central-1.rds.amazonaws.com', 
#         database="db_name", user='user', password='pw')

# query = 'SELECT * FROM table_name'
# df = pd.read_sql(sql=query, con=db_connection)
# df["Person_Name"] = "xx"
# df_temp = df[['Person_Name', 'Person_ID']]

# query_insert = 'insert into table_name(Person_Name) values %s where Person_ID = %s'
# pars = df_temp.values.tolist()
# pars = list(map(tuple, pars))
# cursor = db_connection.cursor()
# cursor.executemany(query, pars)
# cursor.commit()
# cursor.close()   
    

''' DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='your_user', password='password', server='localhost', database='dname')'''