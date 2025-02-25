import json
import requests

# Define the URL with the appropriate parameters
year = "2025"
month = "02"
day = "19"
price_area = "NO2"  # NO2 sør norge
runHours = 5 # for optimalisation

url = f"https://www.hvakosterstrommen.no/api/v1/prices/{year}/{month}-{day}_{price_area}.json"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    try:
        data = response.json()
        # save JSON file
        with open('prices.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Data saved to prices.json")
        #print(data) # print to terminal
    except ValueError:
        print("Response is not in JSON format")
else:
    print(f"Failed to fetch data: {response.status_code}")


# PRICE OPTIMALISATION

# Open prices.json, get the best hours and write to pricesOptimal.json
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