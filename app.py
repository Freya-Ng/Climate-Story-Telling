import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import importlib.util
from openai import OpenAI  # Import OpenAI class
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Set the default encoding to utf-8 for printing (for systems supporting it)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception as e:
        st.error(f"Error setting stdout encoding: {e}")

# Set the correct paths for the files
visual_path = r'.\visual'
sys.path.append(visual_path)

# Dynamically load the co2-in-the-air module
spec_co2_air = importlib.util.spec_from_file_location("co2_in_the_air", os.path.join(visual_path, 'co2-in-the-air.py'))
co2_in_the_air = importlib.util.module_from_spec(spec_co2_air)
spec_co2_air.loader.exec_module(co2_in_the_air)

# Dynamically load the space-co2-budget module
spec_space = importlib.util.spec_from_file_location("space_co2_budget", os.path.join(visual_path, 'space-co2-budget.py'))
space_co2_budget = importlib.util.module_from_spec(spec_space)
spec_space.loader.exec_module(space_co2_budget)

# Dynamically load the fossil-fuel-co2-emissions module
spec_fossil_fuel_co2 = importlib.util.spec_from_file_location("fossil_fuel_co2_emissions", os.path.join(visual_path, 'fossil-fuel-co2-emissions.py'))
fossil_fuel_co2_emissions = importlib.util.module_from_spec(spec_fossil_fuel_co2)
spec_fossil_fuel_co2.loader.exec_module(fossil_fuel_co2_emissions)

# Dynamically load the land-c-flow module
spec_land_c_flow = importlib.util.spec_from_file_location("land_c_flow", os.path.join(visual_path, 'land-c-flow.py'))
land_c_flow = importlib.util.module_from_spec(spec_land_c_flow)
spec_land_c_flow.loader.exec_module(land_c_flow)

# Dynamically load the co2-btw-air-&-ocean module
spec_co2_btw_air_ocean = importlib.util.spec_from_file_location("co2_btw_air_ocean", os.path.join(visual_path, 'co2-btw-air-&-ocean.py'))
co2_btw_air_ocean = importlib.util.module_from_spec(spec_co2_btw_air_ocean)
spec_co2_btw_air_ocean.loader.exec_module(co2_btw_air_ocean)

# Experiment list with full names for better understanding
experiment_full_names = {
    'IS': 'International Standard',
    'LNLG': 'Land and Natural Gas',
    'LNLGIS': 'Land, Natural Gas, and International Standard',
    'LNLGOGIS': 'Land, Natural Gas, Oil, Gas, and International Standard'
}

# Sidebar allows the user to select the experiment using full names
experiment_choice = st.sidebar.selectbox('Select Experiment', list(experiment_full_names.values()))

# Function to get the original abbreviation based on the user selection
def get_experiment_abbreviation(choice):
    for abbr, full_name in experiment_full_names.items():
        if full_name == choice:
            return abbr
    return None

# Get the abbreviation for selected experiment
experiment = get_experiment_abbreviation(experiment_choice)

# Database list (new section)
database_list = [
    "CO₂ in the Air",
    "Space CO₂ Budget",
    "Fossil Fuel CO₂ Tracker",
    "Land Carbon Flow",
    "CO₂ Between Air and Ocean"
]

# Sidebar allows the user to select the database
selected_database = st.sidebar.selectbox('Select Database', database_list)

# Show the charts based on the selected database
def show_charts_for_database(database, experiment):
    if database == "CO₂ in the Air":
        # Check if the required functions exist in the module
        if hasattr(co2_in_the_air, 'plot_co2_growth_rate') and hasattr(co2_in_the_air, 'plot_co2_vs_temperature') and hasattr(co2_in_the_air, 'plot_co2_by_region'):
            co2_in_the_air.plot_co2_growth_rate()
            co2_in_the_air.plot_co2_vs_temperature()
            co2_in_the_air.plot_co2_by_region()
        else:
            st.error("The 'co2_in_the_air' module does not have the required visualization functions.")

    elif database == "Space CO₂ Budget":
        # Call the visualization function from space-co2-budget module
        if hasattr(space_co2_budget, 'visualize_fossil_fuel_co2_tracker'):
            space_co2_budget.visualize_fossil_fuel_co2_tracker(experiment)
        else:
            st.error("The 'space_co2_budget' module does not have the required visualization function.")

    elif database == "Fossil Fuel CO₂ Tracker":
        # Call the visualization functions from fossil-fuel-co2-emissions module
        if hasattr(fossil_fuel_co2_emissions, 'plot_fossil_fuel_emissions'):
            fossil_fuel_co2_emissions.plot_fossil_fuel_emissions()
        else:
            st.error("The 'fossil_fuel_co2_emissions' module does not have the required visualization functions.")

    elif database == "Land Carbon Flow":
        # Call the visualization functions from land-c-flow module
        if hasattr(land_c_flow, 'plot_land_carbon_flow'):
            land_c_flow.plot_land_carbon_flow()
        else:
            st.error("The 'land_c_flow' module does not have the required visualization functions.")

    elif database == "CO₂ Between Air and Ocean":
        # Call the visualization functions from co2-btw-air-&-ocean module
        if hasattr(co2_btw_air_ocean, 'plot_co2_flux_visualization'):
            co2_btw_air_ocean.plot_co2_flux_visualization()
        else:
            st.error("The 'co2_btw_air_ocean' module does not have the required visualization functions.")

# Display selected charts
show_charts_for_database(selected_database, experiment)

# GPT Analysis Section
st.header(f'GPT Analysis for {selected_database}')

# User inputs a question for GPT analysis
user_question = st.text_input('Ask a question about the data or chart:')

def generate_gpt_analysis(selected_database, experiment, user_question):
    # Prepare the data context (using placeholder data for simplicity)
    data_context = f"This is some data context for the selected database: {selected_database}."
    
    # Create the prompt
    prompt = f"""
    You are a data scientist and climate change expert. The data below shows CO₂ emissions for the selected database ({selected_database}),
    especially focusing on the experiment ({experiment}).

    {data_context}

    Based on this data, please answer the following question in detail:
    {user_question}
    """

    # Make the API request using the OpenAI client
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Replace with "gpt-4o-mini" if needed
        messages=[
            {"role": "system", "content": "You are a climate data expert."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

# Process GPT response if user asks a question
if user_question:
    with st.spinner('Processing your question...'):
        try:
            analysis = generate_gpt_analysis(selected_database, experiment, user_question)
            st.subheader('Analysis Result')
            st.write(analysis)
        except Exception as e:
            st.error(f"An error occurred: {e}")