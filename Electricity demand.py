import pandas as pd

# Read the original CSV data
original_csv_path = "C:\Users\user\OneDrive\Documents\Advanced Willy\Final Data\Presentation\solaregypt\per-capita-electricity-source-stacked.csv"
data = pd.read_csv(original_csv_path)

# Filter the data for Egypt from 2000 to 2021
egypt_2000_2021 = data[(data['Entity'] == 'Egypt') & (data['Year'].between(2000, 2021))]

# Save the filtered data to a new CSV file
egypt_2000_2021.to_csv("Egypt 2000-2021" index=False)

