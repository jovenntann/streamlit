from openai import OpenAI
import logging
import os
import json


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
                    "content": 'Business Description: ' + business_description + ' based on the provided business description, please generate a list of application persona for the app in json format: { data: ["Admin", "Customer", "Provider"] }',
                }
            ],
            model="gpt-4-0125-preview",
            response_format= { "type":"json_object" }
        )
        content_response = response.choices[0].message.content
        content_json = json.loads(content_response)
        logging.info(content_json)

        logging.info(f"Type of generated persona: {type(content_json)}")
        logging.info(f"Generated persona: {content_json}")
        return content_json['data']
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


def generate_user_stories(business_description: str, persona: str) -> list:
    """
    This function uses OpenAI to generate user stories based on the provided business description, component, and epic.
    :param business_description: A string describing the business.
    :param component: A string representing the selected component.
    :param epic: A string representing the selected epic.
    :return: A list of user stories relevant to the business, component, and epic.
    """
    logging.info(f"Generating user stories for business description: {business_description}, persona: {persona}")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": 'Business Description: ' + business_description + ' based on the provided business description, please generate user stories for persona of ' + persona + ' including the estimated hours to develop strictly in this json format example { data: ["As a User, I want to login 2hrs"] }',
                }
            ],
            model="gpt-4-0125-preview",
            response_format= { "type":"json_object" }
        )
        content_response = response.choices[0].message.content
        content_json = json.loads(content_response)
        logging.info(content_json)
        logging.info(f"Generated user stories: {content_json}")
        return content_json['data']
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
                    "content": 'Business Description: ' + business_description + ' based on the provided business description, please generate a list of 3rd party integration for the app in json format example: { data: ["Paypal (Payment Integration)", "Stripe (Payment Integration)", "Dropbox (File Upload)"] }',
                }
            ],
            model="gpt-4-0125-preview",
            response_format= { "type":"json_object" }
        )
        content_response = response.choices[0].message.content
        content_json = json.loads(content_response)
        logging.info(content_json)
        logging.info(f"Generated integrations: {content_json}")
        return content_json['data']
    except Exception as e:
        logging.error(f"Error generating integrations: {e}")
        return []



def generate_tasks_based_on_integration(business_description: str, persona: str, integration: str) -> list:
    """
    This function uses OpenAI to generate tasks based on the provided business description and integration.
    :param business_description: A string describing the business.
    :param integration: A string describing the integration.
    :return: A list of tasks relevant to the business description and integration.
    """
    logging.info(f"Generating tasks for business description: {business_description} and integration: {integration}")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": 'Business Description: ' + business_description + ' based on the provided business description, please generate user stories for persona of ' + persona + ' pertaining to ' + integration + ' integration including the estimated hours to develop strictly in this json format example { data: ["As a User,"] }',
                }
            ],
            model="gpt-4-0125-preview",
            response_format= { "type":"json_object" }
        )
        content_response = response.choices[0].message.content
        content_json = json.loads(content_response)
        logging.info(content_json)
        logging.info(f"Generated integration tasks: {content_json}")
        return content_json['data']
    
    except Exception as e:
        logging.error(f"Error generating tasks: {e}")
        return []
