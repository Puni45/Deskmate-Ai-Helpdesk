import os
from openai import OpenAI
from dotenv import load_dotenv

# Explicitly load .env file
load_dotenv(dotenv_path=".env")

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def extract_intent(user_query):

    prompt = f"""
    You are an IT helpdesk assistant.

    Analyze the user query and return ONLY valid JSON.

    Possible intents:
    - software_access
    - password_reset
    - ticket_status
    - vpn_issue
    - out_of_scope

    JSON format:
    {{
        "intent": "",
        "software": "",
        "priority": "",
        "ticket_id": ""
    }}

    Do not include explanations.
    Do not include markdown.
    Do not include ```json.

    Query:
    {user_query}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content