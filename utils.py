from openai import OpenAI
import logging
import os
import json


class OpenAIClient:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        self.client = OpenAI(
            api_key=None
        )

    def generate_persona(self, business_description: str) -> list:
        """
        This function uses OpenAI to generate a list of persona of the app based on the provided business description.
        :param business_description: A string describing the business.
        :return: A list of persona representing the generated personas.
        """
        logging.info(f"Generating persona for business description: {business_description}")
        try:
            response = self.client.chat.completions.create(
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

    def generate_epics(self, business_description: str) -> list:
        """
        This function uses OpenAI to generate a list of epics based on the provided business description.
        :param business_description: A string describing the business.
        :return: A list of epics relevant to the business.
        """
        logging.info(f"Generating epics for business description: {business_description}")
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": 'Business Description: ' + business_description + ' based on the provided business description, please generate epics strictly in this json format example { data: ["User Management"] }',
                    }
                ],
                model="gpt-4-0125-preview",
                response_format= { "type":"json_object" }
            )
            content_response = response.choices[0].message.content
            content_json = json.loads(content_response)
            logging.info(content_json)
            logging.info(f"Generated epics: {content_json}")
            return content_json['data']
        except Exception as e:
            logging.error(f"Error generating epics: {e}")
            return []

    def generate_user_stories(self, business_description: str, persona: str) -> list:
        """
        This function uses OpenAI to generate user stories based on the provided business description and persona.
        :param business_description: A string describing the business.
        :param persona: A string representing the selected persona.
        :return: A list of user stories relevant to the business and persona.
        """
        logging.info(f"Generating user stories for business description: {business_description}, persona: {persona}")
        try:
            response = self.client.chat.completions.create(
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


    def generate_integrations(self, business_description: str) -> list:
        """
        This function uses OpenAI to generate integrations based on the provided business description.
        :param business_description: A string describing the business.
        :return: A list of integrations relevant to the business description.
        """
        logging.info(f"Generating integrations for business description: {business_description}")
        try:
            response = self.client.chat.completions.create(
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


    def generate_tasks_based_on_integration(self, business_description: str, persona: str, integration: str) -> list:
        """
        This function uses OpenAI to generate tasks based on the provided business description and integration.
        :param business_description: A string describing the business.
        :param persona: A string representing the selected persona.
        :param integration: A string describing the integration.
        :return: A list of tasks relevant to the business description, persona, and integration.
        """
        logging.info(f"Generating tasks for business description: {business_description}, persona: {persona}, and integration: {integration}")
        try:
            response = self.client.chat.completions.create(
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
