import pandas as pd
import pandas_profiling
import streamlit as st



from streamlit_pandas_profiling import st_profile_report


def profiling_body():
    st.info('make a pandas profiling info page')

    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input('Not woring now')
    with col2:
        uploaded_file = st.file_uploader("What upload CSV file")
        if uploaded_file is not None:        
            while '.csv' in uploaded_file:
                #read csv
                df1=pd.read_csv(uploaded_file)
                st_profile_report(df1)