import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import os

# Set the correct paths to the database
json_file_path = r'.\database\oco2geos-co2-daygrid-v10r.json'

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
    
    # Updated color to a more vibrant blue for the line
    ax.plot(time_interval, exaggerated_growth_rates, color='#1f77b4', linewidth=2, label='Growth Rate')
    
    ax.set_ylim([-1, 1.25])
    ax.set_title('Exaggerated CO₂ Growth Rate Over Time (2015-2022)', fontsize=16)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Exaggerated Growth Rate (%)', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)  # Add dashed gridlines for a cleaner look
    ax.legend()
    
    plt.tight_layout()
    st.pyplot(fig)

    # Explanation for the first chart
    st.markdown("""
    **Explanation: CO₂ Growth Rate Over Time**
    - **What the data means**: This chart shows how the CO₂ levels have changed in terms of growth rate from 2015 to 2022. The growth rate is exaggerated to emphasize small variations in CO₂ levels.
    - **Is the change good or not?**: A higher CO₂ growth rate is not good, as it indicates that more CO₂ is being released into the atmosphere, contributing to climate change.
    - **What happens when it changes?**: If the growth rate continues to rise, it will lead to higher concentrations of greenhouse gases, which can worsen global warming and climate impacts.
    """)

# Function to plot CO₂ Concentration vs Temperature
def plot_co2_vs_temperature():
    st.header("CO₂ Concentration vs Temperature")
    
    temperature = 15 + (co2_levels - 412) * 0.1  # Mock temperature (in °C)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Scatter plot with larger, more visible markers and gradient coloring
    scatter = ax.scatter(co2_levels, temperature, c=temperature, cmap='coolwarm', s=80, edgecolor='k', alpha=0.75)
    
    ax.set_ylim([min(temperature) - 1, max(temperature) + 1])
    ax.set_title('CO₂ Concentration vs Temperature', fontsize=16)
    ax.set_xlabel('CO₂ Concentration (ppm)', fontsize=12)
    ax.set_ylabel('Temperature (°C)', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Add color bar for the temperature gradient
    fig.colorbar(scatter, ax=ax, label="Temperature (°C)")
    
    plt.tight_layout()
    st.pyplot(fig)

    # Explanation for the second chart
    st.markdown("""
    **Explanation: CO₂ Concentration vs Temperature**
    - **What the data means**: This chart compares the CO₂ concentration (in parts per million) with temperature (in °C). It helps visualize the relationship between rising CO₂ levels and increasing temperatures.
    - **Is the change good or not?**: As CO₂ concentration increases, so does temperature. This is not good, as higher temperatures can lead to negative effects such as heatwaves, droughts, and extreme weather events.
    - **What happens when it changes?**: If CO₂ levels continue to rise, global temperatures will increase, leading to more frequent and severe climate impacts.
    """)

# Function to plot CO₂ levels by region
def plot_co2_by_region():
    st.header("CO₂ Concentrations by Region")
    
    # Regions to display
    regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania']
    
    # Using mock data for demonstration purposes
    region_co2 = [417, 415, 416, 420, 414, 413]  # Mock average CO₂ by region
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Use a modern color palette for the bar chart
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
    ax.bar(regions, region_co2, color=colors, edgecolor='black', linewidth=1.5)
    
    # Adjust y-axis to highlight differences
    ax.set_ylim([min(region_co2) - 1, max(region_co2) + 1])
    
    ax.set_title('CO₂ Concentrations by Region', fontsize=16)
    ax.set_xlabel('Region', fontsize=12)
    ax.set_ylabel('CO₂ Concentration (ppm)', fontsize=12)
    
    ax.grid(True, linestyle='--', alpha=0.7)  # Add dashed gridlines
    plt.tight_layout()
    st.pyplot(fig)

    # Explanation for the third chart
    st.markdown("""
    **Explanation: CO₂ Concentrations by Region**
    - **What the data means**: This bar chart shows the average CO₂ concentrations (in ppm) across different regions. Each region has varying levels of CO₂ concentration due to factors like population density, industrial activity, and land use.
    - **Is the change good or not?**: Higher CO₂ levels in certain regions, such as Asia and North America, are concerning due to their significant contributions to global emissions.
    - **What happens when it changes?**: If CO₂ levels continue to rise in regions with high emissions, it will further contribute to global warming. Efforts to reduce CO₂ in these regions are critical for mitigating climate change.
    """)

# Main function to plot the visualizations
def main():
    plot_co2_growth_rate()
    plot_co2_vs_temperature()
    plot_co2_by_region()

if __name__ == '__main__':
    main()
