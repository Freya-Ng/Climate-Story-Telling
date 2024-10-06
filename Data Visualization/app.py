import os
import streamlit as st
import sys
import importlib.util

# Set the correct paths for the files
visual_path = r'D:\Projects\NASA\visual'
sys.path.append(visual_path)

# Dynamically load the co2-in-the-air module
spec_co2_air = importlib.util.spec_from_file_location("co2_in_the_air", os.path.join(visual_path, 'co2-in-the-air.py'))
co2_in_the_air = importlib.util.module_from_spec(spec_co2_air)
spec_co2_air.loader.exec_module(co2_in_the_air)

# Dynamically load the space-co2-budget module
spec_space = importlib.util.spec_from_file_location("space_co2_budget", os.path.join(visual_path, 'space-co2-budget.py'))
space_co2_budget = importlib.util.module_from_spec(spec_space)
spec_space.loader.exec_module(space_co2_budget)

# Set the default encoding to utf-8 for printing (for systems supporting it)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception as e:
        st.error(f"Error setting stdout encoding: {e}")

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
if selected_database == "CO₂ in the Air":
    # Check if the required functions exist in the module
    if hasattr(co2_in_the_air, 'plot_co2_growth_rate') and hasattr(co2_in_the_air, 'plot_co2_vs_temperature') and hasattr(co2_in_the_air, 'plot_co2_by_region'):
        co2_in_the_air.plot_co2_growth_rate()
        co2_in_the_air.plot_co2_vs_temperature()
        co2_in_the_air.plot_co2_by_region()
    else:
        st.error("The 'co2_in_the_air' module does not have the required visualization functions.")

elif selected_database == "Space CO₂ Budget":
    # Call the visualization function from space-co2-budget module
    if hasattr(space_co2_budget, 'visualize_fossil_fuel_co2_tracker'):
        space_co2_budget.visualize_fossil_fuel_co2_tracker(experiment)
    else:
        st.error("The 'space_co2_budget' module does not have the required visualization function.")