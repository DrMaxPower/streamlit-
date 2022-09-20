import streamlit as st


class MultiPage:

    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon='SE'
        )
    
    def app_page(self, title, func):
        self.pages.append({'title':title, 'function': func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()