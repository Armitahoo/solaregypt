import pandas as pd
import matplotlib.pyplot as plt

# Read the data
Energy_data = pd.read_csv("C:/Users/user/OneDrive/Documents/Advanced Willy/Final Data/Presentation/solaregypt/owid-energy-data.csv")

# Filter data for Egypt
egypt_data = Energy_data.loc[Energy_data['country'] == 'Egypt', ['year', 'electricity_demand', 'electricity_generation', 'electricity_share_energy', 'per_capita_electricity']]

# Filter years between 2000 and 2023
egypt_data = egypt_data[(egypt_data['year'] >= 2000) & (egypt_data['year'] < 2023)]

# Drop rows with missing values (NaN)
egypt_data.dropna(inplace=True)

# Create pivot table for the specified columns
new_pivot = egypt_data.pivot_table(values=['electricity_demand', 'electricity_generation', 'electricity_share_energy', 'per_capita_electricity'], index='year', aggfunc='sum')



# Plot the electricity demand per capita
plt.figure(figsize=(12, 6), dpi=300)
plt.plot(egypt_data['year'], egypt_data['per_capita_electricity'], marker='o', color='blue', linewidth=2)
plt.title('Electricity Demand per Capita in Egypt (2000-2022)')
plt.xlabel('Year')
plt.ylabel('Electricity Demand per Capita (kWh)')
plt.grid(True)
plt.tight_layout()
plt.show()