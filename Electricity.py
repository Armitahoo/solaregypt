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


# Read the CSV file
df = pd.read_csv('International Energy Agency - Domestic energy production, Egypt, 2021.csv')

# Plot
plt.figure(figsize=(10, 6), dpi=300)
plt.bar(df['Domestic energy production, Egypt, 2021'], df['Value'], color='skyblue')

plt.xlabel('Type')
plt.ylabel('Energy Production (TJ)')
plt.title('Domestic Electricity generation in Egypt (2021)')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Read the CSV file for domestic energy production
df_domestic_energy = pd.read_csv('International Energy Agency - Domestic energy production, Egypt, 2021.csv')

# Plot the bar chart for domestic energy production
plt.figure(figsize=(10, 6), dpi=300)
plt.bar(df_domestic_energy['Domestic energy production, Egypt, 2021'], df_domestic_energy['Value'], color='skyblue')

plt.xlabel('Type')
plt.ylabel('Energy Production (TJ)')
plt.title('Domestic Electricity Generation in Egypt (2021)')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Read the CSV file for per capita electricity source
df_per_capita = pd.read_csv('C:/Users/user/OneDrive/Documents/Advanced Willy/Final Data/Presentation/solaregypt/per-capita-electricity-source-stacked.csv')

# Filter data for Egypt
df_per_capita_egypt = df_per_capita[df_per_capita['Entity'] == 'Egypt']

# Plot the bar chart for per capita electricity source
plt.figure(figsize=(12, 6), dpi=300)
plt.bar(df_per_capita_egypt['Year'], df_per_capita_egypt.iloc[:, 2:].sum(axis=1), color='skyblue')

plt.xlabel('Year')
plt.ylabel('Per Capita Electricity (kWh)')
plt.title('Per Capita Electricity Source in Egypt')
plt.tight_layout()
plt.show()
