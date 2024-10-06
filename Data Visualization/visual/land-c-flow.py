import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Database file path (for reference)
database_path = r".\\database\\micasa-carbonflux-daygrid-v1.json"

# 1. Carbon Flux Over Time (Line Chart)
def plot_carbon_flux_over_time():
    time_data = list(range(2001, 2024))  # Years from 2001 to 2023
    carbon_flux = [3.2, 3.1, 3.5, 3.3, 3.6, 3.9, 4.1, 4.0, 4.3, 4.2, 4.5, 4.7, 4.8, 5.0, 5.1, 5.3, 5.4, 5.5, 5.6, 5.8, 6.0, 6.2, 6.4]  # Simulated data

    # Line chart for Carbon Flux Over Time
    st.header("Carbon Flux Over Time (2001-2023)")
    plt.figure(figsize=(10, 6))

    # Use vibrant colors with modern aesthetics
    plt.plot(time_data, carbon_flux, marker="o", linestyle="-", color="#1f77b4", label="Carbon Flux")
    plt.fill_between(time_data, carbon_flux, color="#aec7e8", alpha=0.5)  # Fill area under the line

    plt.title("Carbon Flux Over Time (2001-2023)", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Carbon Flux (Grams per square meter per day)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)  # Dashed gridlines for a modern look
    plt.xticks(time_data, rotation=45)
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the first chart
    st.markdown("""
    **Explanation: Carbon Flux Over Time**
    - **What the data means**: The chart shows how carbon flux, which is the amount of carbon exchanged between the land and the atmosphere, changes from 2001 to 2023.
    - **Is the change good or not?**: An increase in carbon flux might indicate higher carbon emissions, which is generally bad for climate change. On the other hand, stable or decreasing flux can be a sign of better carbon sequestration, which is positive for the environment.
    - **What happens when it changes**: If carbon flux increases, more carbon is being released into the atmosphere, worsening climate change. A decrease indicates a stronger ability of ecosystems to absorb carbon, which helps mitigate climate impacts.
    """)

# 2. Carbon Sources (Pie Chart)
def plot_carbon_sources():
    sources = ["Wildfires", "Fuel Wood", "Heterotrophic Respiration", "Net Ecosystem Exchange"]
    emissions = [25, 15, 40, 20]  # Simulated percentage data

    # Pie chart for Carbon Sources
    st.header("Contribution of Carbon Sources to Emissions")

    # Use vibrant, modern colors
    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
    plt.figure(figsize=(8, 8))
    plt.pie(emissions, labels=sources, autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

    plt.title("Contribution of Carbon Sources to Emissions", fontsize=16)
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the second chart
    st.markdown("""
    **Explanation: Contribution of Carbon Sources to Emissions**
    - **What the data means**: This pie chart shows the relative contribution of various carbon sources to overall emissions.
    - **Is the change good or not?**: Higher contributions from sources like wildfires or fuel wood suggest natural and human-driven activities are releasing significant amounts of carbon. A higher contribution from heterotrophic respiration (from organisms breaking down organic matter) might be natural but could increase under warmer conditions.
    - **What happens when it changes**: If wildfires increase, more carbon is released into the atmosphere, exacerbating climate change. An increase in net ecosystem exchange indicates higher carbon storage capacity, which is a good sign for climate stabilization.
    """)

# 3. Carbon Flux by Region (Bar Chart)
def plot_carbon_flux_by_region():
    regions = ["North America", "South America", "Europe", "Asia", "Africa", "Australia"]
    flux_values = [3.5, 4.1, 2.7, 5.0, 3.9, 2.0]  # Simulated values

    # Bar chart for Carbon Flux by Region
    st.header("Carbon Flux by Region")
    plt.figure(figsize=(10, 6))

    # Use a gradient color palette for the bars
    colors = ["#5dade2", "#48c9b0", "#f7dc6f", "#f1948a", "#af7ac5", "#aed6f1"]
    plt.barh(regions, flux_values, color=colors, edgecolor='black', linewidth=1.5)

    plt.title("Carbon Flux by Region", fontsize=16)
    plt.xlabel("Carbon Flux (Grams per square meter per day)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the third chart
    st.markdown("""
    **Explanation: Carbon Flux by Region**
    - **What the data means**: This bar chart highlights how different regions contribute to the global carbon flux.
    - **Is the change good or not?**: Higher flux in regions like Asia or South America could indicate deforestation, agricultural expansion, or industrial activities releasing more carbon. Lower flux in regions like Europe or Australia suggests either better land management practices or less carbon exchange.
    - **What happens when it changes**: If carbon flux increases in a region, it may suggest higher emissions or less carbon sequestration. A decrease indicates improvements in managing carbon sources and sinks.
    """)

# 4. Impact of Wildfires Over Time (Area Chart)
def plot_impact_of_wildfires():
    time_data = list(range(2001, 2024))
    wildfire_flux = [0.5, 0.7, 0.6, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 1.7, 1.9, 2.0, 2.1, 2.2, 2.3, 2.5, 2.6, 2.8, 3.0, 3.2, 3.3, 3.4]  # Simulated data

    # Area chart for Impact of Wildfires Over Time
    st.header("Impact of Wildfires on Carbon Flux Over Time")
    plt.figure(figsize=(10, 6))

    # Use a brighter, eye-catching orange color
    plt.fill_between(time_data, wildfire_flux, color="#ff7f0e", alpha=0.5)
    plt.plot(time_data, wildfire_flux, color="#ff7f0e", marker="o", linestyle="-", label="Wildfire Impact")

    plt.title("Impact of Wildfires on Carbon Flux Over Time", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Carbon Flux from Wildfires (Grams per square meter per day)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the fourth chart
    st.markdown("""
    **Explanation: Impact of Wildfires on Carbon Flux**
    - **What the data means**: This area chart shows how wildfires have contributed to carbon flux over time, releasing large amounts of carbon into the atmosphere.
    - **Is the change good or not?**: An increasing trend in wildfire-related carbon flux is concerning, as it indicates more frequent or intense fires contributing to higher carbon emissions.
    - **What happens when it changes**: As wildfires become more frequent, they release more carbon, weakening the ability of forests and other ecosystems to act as carbon sinks. This exacerbates global warming.
    """)

# Main function to call all the plots
def plot_land_carbon_flow():
    plot_carbon_flux_over_time()
    plot_carbon_sources()
    plot_carbon_flux_by_region()
    plot_impact_of_wildfires()

