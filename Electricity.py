# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:47:23 2024

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
Energy_data = pd.read_csv("C:/Users/user/OneDrive/Documents/Advanced Willy/Final Data/Presentation/solaregypt/owid-energy-data.csv")

# Filter data for Egypt
egypt_data = Energy_data.loc[Energy_data['country'] == 'Egypt', ['year', 'biofuel_electricity', 'coal_electricity', 'gas_electricity', 'hydro_electricity', 
                       'nuclear_electricity', 'oil_electricity', 'other_renewable_electricity', 
                       'solar_electricity', 'wind_electricity']]

# Filter years between 2000 and 2023
egypt_data = egypt_data[(egypt_data['year'] >= 2000) & (egypt_data['year'] < 2023)]

# Drop rows with missing values (NaN)
egypt_data.dropna(inplace=True)

# Create pivot table
Pivot = egypt_data.pivot_table(values=["biofuel_electricity", "coal_electricity", "gas_electricity", "hydro_electricity", 
                       "nuclear_electricity", "oil_electricity", "other_renewable_electricity", 
                       "solar_electricity", "wind_electricity"], index='year', aggfunc='sum')

# Plot the pivot table
plt.figure(figsize=(12, 6), dpi=300)
for column in Pivot.columns:
    plt.plot(Pivot.index, Pivot[column], marker='o', label=column)

plt.title('Electricity Generation by Fuel Type in Egypt (2000-2022)')
plt.xlabel('Year')
plt.ylabel('Electricity Generation (GWh)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

