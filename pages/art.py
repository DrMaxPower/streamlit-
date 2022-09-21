import streamlit as st
import os
import pandas as pd
import numpy as np
import requests
import wikipedia
import texthero as hero
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path
from PIL import Image


def valid_site(url):
    ''' Validate wikipedia website '''

    r = requests.head(f"{url}")
    if r.status_code == 200:
        return True
    elif 400 <= r.status_code < 500:
        return False
    else:
        return None


def body_art(text_clean=None):
    """ dispaly wordcloud """

    st.write('---')
    st.write("### ABC Wordcloud Generator")
    st.info("* Link a wikipedia site and wordcloud pitcher will be generated based by frequency of words used")

    # Input from User
    wiki_website = st.text_input(label='Wiki Page', value='https://sv.wikipedia.org/wiki/Guld')
    # if website is True
    if valid_site(wiki_website):
        pass
    else:
        st.error('Is this input page correct')

    text = wikipedia.page(wiki_website[30:]).content


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


    # create wordcloud
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

    # Show plot Of top words
    text = pd.Series(text)
    text = hero.clean(text)[0]
    st.info(
        f'The text is **{len(text)}** words long and the word: \
             **{(hero.top_words(pd.Series(text)).head(1).index[0])}**\
                 is used **{hero.top_words(pd.Series(text))[0]}** times')


