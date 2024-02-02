import streamlit as st
import time
import hashlib


def generate_key(story: str, prefix: str) -> str:
    # Generate a MD5 hash of the story text for a unique and stable key
    story_hash = hashlib.md5(story.encode()).hexdigest()
    return f"{prefix}_{story_hash}"


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
        
        # Check if Payment Gateway Integration is selected and render user stories as checkboxes
        if component == 'Payment' and 'Payment Gateway Integration' in selected_epics:
            st.write('### User Stories for Payment Gateway Integration')
            user_stories_payment_gateway_integration = [
                'As a user, I want to add my credit/debit card details securely so that I can use it for payments.',
                'As a user, I want to receive a confirmation for my transaction so that I know the payment was successful.',
                'As a merchant, I want to support multiple payment methods so that I can cater to a wider audience.',
                'As a user, I want to view my transaction history so that I can keep track of my expenses.',
                'As a merchant, I want to integrate with major payment gateways so that I can process payments efficiently.'
            ]
            for story in user_stories_payment_gateway_integration:
                key = generate_key(story, 'story_payment')
                st.checkbox(story, key=key)

        # Check if Refund Process is selected and render user stories as checkboxes
        if component == 'Payment' and 'Refund Process' in selected_epics:
            st.write('### User Stories for Refund Process')
            user_stories_refund_process = [
                'As a user, I want to easily request a refund for a transaction that didn’t meet my expectations so that I can get my money back without hassle.',
                'As a merchant, I want to process refunds efficiently so that I can maintain customer satisfaction and trust.',
                'As a user, I want to be notified of the status of my refund request so that I can know when to expect my refund.',
                'As a merchant, I want to have a clear refund policy that is easy to understand so that users know what to expect.',
                'As a user, I want to understand the criteria for a refund so that I can know if my request will be considered.'
            ]
            for story in user_stories_refund_process:
                key = generate_key(story, 'story_refund')
                st.checkbox(story, key=key)
