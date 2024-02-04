import streamlit as st
from utils import OpenAIClient


# Initialize OpenAIClient
openai_client = OpenAIClient()
openai_client.client.api_key = st.text_input("Enter your OpenAI API Key", type='password')

# PERSONAS

# Check if 'personas' key exists in session_state, if not initialize it as an empty list
if 'personas' not in st.session_state:
    st.session_state['personas'] = []

st.title("User Story Generation")
business_description = st.text_area("Enter the business description:")

# You no longer need `persona_generated` as session state will track the personas
if st.button("Generate Persona", key="generate_persona_button"):
    with st.spinner("Generating Persona..."):
        st.session_state['personas'] = openai_client.generate_persona(business_description=business_description)

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
        st.session_state['integrations'] = openai_client.generate_integrations(business_description=business_description)

# Check if there are any integrations to display
if st.session_state['integrations']:
    for integration in st.session_state['integrations']:
        unique_key = f"{integration}_checkbox"  # Create a unique key for each persona
        st.checkbox(integration, value=False, key=unique_key)  # Pass the unique key to st.checkbox


# INTEGRATION TASKS

if 'integration_tasks' not in st.session_state:
    st.session_state['integration_tasks'] = {}

if st.button("Generate Integration Tasks"):
    with st.spinner("Generating Integration Tasks..."):  # Add loading spinner
        selected_personas = [persona for persona in st.session_state['personas'] if st.session_state[persona+"_checkbox"]]
        selected_integrations = [integration for integration in st.session_state['integrations'] if st.session_state[integration+"_checkbox"]]
        for persona in selected_personas:
            st.session_state['integration_tasks'][persona] = {}
            for integration in selected_integrations:
                tasks = openai_client.generate_tasks_based_on_integration(business_description=business_description, persona=persona, integration=integration)
                st.session_state['integration_tasks'][persona][integration] = tasks

# Check if there are any integration tasks to display
if st.session_state['integration_tasks']:
    for persona, integrations in st.session_state['integration_tasks'].items():
        for integration, tasks in integrations.items():
            st.subheader(f"Integration Tasks for {persona} with {integration}")
            for task in tasks:
                unique_key = f"{persona}_{integration}_{task}_checkbox"  # Create a unique key for each task
                st.checkbox(task, value=False, key=unique_key)  # Pass the unique key to st.checkbox

# EPICS

if 'epics' not in st.session_state:
    st.session_state['epics'] = []

if st.button("Generate Epics"):
    with st.spinner("Generating Epics..."):  # Add loading spinner
        st.session_state['epics'] = openai_client.generate_epics(business_description=business_description)

# Check if there are any epics to display
if st.session_state['epics']:
    for epic in st.session_state['epics']:
        unique_key = f"{epic}_checkbox"  # Create a unique key for each epic
        st.checkbox(epic, value=False, key=unique_key)  # Pass the unique key to st.checkbox
        
# USER STORIES

if 'user_stories' not in st.session_state:
    st.session_state['user_stories'] = []

if st.button("Generate User Stories"):
    with st.spinner("Generate User Stories..."):  # Add loading spinner
        selected_personas = [persona for persona in st.session_state['personas'] if st.session_state[persona+"_checkbox"]]
        for persona in selected_personas:
            user_stories_for_persona = openai_client.generate_user_stories(business_description=business_description, persona=persona)
            st.session_state['user_stories'].extend(user_stories_for_persona)

if st.session_state['user_stories']:
    for user_story in st.session_state['user_stories']:
        unique_key = f"{user_story}_checkbox"  
        st.checkbox(user_story, value=False, key=unique_key)


# PRINT 

if st.button("Print Checked Items"):
    selected_personas = [persona for persona in st.session_state['personas'] if st.session_state[persona+"_checkbox"]]
    selected_integrations = [integration for integration in st.session_state['integrations'] if st.session_state[integration+"_checkbox"]]
    st.write("Selected Personas:", selected_personas)
    st.write("Selected Integrations:", selected_integrations)
