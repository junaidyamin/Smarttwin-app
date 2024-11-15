import streamlit as st

def app():
    st.title('Project Parameters')
    st.write('User is required to fill in the Project Details in this section, which consist of the following items:')
    
    # Initialize session state if not already done
    if 'project_details' not in st.session_state:
        st.session_state.project_details = {
            'name_of_user': '',
            'name_of_project': '',
            'assessment_date': None,
            'type_of_project': 'Residential'  # Default to Residential
        }
    
    # Form for project details
    with st.form(key='project_details_form'):
        st.subheader('Project Details')

        # Input fields
        name_of_user = st.text_input('Name of User', value=st.session_state.project_details['name_of_user'])
        name_of_project = st.text_input('Name of Project', value=st.session_state.project_details['name_of_project'])
        assessment_date = st.date_input('Assessment Date', value=st.session_state.project_details['assessment_date'])
        
        # Convert numeric type options to categorical labels
        type_options = ['Residential', 'Commercial', 'Industrial', 'Government']
        type_of_project = st.selectbox('Type of Project', type_options, index=type_options.index(st.session_state.project_details['type_of_project']))
        
        # Form submission buttons
        submit_button = st.form_submit_button(label='Next')
        clear_button = st.form_submit_button(label='Clear Entries')
    
    if submit_button:
        # Save inputs to session state
        st.session_state.project_details = {
            'name_of_user': name_of_user,
            'name_of_project': name_of_project,
            'assessment_date': assessment_date,
            'type_of_project': type_of_project
        }
        
        # Navigate to the next page
        st.session_state.page = 'Decision Factors Scoring'
        st.rerun()
    
    if clear_button:
        # Clear the session state
        st.session_state.project_details = {
            'name_of_user': '',
            'name_of_project': '',
            'assessment_date': None,
            'type_of_project': 'Residential'
        }
        st.rerun()
    
if __name__ == '__main__':
    app()
