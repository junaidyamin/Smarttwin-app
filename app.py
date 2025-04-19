import streamlit as st
from streamlit_option_menu import option_menu

import Home

import Project_Parameters

import Decision_Factors_Scoring

st.set_page_config(page_title="Knowledge-based Decision Support System")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        
        if 'page' not in st.session_state:
            st.session_state.page = 'Home'

        with st.sidebar:
            app = option_menu(
                menu_title="Twin Decisionmaker",
                options=["Home", "Project Parameters", "Decision Factors Scoring"],
                default_index=0 if st.session_state.page == 'Home' else 1 if st.session_state.page == 'Project Parameters' else 2 if st.session_state.page == 'Decision Factors Scoring' else 0,
            )
        st.session_state.page = app

        if st.session_state.page == "Home":
            Home.app()
        elif st.session_state.page == "Project Parameters":
            Project_Parameters.app()
        elif st.session_state.page == "Decision Factors Scoring":
            Decision_Factors_Scoring.app()

app = MultiApp()
app.run()

background_image_url = "https://i.ibb.co/VLGJV4W/Untitled-design-5.png"
background_css = f"""
<style>
.stApp {{
    background: none;
}}

#background-image {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background-image: url({background_image_url});
    background-size: 50%;  /* Zoom out the image slightly */
    background-repeat: no-repeat;
    background-position: center;  /* Center the image */
}}
</style>
<div id="background-image"></div>
"""

st.markdown(background_css, unsafe_allow_html=True)

