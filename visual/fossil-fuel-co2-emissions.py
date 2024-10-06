import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import json
import os

# Database file path (JSON data)
database_path = r".\\database\\odiac-ffco2-monthgrid-v2023.json"

# Load the JSON database
def load_json_data():
    if os.path.exists(database_path):
        with open(database_path, 'r') as file:
            data = json.load(file)
            return data
    else:
        st.error(f"Database file not found: {database_path}")
        return None

# 1. Global CO₂ Emissions Over Time
def plot_global_emissions():
    # Simulated data for global CO2 emissions over time
    data_global = {
        "Year": list(range(2000, 2023)),
        "CO2_Emissions_Global": [28.7, 29.0, 29.2, 30.0, 30.5, 31.1, 31.6, 32.0, 32.5, 33.0, 33.4, 33.9, 34.5, 35.0, 35.5, 36.1, 36.5, 36.9, 37.5, 38.0, 38.5, 39.0, 39.5],  # Simulated data
    }

    df_global = pd.DataFrame(data_global)

    # Line chart for Global CO2 Emissions over time
    st.header("Global Fossil Fuel CO₂ Emissions (2000-2022)")
    plt.figure(figsize=(10, 6))

    # Use a vibrant color palette
    plt.plot(df_global["Year"], df_global["CO2_Emissions_Global"], marker="o", linestyle="-", color="#1f77b4", label="Global CO₂ Emissions")  # Blue
    plt.fill_between(df_global["Year"], df_global["CO2_Emissions_Global"], color="#aec7e8", alpha=0.5)  # Light blue for area fill

    plt.title("Global Fossil Fuel CO₂ Emissions (2000-2022)", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("CO₂ Emissions (Billion Tons)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)  # Add dashed gridlines for better visibility
    plt.xticks(df_global["Year"], rotation=45)
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the first chart
    st.markdown("""
    **Explanation: Global Fossil Fuel CO₂ Emissions Over Time**
    - **What the data means**: The chart shows how global CO₂ emissions from fossil fuel combustion have evolved from 2000 to 2022. The y-axis represents total CO₂ emissions in billion tons.
    - **Is the change good or not?**: The rising trend in emissions is not good because it indicates increasing levels of greenhouse gases in the atmosphere, which contributes to climate change.
    - **What happens when it changes?**: If CO₂ emissions continue to rise, it will exacerbate global warming, potentially leading to more extreme weather events, rising sea levels, and environmental degradation.
    """)

# 2. CO₂ Emissions by Continent
def plot_continent_emissions():
    # Simulated data for CO2 emissions by continent in 2022
    data_continents = {
        "Continent": ["Asia", "North America", "Europe", "Africa", "South America", "Oceania"],
        "CO2_Emissions_2022": [19.0, 6.5, 4.5, 1.5, 1.0, 0.5],  # Simulated data
    }

    df_continents = pd.DataFrame(data_continents)

    # Bar chart for CO2 Emissions by Continent
    st.header("CO₂ Emissions by Continent (2022)")
    plt.figure(figsize=(10, 6))

    # Use a more modern and attractive color palette for the bars
    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]
    plt.bar(df_continents["Continent"], df_continents["CO2_Emissions_2022"], color=colors, edgecolor='black', linewidth=1.5)

    plt.title("CO₂ Emissions by Continent (2022)", fontsize=16)
    plt.xlabel("Continent", fontsize=12)
    plt.ylabel("CO₂ Emissions (Billion Tons)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)  # Dashed gridlines
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the second chart
    st.markdown("""
    **Explanation: CO₂ Emissions by Continent (2022)**
    - **What the data means**: This bar chart highlights the distribution of CO₂ emissions by continent in 2022. The y-axis shows emissions in billion tons.
    - **Is the change good or not?**: Continents like Asia and North America have higher emissions, which is concerning as these regions contribute significantly to global emissions.
    - **What happens when it changes?**: If emissions in continents with high outputs (like Asia) continue to increase, it will accelerate global climate change. Efforts to reduce emissions in these regions are critical to mitigating environmental impact.
    """)

# 3. CO₂ Emissions in Urban vs Rural Areas
def plot_urban_vs_rural_emissions():
    # Simulated data for urban vs rural CO2 emissions
    data_urban_rural = {
        "Region": ["Urban", "Rural"],
        "CO2_Emissions": [85, 15],  # Simulated percentage data
    }

    df_urban_rural = pd.DataFrame(data_urban_rural)

    # Pie chart for CO2 Emissions in Urban vs. Rural areas
    st.header("CO₂ Emissions: Urban vs. Rural Areas")

    # Updated colors to be more modern and visually appealing
    colors = ["#FF6347", "#4682B4"]  # Tomato red for Urban, Steel Blue for Rural

    plt.figure(figsize=(8, 8))
    plt.pie(df_urban_rural["CO2_Emissions"], 
            labels=df_urban_rural["Region"], 
            autopct='%1.1f%%', 
            colors=colors, 
            startangle=90,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})  # Add black edge to wedges

    plt.title("CO₂ Emissions: Urban vs. Rural Areas", fontsize=16)
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the third chart
    st.markdown("""
    **Explanation: CO₂ Emissions in Urban vs Rural Areas**
    - **What the data means**: This pie chart compares the proportion of CO₂ emissions from urban areas (85%) and rural areas (15%). Urban areas tend to contribute more due to industrialization, transportation, and higher energy demand.
    - **Is the change good or not?**: The large share of emissions from urban areas indicates that cities are major sources of greenhouse gases, which is not a positive sign for climate sustainability.
    - **What happens when it changes?**: If urban emissions continue to rise, air quality will deteriorate, and the urban heat island effect will intensify. Focus on green technologies and infrastructure is crucial to curbing these emissions.
    """)

# 4. Main function to call each of the visualizations
def plot_fossil_fuel_emissions():
    # Load the JSON data before plotting (if needed for real data in the future)
    json_data = load_json_data()

    # Check if the JSON data was loaded successfully
    if json_data is not None:
        # Add logic to process real JSON data if needed, e.g., time-series or other data visualization
        pass  # Placeholder for now

    # Plot the simulated charts
    plot_global_emissions()
    plot_continent_emissions()
    plot_urban_vs_rural_emissions()

