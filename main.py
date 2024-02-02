import streamlit as st
from utils import generate_persona, generate_integrations

# Check if 'personas' key exists in session_state, if not initialize it as an empty list
if 'personas' not in st.session_state:
    st.session_state['personas'] = []

st.title("User Story Generation")
business_description = st.text_area("Enter the business description:")

# You no longer need `persona_generated` as session state will track the personas
if st.button("Generate Persona"):
    # Assuming `generate_persona` returns a list of personas
    st.session_state['personas'] = generate_persona(business_description=business_description)

# Check if there are any personas to display
if st.session_state['personas']:
    for persona in st.session_state['personas']:
        unique_key = f"{persona}_checkbox"  # Create a unique key for each persona
        st.checkbox(persona, value=False, key=unique_key)  # Pass the unique key to st.checkbox


if 'integrations' not in st.session_state:
    st.session_state['integrations'] = []

if st.button("Generate Integrations"):
    st.session_state['integrations'] = generate_integrations(business_description=business_description)

# Check if there are any integrations to display
if st.session_state['integrations']:
    for integration in st.session_state['integrations']:
        unique_key = f"{integration}_checkbox"  # Create a unique key for each persona
        st.checkbox(integration, value=False, key=unique_key)  # Pass the unique key to st.checkbox

if st.button("Print Checked Items"):
    selected_personas = [persona for persona in st.session_state['personas'] if st.session_state[persona+"_checkbox"]]
    selected_integrations = [integration for integration in st.session_state['integrations'] if st.session_state[integration+"_checkbox"]]
    st.write("Selected Personas:", selected_personas)
    st.write("Selected Integrations:", selected_integrations)
