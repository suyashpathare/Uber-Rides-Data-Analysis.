import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/charts", exist_ok=True)

df = pd.read_csv("data/uber_rides.csv")

df.drop_duplicates(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Hour'] = df['Date'].dt.hour

# Peak Hour Analysis
hourly_rides = df.groupby('Hour').size()

plt.figure()
plt.bar(hourly_rides.index, hourly_rides.values)
plt.title("Rides per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Rides")
plt.savefig("outputs/charts/rides_per_hour.png")
plt.close()

# Ride Category Distribution
plt.figure()
df['Category'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Ride Category Distribution")
plt.ylabel("")
plt.savefig("outputs/charts/ride_category_distribution.png")
plt.close()

total_revenue = df['Fare'].sum()
print("Total Revenue:", total_revenue)

print("Analysis Completed Successfully!")
