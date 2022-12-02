# Importing pakages
import streamlit as st
from sentiment import model
from upload import upload
from upload1 import upload1
from upload2 import upload3
from companywise import upload4
from similarity import simi
from read import read
def main():
    try:
        st.title("Car Reliability Score")
        menu = ["Full Dataset", "Yearwise Scores","Model Scores","Company Scores","Similarity"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Full Dataset":
            upload()
        elif choice == "Yearwise Scores":
            upload1()
        elif choice == "Model Scores":
            upload3()
        elif choice == "Company Scores":
            upload4()
        elif choice == "Similarity":
            simi()

        # elif choice == "Analytics":
        #     analyse()

        else:
            st.subheader("About tasks")
    except:
        print("Exception")


if __name__ == '__main__':
    main()
