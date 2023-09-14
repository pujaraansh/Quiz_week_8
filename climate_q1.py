import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Fetch the required values (assuming table and column names; you should replace them with actual names)
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
data = cursor.fetchall()

# Close the database connection
conn.close()

# Populate the Python lists with the fetched values
years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

# Plotting the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

# Save the figure before displaying it
plt.savefig("co2_temp_1.png")
plt.show()
