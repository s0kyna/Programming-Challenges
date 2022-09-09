layout = "{:<20} {:<25} {:<20}"
measurements = [1,5,9.1,9.2,9.5]

# Subprograms
# Joules
def getjoules(measurement):
    Joules = 10**((1.5*measurement)+4.8)
    return Joules
# TNT
def gettnt(Joules):
    TNT = Joules / (4.184*(10**9))
    return TNT
print(layout.format("Richter","Joules","TNT"))

# Print table
for measurement in measurements:
    Joules = joules(measurement)
    TNT = tnt(Joules)
    print(layout.format(measurement,Joules,TNT))

# Main program
print("\n")
richter_value = float(input("Please enter a Richter scale value: "))
print("Richter value: ",richter_value)
print("Equivalence in joules: ",joules(richter_value))
print("Equivalence in tons of TNT: ",tnt(joules(richter_value)))
