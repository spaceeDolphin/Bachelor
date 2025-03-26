import json
import matplotlib.pyplot as plt
from datetime import datetime

# Load the JSON data from the file
with open('Python\EnergyPriceAPI\prices.json', 'r') as json_file:
    data = json.load(json_file)
#with open('Python\EnergyPriceAPI\pricesOptimal.json', 'r') as json_file:
#    bestHours = json.load(json_file)

# Extract the time and price data
times = [datetime.fromisoformat(entry['time_start']) for entry in data]
#timesBest = [datetime.fromisoformat(entry['time_start']) for entry in bestHours]
prices = [entry['NOK_per_kWh'] for entry in data]
#pricesBest = [entry['NOK_per_kWh'] for entry in bestHours]

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(times, prices, marker='o', linestyle='-', color='b', label='Electricity prices')
#plt.plot(timesBest, pricesBest, marker='o', linestyle='', color='r', label='Best run hours')
plt.xlabel('Time')
plt.ylabel('NOK per kWh')
plt.title('Electricity Prices Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
