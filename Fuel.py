import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set the seaborn style to whitegrid to get a grid with a white background
sns.set(style='whitegrid')

# Read the CSV file
Fuel = pd.read_csv("C:/Users/user/OneDrive/Documents/Advanced Willy/Final Data/Presentation/solaregypt/International Energy Agency - Domestic energy production, Egypt, 2021.csv")

# Create the bar chart with the whitegrid style and remove the spines (the chart frame)
plt.figure(figsize=(10, 6), dpi=300)
barplot = plt.bar(Fuel['Domestic energy production, Egypt, 2021'], Fuel['Value'], color=['#ff5733', '#3399ff', '#33cc33', '#ffcc33', '#cc33ff'])

# Customize the appearance
plt.xlabel('Energy Source')
plt.ylabel('Value')
plt.title('Domestic Energy Production in Egypt (2021)')

# Remove the top and right spines for a clean look
sns.despine(left=False, right=True, top=True)

# Display the plot
plt.show()

