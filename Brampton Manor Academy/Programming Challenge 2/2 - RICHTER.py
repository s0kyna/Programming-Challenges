layout = "{:<20} {:<25} {:<20}"
measurements = [1,5,9.1,9.2,9.5]

# Subprograms
# Joules
def joules(measure):
    Joules = 10**((1.5*measure)+4.8)
    return Joules
# TNT
def tnt(Joules):
    TNT = Joules / (4.184*(10**9))
    return TNT
print(layout.format("Richter","Joules","TNT"))

# Print table
for measure in measurements:
    Joules = joules(measure)
    TNT = tnt(Joules)
    print(layout.format(measure,Joules,TNT))

# Main program
print("\n")
richter_value = float(input("Please enter a Richter scale value: "))
print("Richter value: ",richter_value)
print("Equivalence in joules: ",joules(richter_value))
print("Equivalence in tons of TNT: ",tnt(joules(richter_value)))
