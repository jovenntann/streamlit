from openai import OpenAI
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


client = OpenAI(
    api_key=os.environ['OPENAI_KEY']
)


def generate_persona(business_description: str) -> list:
    """
    This function uses OpenAI to generate a list of persona of the app based on the provided business description.
    :param business_description: A string describing the business.
    :return: A list of persona representing the generated personas.
    """
    logging.info(f"Generating persona for business description: {business_description}")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Based on the provided business description, please generate a list of application persona (e.g admin, customer, manager) for the app: {business_description} List down in Array in this format: ['Persona 1', 'Persona 2']",
                }
            ],
            model="gpt-4",
        )
        content_response = response.choices[0].message.content
        converted_response = content_response.replace('\'', '').replace('[', '').replace(']', '').split(', ')
        generated_persona = [persona.strip() for persona in converted_response]
        logging.info(f"Type of generated persona: {type(generated_persona)}")
        logging.info(f"Generated persona: {generated_persona}")
        return generated_persona
    except Exception as e:
        logging.error(f"Error generating persona: {e}")
        return []


def generate_components(description: str) -> list:
    """
    This function uses OpenAI to generate a list of components based on the provided business description.
    :param description: A string describing the business.
    :return: A list of components relevant to the business.
    """
    logging.info(f"Generating components for business description: {description}")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Based on the provided business description, please list list down possible sub application: {description} List down in Array in this format: ['Payments', 'Delivery']",
                }
            ],
            model="gpt-4",
        )
        content_response = response.choices[0].message.content
        converted_response = content_response.replace('\'', '').replace('[', '').replace(']', '').split(', ')
        generated_components = [component.strip() for component in converted_response]
        logging.info(f"Type of generated components: {type(generated_components)}")
        logging.info(f"Generated components: {generated_components}")
        return generated_components  # Fixed the return statement
    except Exception as e:
        logging.error(f"Error generating components: {e}")
        return []


def generate_epics(business_description: str, component: str) -> list:
    """
    This function uses OpenAI to generate a list of epics based on the provided business description and component.
    :param business_description: A string describing the business.
    :param component: A string representing the selected component.
    :return: A list of epics relevant to the business and component.
    """
    logging.info(f"Generating epics for business description: {business_description} and component: {component}")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Based on the provided business description and selected component, please list down possible epics: {business_description}, {component} List down in Array in this format: ['Epic 1', 'Epic 2']",
                }
            ],
            model="gpt-4",
        )
        content_response = response.choices[0].message.content
        converted_response = content_response.replace('\'', '').replace('[', '').replace(']', '').split(', ')
        generated_epics = [epic.strip() for epic in converted_response]
        logging.info(f"Type of generated epics: {type(generated_epics)}")
        logging.info(f"Generated epics: {generated_epics}")
        return generated_epics
    except Exception as e:
        logging.error(f"Error generating epics: {e}")
        return []


def generate_user_stories(business_description: str, component: str, epic: str) -> list:
    """
    This function uses OpenAI to generate user stories based on the provided business description, component, and epic.
    :param business_description: A string describing the business.
    :param component: A string representing the selected component.
    :param epic: A string representing the selected epic.
    :return: A list of user stories relevant to the business, component, and epic.
    """
    logging.info(f"Generating user stories for business description: {business_description}, component: {component}, and epic: {epic}")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Based on the provided business description, selected component, and epic, please generate user stories: {business_description}, {component}, {epic} List down in Array in this format: ['Story 1', 'Story 2']",
                }
            ],
            model="gpt-4",
        )
        content_response = response.choices[0].message.content
        converted_response = content_response.replace('\'', '').replace('[', '').replace(']', '').split(', ')
        generated_stories = [story.strip() for story in converted_response]
        logging.info(f"Type of generated user stories: {type(generated_stories)}")
        logging.info(f"Generated user stories: {generated_stories}")
        return generated_stories
    except Exception as e:
        logging.error(f"Error generating user stories: {e}")
        return []


def generate_integrations(business_description: str) -> list:
    """
    This function uses OpenAI to generate integrations based on the provided business description.
    :param business_description: A string describing the business.
    :return: A list of integrations relevant to the business description.
    """
    logging.info(f"Generating integrations for business description: {business_description}")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Based on the provided business description, please generate 3rd party integrations: {business_description} List down in Array in this format: ['Integration 1', 'Integration 2']",
                }
            ],
            model="gpt-4",
        )
        content_response = response.choices[0].message.content
        converted_response = content_response.replace('\'', '').replace('[', '').replace(']', '').split(', ')
        generated_integrations = [integration.strip() for integration in converted_response]
        logging.info(f"Type of generated integrations: {type(generated_integrations)}")
        logging.info(f"Generated integrations: {generated_integrations}")
        return generated_integrations
    except Exception as e:
        logging.error(f"Error generating integrations: {e}")
        return []


