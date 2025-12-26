# City Street Cleaning Schedule Optimization Analysis
# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Take data from user
# -------------------------------
streets = []
days = []
waste = []

n = int(input("Enter number of cleaning records: "))

for i in range(n):
    print(f"\nRecord {i+1}")
    street = input("Enter Street Name: ")
    day = input("Enter Day (Mon/Wed/Fri): ")
    kg = float(input("Enter Waste Collected (kg): "))
    streets.append(street)
    days.append(day)
    waste.append(kg)

# Create DataFrame
df = pd.DataFrame({
    "Street": streets,
    "Day": days,
    "Waste_Collected_kg": waste
})

print("\nCollected Data:")
print(df)

# -------------------------------
# Step 2: Statistical Analysis
# -------------------------------
print("\nAverage Waste Collected per Street:")
mean_waste = df.groupby("Street")["Waste_Collected_kg"].mean()
print(mean_waste)

print("\nVariance of Waste Collected per Street:")
variance_waste = df.groupby("Street")["Waste_Collected_kg"].var()
print(variance_waste)

# -------------------------------
# Step 3: Line Plot
# -------------------------------
plt.figure()

for street in df["Street"].unique():
    street_data = df[df["Street"] == street]
    plt.plot(
        street_data["Day"],
        street_data["Waste_Collected_kg"],
        marker='o',
        label=f"Street {street}"
    )

plt.xlabel("Day")
plt.ylabel("Waste Collected (kg)")
plt.title("City Street Cleaning Waste Trend")
plt.legend()
plt.show()

# -------------------------------
# Step 4: Schedule Optimization
# -------------------------------
print("\nOptimized Cleaning Schedule:")

for street in mean_waste.index:
    avg = mean_waste[street]

    if avg > 150:
        schedule = "Clean 3 times per week"
    elif avg > 90:
        schedule = "Clean 2 times per week"
    else:
        schedule = "Clean 1 time per week"

    print(f"Street {street}: {schedule}")