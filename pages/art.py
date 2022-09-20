import streamlit as st
import os
import numpy as np
import requests
from os import path
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def valid_site(url):
    ''' Validate wikipedia website '''

    r = requests.head(f"{url}")
    if r.status_code == 200:
        return True
    elif 400 <= r.status_code < 500:
        return False
    else:
        return None


def body_art():
    """ dispaly wordcloud """

    st.write('---')
    st.write("### ABC Wordcloud Generator")
    st.info("* Link a wikipedia site and wordcloud pitcher will be generated based by frequency of words used")

    # Input from User
    wiki_website = st.text_input(label='Wiki Page', value='https://sv.wikipedia.org/wiki/Guld')

    # Adjusting the image
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        width = st.slider(min_value=400, step=100, max_value=1200, label='Width')    
    with col2:
        height = st.slider(min_value=300, step=100, max_value=1200, label='Height')
    with col3:
        colormap = st.radio('color text', ('Pastel1', 'Accent'))
    with col4:
        bg_color = st.color_picker('Background Color')

    # if website is True
    if valid_site(wiki_website):
        pass
    else:
        st.error('Is this input page correct')
    
    # create wordcloud
    text = wikipedia.page(wiki_website[30:]).content
    wordcloud = WordCloud(
        width=width, height=height, background_color=bg_color, colormap=colormap,
        collocations=False, stopwords=STOPWORDS).generate(text)

    # show image
    st.image(wordcloud.to_image())

    # download image
    if st.button('Like this Image, click here to download'):
        img = wordcloud.to_file(f"{wiki_website[30:]}.png")

        with open(f"{wiki_website[30:]}.png", "rb") as file:
            btn = st.download_button(
                label=f"Download {wiki_website[30:]}",
                data=file,
                file_name=f"{wiki_website[30:]}.png",
                mime="image/png"
          )
        os.remove(f"{wiki_website[30:]}.png")