import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load and cache the data for faster access (kept inside fossil-fuel-co2-tracker.py)
@st.cache
def load_data():
    # Replace 'data.csv' with the actual path to your dataset for "Fossil Fuel CO₂ Tracker"
    df = pd.read_csv(r'.\database\pilot_topdown_CO2_Budget_countries_v1.csv')
    return df

def visualize_fossil_fuel_co2_tracker(experiment):
    # Load the dataset
    df_all = load_data()

    # Function to process the data based on selected experiment
    def select_experiment(df_all, experiment):
        if experiment == 'IS':
            df = df_all.drop(df_all.columns[[4,5,6,7,8,9,12,13,14,15,16,17,20,21,22,23,24,25,34,35,36]], axis=1)
        elif experiment == 'LNLG':
            df = df_all.drop(df_all.columns[[2,3,6,7,8,9,10,11,14,15,16,17,18,19,22,23,24,25,33,35,36]], axis=1)
        elif experiment == 'LNLGIS':
            df = df_all.drop(df_all.columns[[2,3,4,5,8,9,10,11,12,13,16,17,18,19,20,21,24,25,33,34,36]], axis=1)
        elif experiment == 'LNLGOGIS':
            df = df_all.drop(df_all.columns[[2,3,4,5,6,7,10,11,12,13,14,15,18,19,20,21,22,23,33,34,35]], axis=1)
        return df

    df = select_experiment(df_all, experiment)

    # Country list
    countries = df['Alpha 3 Code'].unique()
    countries.sort()

    # Allow user to select a country
    country_name = st.sidebar.selectbox('Select Country', countries)

    # Filter data by selected country
    country_data = df[df['Alpha 3 Code'] == country_name]

    # Ensure the 'Year' column is numeric
    country_data['Year'] = pd.to_numeric(country_data['Year'], errors='coerce')

    # Drop rows with missing or non-numeric years
    country_data = country_data.dropna(subset=['Year'])

    # Simple and bright ΔC_loss chart using Seaborn
    st.header(f"CO₂ Change Over Time for {country_name}")

    if country_data.empty:
        st.error("No data available for the selected country and experiment.")
    else:
        # Simpler ΔC_loss visualization
        plt.figure(figsize=(10, 6))
        
        # Use a bright color palette and larger markers
        sns.lineplot(data=country_data, x='Year', y=experiment + ' dC_loss (TgCO2)', marker='o', color='orange')
        
        # Remove gridlines and use more straightforward axis labels
        plt.axhline(0, color='black', linestyle='--')
        plt.title(f"CO₂ Increase/Decrease for {country_name} Over Time", fontsize=18)
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Change in CO₂ (TgCO₂)', fontsize=14)
        
        # Ensure the x-axis shows integer years, not floats
        plt.xticks(ticks=plt.gca().get_xticks(), labels=[int(x) for x in plt.gca().get_xticks()])
        
        # Display the first plot
        st.pyplot(plt)

    # Enhanced Carbon Budget visualization using Seaborn
    st.header(f'Enhanced Carbon Budget for {country_name} (Multiple Years)')

    # Prepare data for carbon budget visualization for all years
    components = ['FF (TgCO2)', 'Rivers (TgCO2)', 'Wood+Crop (TgCO2)', 
                  experiment+' dC_loss (TgCO2)', experiment+' NCE (TgCO2)']
    labels = ['Fossil Fuels', 'Rivers', 'Wood + Crops', 'ΔC_loss', 'NCE']

    # Prepare DataFrame for all years
    budget_data = country_data[['Year'] + components].set_index('Year')

    # Reshape data for better visualization using Seaborn's barplot
    budget_data_long = pd.melt(budget_data.reset_index(), id_vars=['Year'], 
                               value_vars=components, 
                               var_name='Component', 
                               value_name='CO₂ Emissions (TgCO₂)')

    # Enhanced Carbon Budget visualization with different color palette and grouping by year
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Year', y='CO₂ Emissions (TgCO₂)', hue='Component', data=budget_data_long, palette='coolwarm')
    plt.title(f'Carbon Budget for {country_name} (2015 - 2020)', fontsize=16)
    plt.ylabel('CO₂ Emissions (TgCO₂)', fontsize=12)
    plt.grid(True)
    plt.legend(title='Component')

    # Display the second plot
    st.pyplot(plt)
