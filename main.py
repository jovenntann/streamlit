import streamlit as st
import time

# Title of the app
st.title('User Stories Generation')

# A simple text input for the client to describe their business
business_description = st.text_input('Describe your business')

# Initialize components in session state if it doesn't exist
if 'components' not in st.session_state:
    st.session_state.components = []

# A button to generate the list of components with loading effects
if st.button('Generate Components'):
    with st.spinner('Generating...'):
        time.sleep(5)  # Simulating a long process
        st.success('Components generated!')

        # Update the components in session state
        st.session_state.components = [
            'Payment',
            'Delivery',
            'User Management'
        ]

# If components have been generated, display the multiselect for selecting components
if st.session_state.components:
    # Initialize selected_components in session state if it doesn't exist
    if 'selected_components' not in st.session_state:
        st.session_state.selected_components = []
    # Display the multiselect widget and let Streamlit automatically update session_state.selected_components
    st.multiselect('Select components', st.session_state.components, key='selected_components')

# Use session state to check if components are selected
if 'selected_components' in st.session_state and st.session_state.selected_components:
    # List of epics based on selected components
    epics = {
        'Payment': ['Payment Gateway Integration', 'Transaction History', 'Refund Process', 'Invoice Generation', 'Discount and Coupons Management'],
        'Delivery': ['Order Tracking', 'Shipping Options', 'Delivery Time Estimation', 'Courier Integration', 'Packaging Options'],
        'User Management': ['User Registration', 'Login & Authentication', 'Profile Management', 'Password Recovery', 'User Permissions & Roles']
    }

    st.write('---')

    for component in st.session_state.selected_components:
        st.write(f'## {component}')
        # Generate multi select based on selected components
        selected_epics = st.multiselect(f'Select epics for {component}', epics[component], key=f'epics_{component}')