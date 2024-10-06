import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import os

# Set the correct paths to the database
json_file_path = r'D:\Projects\NASA\database\oco2geos-co2-daygrid-v10r.json'

# Check if the JSON file exists before loading it
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        co2_data = json.load(file)
else:
    st.error(f"JSON file not found: {json_file_path}")

# Assuming the JSON file contains the time interval and CO₂ levels
time_interval = pd.date_range(start='2015-01-01', end='2022-02-28', freq='D')

# Simulate CO₂ levels with some random variation over time
np.random.seed(42)  # For reproducibility
co2_levels = 412 + np.cumsum(np.random.normal(0.05, 0.1, len(time_interval)))  # Add cumulative random noise

# Function to plot CO₂ growth rate over time using a line plot
def plot_co2_growth_rate():
    st.header("CO₂ Growth Rate Over Time")  
    growth_rates = pd.Series(co2_levels).pct_change() * 100  # percentage change
    growth_rates = growth_rates.fillna(0)  # Fill NaN values with 0

    # Exaggerate growth rates by multiplying by a factor
    exaggerated_growth_rates = growth_rates * 10
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_interval, exaggerated_growth_rates, color='orange', linewidth=2)
    ax.set_ylim([-1, 1.25])
    ax.set_title('Exaggerated CO₂ Growth Rate Over Time (2015-2022)', fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Exaggerated Growth Rate (%)', fontsize=12)
    ax.grid(True)
    plt.tight_layout()
    st.pyplot(fig)

# Function to plot CO₂ Concentration vs Temperature
def plot_co2_vs_temperature():
    st.header("CO₂ Concentration vs Temperature")
    
    temperature = 15 + (co2_levels - 412) * 0.1  # Mock temperature (in °C)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(co2_levels, temperature, color='red')
    ax.set_ylim([min(temperature) - 1, max(temperature) + 1])
    ax.set_title('CO₂ Concentration vs Temperature', fontsize=14)
    ax.set_xlabel('CO₂ Concentration (ppm)', fontsize=12)
    ax.set_ylabel('Temperature (°C)', fontsize=12)
    ax.grid(True)
    plt.tight_layout()
    st.pyplot(fig)

# Function to plot CO₂ levels by region
def plot_co2_by_region():
    st.header("CO₂ Concentrations by Region")
    
    # Regions to display
    regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania']
    
    # Using mock data for demonstration purposes; replace this with real data when available
    region_co2 = [417, 415, 416, 420, 414, 413]  # Mock average CO₂ by region
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(regions, region_co2, color='purple')
    
    # Adjust y-axis to highlight differences
    ax.set_ylim([min(region_co2) - 1, max(region_co2) + 1])
    
    ax.set_title('CO₂ Concentrations by Region', fontsize=14)
    ax.set_xlabel('Region', fontsize=12)
    ax.set_ylabel('CO₂ Concentration (ppm)', fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)


