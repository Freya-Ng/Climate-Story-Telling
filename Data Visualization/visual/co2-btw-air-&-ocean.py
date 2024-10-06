import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Database file path (for reference)
database_path = r".\\database\\eccodarwin-co2flux-monthgrid-v5.json"

# Simulated CO₂ Flux Data for Multiple Years (2020, 2021, 2022)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
flux_2020 = np.sin(np.linspace(0, 3, 12)) * 0.0005  # Simulated CO₂ flux for 2020
flux_2021 = np.sin(np.linspace(0, 3, 12) + 0.5) * 0.0006  # Simulated CO₂ flux for 2021
flux_2022 = np.sin(np.linspace(0, 3, 12) + 1) * 0.0007  # Simulated CO₂ flux for 2022

# Function to plot the CO₂ Flux Visualizations
def plot_co2_flux_visualization():
    # 1. CO₂ Flux Over Time (Line Chart)
    st.header("CO₂ Flux Over Time (2020-2022)")
    plt.figure(figsize=(10, 6))
    
    # Use more vibrant colors
    plt.plot(months, flux_2020, marker="o", linestyle="-", color="#1f77b4", label="2020")  # Blue
    plt.plot(months, flux_2021, marker="o", linestyle="-", color="#ff7f0e", label="2021")  # Orange
    plt.plot(months, flux_2022, marker="o", linestyle="-", color="#2ca02c", label="2022")  # Green
    
    plt.title("CO₂ Flux Over Time (2020-2022)", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("CO₂ Flux (mmol/m²/s)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the first chart
    st.markdown("""
    **Explanation: CO₂ Flux Over Time (2020-2022)**
    - **What the data means**: This chart shows the seasonal changes in CO₂ flux (in mmol/m²/s) from 2020 to 2022. CO₂ flux represents the exchange of carbon dioxide between the atmosphere and the ocean.
    - **Is the change good or not?**: Fluctuations are expected due to seasonal variations. However, if the overall trend shows increasing release (positive flux), it could indicate rising CO₂ emissions, which is bad for the environment.
    - **What happens when it changes?**: If CO₂ release continues to rise, more carbon will be released into the atmosphere, contributing to climate change. Stabilizing or increasing absorption would be beneficial for reducing atmospheric CO₂.
    """)

    # 2. CO₂ Absorption vs. Release (Pie Chart)
    st.header("CO₂ Absorption vs. Release (2020-2022)")
    absorption_total = 70  # Simulated % of time the ocean absorbs CO₂
    release_total = 30  # Simulated % of time the ocean releases CO₂
    
    # Use a more modern color palette for the pie chart
    colors = ["#17becf", "#d62728"]  # Cyan for absorption, Red for release
    plt.figure(figsize=(8, 8))
    plt.pie([absorption_total, release_total], labels=["Absorption", "Release"], autopct='%1.1f%%', 
            colors=colors, startangle=90, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
    plt.title("CO₂ Absorption vs. Release (2020-2022)", fontsize=16)
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the second chart
    st.markdown("""
    **Explanation: CO₂ Absorption vs. Release (2020-2022)**
    - **What the data means**: This pie chart compares the percentage of time the ocean absorbs CO₂ (70%) versus the time it releases CO₂ (30%) between 2020 and 2022.
    - **Is the change good or not?**: Higher absorption percentages are good because it means the ocean is acting as a carbon sink, removing CO₂ from the atmosphere. More release would be harmful, as it contributes to the greenhouse effect.
    - **What happens when it changes?**: If the ocean's ability to absorb CO₂ weakens and release increases, more CO₂ will remain in the atmosphere, accelerating climate change and causing ocean acidification.
    """)

    # 3. Comparison of CO₂ Flux Between Years (Grouped Bar Chart)
    st.header("Comparison of CO₂ Flux Between Years")
    width = 0.2  # Bar width for grouping
    x = np.arange(len(months))  # Label locations
    
    # Vibrant colors for the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(x - width, flux_2020, width, label='2020', color="#1f77b4")  # Blue
    plt.bar(x, flux_2021, width, label='2021', color="#ff7f0e")  # Orange
    plt.bar(x + width, flux_2022, width, label='2022', color="#2ca02c")  # Green
    
    plt.title("Comparison of CO₂ Flux Between Years", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("CO₂ Flux (mmol/m²/s)", fontsize=12)
    plt.xticks(x, months)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

    # Explanation for the third chart
    st.markdown("""
    **Explanation: Comparison of CO₂ Flux Between Years**
    - **What the data means**: This chart compares CO₂ flux between 2020, 2021, and 2022, showing how carbon exchange has changed across months for each year.
    - **Is the change good or not?**: Significant increases in positive flux (CO₂ release) would not be good, as it indicates higher levels of CO₂ being emitted into the atmosphere. Stabilized or increased negative flux (absorption) is beneficial for reducing CO₂.
    - **What happens when it changes?**: If the trend shows increasing release over time, it signals a need for more robust climate action. If absorption improves, the ocean is helping mitigate climate change by reducing atmospheric CO₂ levels.
    """)
