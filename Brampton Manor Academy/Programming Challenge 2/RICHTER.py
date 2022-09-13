measurements = [1,5,9.1,9.2,9.5]

# Subprograms
# Joules calculation
def getjoules(measurement):
    joules = 10**((1.5*measurement)+4.8)
    return joules
# TNT calculation
def gettnt(joules):
    tnt = joules / (4.184*(10**9))
    return tnt
print(f"{'Richter':<20}{'Joules':<25}{'TNT':<20}")

# Print table
for measurement in measurements:
    joules = getjoules(measurement)
    tnt = gettnt(joules)
    print(f"{measurement:<20}{joules:<25}{tnt:<20}")

# Main program
print("\n")
richter_value = float(input("Please enter a Richter scale value: "))
print("Richter value: ",richter_value,
      "\nEquivalence in joules: ",getjoules(richter_value),
      "\nEquivalence in tons of TNT: ",gettnt(getjoules(richter_value)))
