import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Python\Simulator\simLog 24H25-03.csv')

# Create a figure with two subplots
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
fig, (ax1) = plt.subplots(1, 1, figsize=(14,8))

# Limit plotting to 24 h
plotStart = 1442
plotEnd = 1441*2

# Convert Time (seconds) to Hours:minutes
df['TimeClock'] = pd.to_datetime(df['Time'], unit='s').dt.strftime('%H:%M')

# Plot Qin and Qout on the first subplot
ax1.set_ylim(0,100)
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Qin'][plotStart:plotEnd], label='Flow in [m3/h]', color='orange')
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Qout'][plotStart:plotEnd], label='Flow out [m3/h]', color='black')
ax1.plot(df['TimeClock'][plotStart:plotEnd], df['Level'][plotStart:plotEnd], label='Level [%]', color='blue')
xticksToUse = df['TimeClock'][plotStart:plotEnd][::int((plotEnd-plotStart)/24)].tolist()
xticksToUse.append(df['TimeClock'][plotStart:plotEnd].iloc[-1])
ax1.set_xticks(xticksToUse)
ax1.tick_params(axis='x', rotation=45)
#ax1.plot(df['Time'], df['Qin'], label='Qin', color='orange')
#ax1.plot(df['Time'], df['Qout'], label='Qout', color='black')
ax1.set_title('Flow in and out of the tank')
#ax1.set_xlabel('Time [s]')
#ax1.set_ylabel('Flow [m3/s]')
ax1.set_ylabel('Flow [m3/h] / Level [%]')
ax1.legend()
ax1.grid(True)

# Plot Level on the second subplot
#ax2.set_ylim(0,100)
#ax2.plot(df['Time'][plotStart:plotEnd], df['Level'][plotStart:plotEnd], label='Level', color='blue')
#ax2.plot(df['Time'][plotStart:plotEnd], df['TargetLevel'][plotStart:plotEnd], label='Target Level', color='red')
#ax2.plot(df['Time'], df['Level'], label='Level', color='blue')
#ax2.plot(df['Time'], df['TargetLevel'], label='Target Level', color='red')
#ax2.set_title('Tank Level')
#ax2.set_xlabel('Time [s]')
#ax2.set_ylabel('Level [%]')
#ax2.legend()
#ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
