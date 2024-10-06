import os
import pandas as pd
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
# Initialize the OpenAI client
client = OpenAI(api_key=api_key)
# Set the default encoding to utf-8 for printing
sys.stdout.reconfigure(encoding='utf-8')

def generate_gpt_analysis(country_name, experiment, country_data, user_question):
    # Prepare the data context
    data_context = country_data.head(10).to_string(index=False)
    
    # Create the prompt
    prompt = f"""
    You are a data scientist and climate change expert. The data below shows CO₂ emissions for {country_name}, 
    especially focusing on the following components: Fossil Fuels, Rivers, Wood+Crops, ΔC_loss, and NCE.

    {data_context}

    Based on this data, please answer the following question in detail:
    {user_question}
    """

    # Make the API request using the latest OpenAI API client
    response = client.chat.completions.create(
        model="gpt-4o",  # You can replace this with "gpt-4o-mini" if needed
        messages=[
            {"role": "system", "content": "You are a climate data expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

# Load the data
india_data = pd.read_csv("./pilot_topdown_CO2_Budget_countries_v1.csv")
print(generate_gpt_analysis("India", "CO2 Emissions", india_data, "What are the main sources of CO2 emissions in India?"))
