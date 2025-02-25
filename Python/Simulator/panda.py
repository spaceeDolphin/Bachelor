import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv('Python\Simulator\hb402.csv')

# The number you want to find the closest match for
target_number = 50000

# Find the closest number in column 1
closest_index = (np.abs(df.iloc[:, 0] - target_number)).idxmin()

# Retrieve the corresponding value from column 2
closest_value = df.iloc[closest_index, 1]

print(f"The closest number to {target_number} in column 1 is {df.iloc[closest_index, 0]}")
print(f"The corresponding value in column 2 is {closest_value}")
