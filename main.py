import streamlit as st
from utils import generate_persona, generate_integrations, generate_tasks_based_on_integration

# PERSONAS

# Check if 'personas' key exists in session_state, if not initialize it as an empty list
if 'personas' not in st.session_state:
    st.session_state['personas'] = []

st.title("User Story Generation")
business_description = st.text_area("Enter the business description:")

# You no longer need `persona_generated` as session state will track the personas
if st.button("Generate Persona", key="generate_persona_button"):
    with st.spinner("Generating Persona..."):
        st.session_state['personas'] = generate_persona(business_description=business_description)

# Check if there are any personas to display
if st.session_state['personas']:
    for persona in st.session_state['personas']:
        unique_key = f"{persona}_checkbox"  # Create a unique key for each persona
        st.checkbox(persona, value=False, key=unique_key)  # Pass the unique key to st.checkbox

# INTEGRATIONS

if 'integrations' not in st.session_state:
    st.session_state['integrations'] = []

if st.button("Generate Integrations"):
    with st.spinner("Generating Integrations..."):
        st.session_state['integrations'] = generate_integrations(business_description=business_description)

# Check if there are any integrations to display
if st.session_state['integrations']:
    for integration in st.session_state['integrations']:
        unique_key = f"{integration}_checkbox"  # Create a unique key for each persona
        st.checkbox(integration, value=False, key=unique_key)  # Pass the unique key to st.checkbox


# INTEGRATION TASKS

if 'integration_tasks' not in st.session_state:
    st.session_state['integration_tasks'] = []

if st.button("Generate Integration Tasks"):
    with st.spinner("Generating Integration Tasks..."):  # Add loading spinner
        selected_integrations = [integration for integration in st.session_state['integrations'] if st.session_state[integration+"_checkbox"]]
        st.session_state['integration_tasks'] = generate_tasks_based_on_integration(business_description=business_description,integration=selected_integrations[0])

# Check if there are any integration tasks to display
if st.session_state['integration_tasks']:
    for integration_task in st.session_state['integration_tasks']:
        unique_key = f"{integration_task}_checkbox"  # Create a unique key for each persona
        st.checkbox(integration_task, value=False, key=unique_key)  # Pass the unique key to st.checkbox

# PRINT 

if st.button("Print Checked Items"):
    selected_personas = [persona for persona in st.session_state['personas'] if st.session_state[persona+"_checkbox"]]
    selected_integrations = [integration for integration in st.session_state['integrations'] if st.session_state[integration+"_checkbox"]]
    st.write("Selected Personas:", selected_personas)
    st.write("Selected Integrations:", selected_integrations)
    