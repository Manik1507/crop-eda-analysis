# EDA of Crop Generation Patterns in India

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('crop_production_data.csv')  # Replace with actual file name

# Basic overview
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values
df.dropna(inplace=True)

# Most produced crops overall
top_crops = df.groupby('Crop')['Production'].sum().sort_values(ascending=False).head(10)
top_crops.plot(kind='bar', title='Top 10 Produced Crops in India')
plt.xlabel("Crop")
plt.ylabel("Total Production")
plt.show()

# Crop trends over years
crop_trends = df.groupby(['Year', 'Crop'])['Production'].sum().reset_index()
wheat = crop_trends[crop_trends['Crop'] == 'Wheat']
plt.plot(wheat['Year'], wheat['Production'])
plt.title("Wheat Production Over Years")
plt.xlabel("Year")
plt.ylabel("Production")
plt.grid()
plt.show()
