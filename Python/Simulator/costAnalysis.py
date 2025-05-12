import pandas as pd
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Calculating costs based on a pump using 5 kW at max flow (50m3/h)
# Using a 24h simulation completed in 24 minutes. Simulation must be done with 1 minute simulated time per 1 second real time. (boost = 60)

# Load the CSV file into a DataFrame
df = pd.read_csv('Python\Simulator\simLog 24H01-04.csv')

# Get energy prices
with open('Python\EnergyPriceAPI\prices.json', 'r') as json_file:
    priceData = json.load(json_file)
# Extract the time and price data
times = [datetime.fromisoformat(entry['time_start']) for entry in priceData for _ in range(2)]
times = times[1:]
timesLast = times[-1]
times.append(timesLast + timedelta(hours=1))
prices = [entry['NOK_per_kWh'] for entry in priceData for _ in range(2)]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 9))

# Limit plotting to first 24 h
#plotStart = 0
#plotEnd = 1440

# Limit plotting to second 24 h
plotStart = 1442
plotEnd = 1441 * 2

# calculate total energy use and cost
calculationPrices = [entry['NOK_per_kWh'] for entry in priceData for _ in range(60)]
averagePrice = sum(prices)/len(prices)
print("Average price this day = ", round(averagePrice,2), "NOK")

pumpFlowValues = df['Qin'][plotStart:plotEnd].tolist()
averagePumpFlow = sum(pumpFlowValues)/len(pumpFlowValues)
#print("average pump flow = ", round(averagePumpFlow,2))

# calculate total energy use and cost
totalEnergy = 0
totalCost = 0
for i in range(len(pumpFlowValues)):
    pumpPercent = pumpFlowValues[i] * 0.02
    energy = pumpPercent * 5 * (1/60) # 5kW, 1 minute
    cost = energy * calculationPrices[i]
    totalEnergy += energy
    totalCost += cost
totalCost = round(totalCost,2)
print("Energy used:", round(totalEnergy), "kWh, Cost:", totalCost, "NOK")

# theoretical cost if no smart regulation, power use spread evenly accross the day
estimatedCost = round(totalEnergy * averagePrice,2)
print("Estimated cost =", estimatedCost, "NOK")
print("Saved", round(estimatedCost-totalCost,2),"NOK")

# Convert Time (seconds) to Hours:minutes
df['TimeClock'] = pd.to_datetime(df['Time'], unit='s').dt.strftime('%H:%M')

# Plot first subplot
ax1.set_ylim(0,100)
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Qin'][plotStart:plotEnd], label='Flow in [m3/h]', color='orange')
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Qout'][plotStart:plotEnd], label='Flow out [m3/h]', color='black')
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Level'][plotStart:plotEnd], label='Level [%]', color='blue')
xticksToUse = df['TimeClock'][plotStart:plotEnd][::int((plotEnd-plotStart)/24)].tolist()
xticksToUse.append(df['TimeClock'][plotStart:plotEnd].iloc[-1])
ax1.set_xticks(xticksToUse)
ax1.tick_params(axis='x', rotation=45)
ax1.set_title('Flow in and out of the tank')
ax1.set_ylabel('Flow [m3/h] / Level [%]')
ax1.legend()
ax1.grid(True)

# Plot second subplot
ax2.plot(times, prices, marker='', linestyle='-', color='g', label='Electricity prices')
ax2.set_title('Electricity Prices Over Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('NOK per kWh')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()