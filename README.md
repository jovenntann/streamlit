
# User Story Generation

This project leverages OpenAI to generate user stories, personas, integrations, integration tasks, and epics based on a given business description. It is developed using Python and Streamlit.

## Prerequisites

- Python 3.11
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Enter your OpenAI API key in the text input field.

3. Enter a business description in the text area.

4. Click the "Generate Persona" button to generate personas based on the business description.

5. Click the "Generate Integrations" button to generate possible integrations for the business.

6. Select the personas and integrations you want to generate tasks for, then click the "Generate Integration Tasks" button.

7. Click the "Generate Epics" button to generate epics based on the business description.

8. Select the personas you want to generate user stories for, then click the "Generate User Stories" button.

9. Click the "Print Checked Items" button to print the selected personas, integrations, integration tasks, epics, and user stories.

## OpenAI Python Client

This project utilizes the OpenAI Python client. For more information, please refer to its official documentation.

## License

This project is licensed under the Apache License 2.0. For more details, see the LICENSE file in the repository.
