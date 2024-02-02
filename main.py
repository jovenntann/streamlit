import streamlit as st
import time

# Title of the app
st.title('User Stories Generation')

# A simple text input for the client to describe their business
business_description = st.text_input('Describe your business')

# A button to generate the list of components with loading effects
if st.button('Generate Components'):
    # Generate the list of components using OpenAI's GPT-3
    with st.spinner('Generating...'):
        time.sleep(5)  # Simulating a long process
        st.success('Components generated!')

# Components
components = [
    'Payment',
    'Delivery',
    'User Management'
]

# Create checkboxes based on the components
selected_components = st.multiselect('Select components', components)

# List of epics based on selected components
epics = {
    'Payment': ['Payment Gateway Integration', 'Transaction History', 'Refund Process', 'Invoice Generation', 'Discount and Coupons Management'],
    'Delivery': ['Order Tracking', 'Shipping Options', 'Delivery Time Estimation', 'Courier Integration', 'Packaging Options'],
    'User Management': ['User Registration', 'Login & Authentication', 'Profile Management', 'Password Recovery', 'User Permissions & Roles']
}

st.write('---')

if selected_components:
    for component in selected_components:
        st.write(f'## {component}')
        # Generate multi select based on selected components
        selected_epics = st.multiselect(f'Select epics for {component}', epics[component])
