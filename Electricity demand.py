import pandas as pd

# Read the data
Energy_data = pd.read_csv("C:/Users/user/OneDrive/Documents/Advanced Willy/GitHub/Final/owid-energy-data.csv")

# Filter data for Egypt
egypt_data = Energy_data.loc[Energy_data['country'] == 'Egypt', ['year', 'electricity_demand', 'electricity_generation', 'electricity_share_energy', 'per_capita_electricity']]

# Filter years between 2000 and 2023
egypt_data = egypt_data[(egypt_data['year'] >= 2000) & (egypt_data['year'] < 2023)]

# Drop rows with missing values (NaN)
egypt_data.dropna(inplace=True)

# Create pivot table
Pivot = egypt_data.pivot_table(values=['electricity_demand', 'electricity_generation', 'electricity_share_energy', 'per_capita_electricity'], index='year', aggfunc='sum')

print(Pivot)
