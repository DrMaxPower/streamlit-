import streamlit as st
import pandas as pd
import texthero as hero
from wikipedia import *



def body_hero():
    st.write('---')
    st.text(f"* This will be a Hero")

    txt = WikipediaPage('IPython').content
    txt = pd.Series(data=txt)

