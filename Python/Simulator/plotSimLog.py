import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Python\Simulator\simLog 24H25-03.csv')

# Create a figure with one subplot
fig, (ax1) = plt.subplots(1, 1, figsize=(14,8))

# Limit plotting to first 24 h
plotStart = 0
plotEnd = 1440

# Limit plotting to second 24 h
#plotStart = 1442
#plotEnd = 1441 * 2

# Convert Time (seconds) to Hours:minutes
df['TimeClock'] = pd.to_datetime(df['Time'], unit='s').dt.strftime('%H:%M')

# Create plot
ax1.set_ylim(0,100)

ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Qin'][plotStart:plotEnd], label='Flow in [m3/h]', color='orange')
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Qout'][plotStart:plotEnd], label='Flow out [m3/h]', color='black')
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Level'][plotStart:plotEnd], label='Level [%]', color='blue')

# Config x-axis (time)
xticksToUse = df['TimeClock'][plotStart:plotEnd][::int((plotEnd-plotStart)/24)].tolist()
xticksToUse.append(df['TimeClock'][plotStart:plotEnd].iloc[-1])
ax1.set_xticks(xticksToUse)
ax1.tick_params(axis='x', rotation=45)

ax1.set_title('Flow in and out of the tank')
ax1.set_ylabel('Flow [m3/h] / Level [%]')
ax1.legend()
ax1.grid(True)

plt.tight_layout()
plt.show()
