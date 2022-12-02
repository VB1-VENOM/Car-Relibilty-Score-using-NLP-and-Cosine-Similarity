import pandas as pd 
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from read import read
def similarity(new_data,tr):
    similar = []
    vectorizer = TfidfVectorizer()
    for i in new_data:
        
            
            corpus = [new_data[i],tr]
            trsfm=vectorizer.fit_transform(corpus)
            doc1 = trsfm[0:1].todense()
            doc2 = trsfm[1:2].todense()
            doc_1 = []

            for k in range(len(doc1[0])):
                doc_1.append(doc1[k])
            doc_2 = []
            for u in range(len(doc2[0])):
                doc_2.append(doc2[u])
            doc_1 = np.squeeze(np.asarray(doc_1))
            doc_2 = np.squeeze(np.asarray(doc_2))
            # Dot and norm
            dot = sum(a*b for a, b in zip(doc_1, doc_2))
            norm_a = sum(a*a for a in doc_1) ** 0.5
            norm_b = sum(b*b for b in doc_2) ** 0.5

            # Cosine similarity
            
            cos_sim = dot / (norm_a * norm_b)
            #print([i,j,cos_sim])
            
            similar.append([i,cos_sim])
    return similar
def simi():
    st.title("Upload here")
    uploaded_file = st.file_uploader("Choose a file")
    c = pd.read_csv(uploaded_file)
    import numpy as np 
    from sklearn.feature_extraction.text import TfidfVectorizer
    name = list(c['Vehicle_Title'])
    trait = list(c['Review'])
    res = {}
    for key in name :
        for j in trait:
            res[key] = j
            trait.remove(j)
            break
    tr=st.text_input("Enter traits of the car you would wish to have")
    
    
    #tr = input("Enter traits of the car you would wish to have")

    similar = similarity(res,tr)
    cols = ['Name1','similarity']
    s_df = pd.DataFrame(similar,columns=cols)
    s_df.sort_values('similarity',ascending=False).head()
    read(s_df)