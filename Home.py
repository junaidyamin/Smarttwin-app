import streamlit as st

def app():
    st.title("Home")
    st.write("Welcome to the Knowledge-Based Decision Support System for implementing Digital Twin in construction projects.")
    st.write("This system will enable you to assess the extent to which Digital Twin is suitable for your project and guide you through the process of evaluating your project. It will also provide recommendations based on various factors. Click the 'Next' button to proceed.")

    if st.button("Next"):
        st.session_state.page = 'Project Parameters'
        st.rerun()

if __name__ == '__main__':
    app()
