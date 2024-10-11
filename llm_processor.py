import os
from dotenv import load_dotenv
from groq import Groq
import logging

# Load environment variables from the .env file outside the pyextract directory
load_dotenv()

def process_with_llm(prompt):
    logging.info("Inside process_with_llm function.")
    try:
        # Get the API key from environment variables
        api_key = os.getenv("GROQ_API_KEY")
        # if not api_key:
        #     logging.error("GROQ_API_KEY not found in environment variables.")
        #     return "Error: API key not found."

        client = Groq(api_key=api_key)
        logging.info("Groq client created successfully.")

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-70b-versatile",
        )
        
        logging.info("LLM processed the prompt successfully.")
        return chat_completion.choices[0].message.content

    except Exception as e:
        logging.error(f"An error occurred while processing with LLM: {e}")
        return "Error: Unable to process the prompt."

