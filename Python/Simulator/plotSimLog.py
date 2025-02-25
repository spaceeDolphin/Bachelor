import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Python\Simulator\simLog.csv')

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Plot Qin and Qout on the first subplot
ax1.plot(df['Time'], df['Qin'], label='Qin', color='orange')
ax1.plot(df['Time'], df['Qout'], label='Qout', color='black')
ax1.set_title('Flow in and out of the tank')
#ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Flow [m3/s]')
ax1.legend()
ax1.grid(True)

# Plot Level on the second subplot
ax2.plot(df['Time'], df['Level'], label='Level', color='blue')
ax2.plot(df['Time'], df['TargetLevel'], label='Target Level', color='red')
ax2.set_title('Tank Level')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Level [%]')
ax2.legend()
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
