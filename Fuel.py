import pandas as pd

Fuel = pd.read_csv("C:\Users\user\OneDrive\Documents\Advanced Willy\Final Data\Presentation\solaregypt\International Energy Agency - Domestic energy production, Egypt, 2021.csv")


# Create a bar chart with the appropriate labels and title
plt.figure(figsize=(10, 6))
plt.bar(Fuel['Domestic energy production, Egypt, 2021'], Fuel['Value'], color=['#ff5733', '#3399ff', '#33cc33', '#ffcc33', '#cc33ff'])
plt.xlabel('Energy Source')
plt.ylabel('Value')
plt.title('Domestic Energy Production in Egypt (2021)')
plt.show()