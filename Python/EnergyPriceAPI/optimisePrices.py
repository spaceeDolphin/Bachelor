# SCRIPT INTEGRATED IN stromprisAPI.py

import json

# Open prices.json, get the best hours and write to pricesOptimal.json

runHours = 5

# Load the JSON data from the file
with open('prices.json', 'r') as json_file:
    data = json.load(json_file)

# Sort the data by NOK_per_kWh
sorted_data = sorted(data, key=lambda x: x['NOK_per_kWh'])

# Select the top entries with the lowest NOK_per_kWh
top_entries = sorted_data[:runHours]

# Save the modified data to a new JSON file
with open('pricesOptimal.json', 'w') as json_file:
    json.dump(top_entries, json_file, indent=4)

print("Best entries saved to pricesOptimal.json")
