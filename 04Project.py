# 4.11. Project: Data & Variables

# 4.11.2. Declare and Assign Variables:
date = "Monday 2019-03-18"
time = "10:05:34 AM"
average_astronaut_mass_kg = 80.7
fuel_mass_kg = 760000
ship_mass_kg = 74842.31
fuel_level = 100

# 4.11.3. Collect User Input: 
# Prompt the user for the number of astronauts and the crew status:
num_astronauts = int(input("How many astronauts are in the crew: "))
crew_status = "Ready"

# 4.11.4. Mass Calculations:
total_crew_mass_kg = num_astronauts * average_astronaut_mass_kg
total_ship_mass_kg = total_crew_mass_kg + ship_mass_kg + fuel_mass_kg

# 4.11.5. Generate the Checklist:
line = "-------------------"

print(line, "\n> LAUNCH CHECKLIST\n", line)
print("Date:", date, "\nTime:", time)
print()
print(line, "\n> SHIP INFO\n", line)
print("* Crew:", num_astronauts, 
    "\n* Crew Status:", crew_status, 
    "\n* Fuel Level:", str(fuel_level) + "%")
print()
print(line, "\n> MASS DATA\n", line)
print("* Crew:", total_crew_mass_kg, "kg",
    "\n* Fuel:", fuel_mass_kg, "kg", 
    "\n* Spaceship:", ship_mass_kg, "kg", 
    "\n* Total mass:", total_ship_mass_kg, "kg")