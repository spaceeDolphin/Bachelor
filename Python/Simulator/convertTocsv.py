import pandas as pd

# Load the tab-separated text file into a DataFrame
df = pd.read_csv('Python\Simulator\hb402.txt', delimiter='\t')

# Save the DataFrame to a CSV file
df.to_csv('hb402.csv', index=False)

print("File converted to CSV successfully.")
