# Gets input from user

rods = float(input("Input rods: "))
print("You input",rods,"rods.")


# Conversions
# Meters
def meters(rods):
    Meters = rods* 5.0292
    print("Meters:",Meters)

#Feet  
def feet(rods):
    Feet = (rods*5.0292)/0.3048
    print("Feet:",Feet)

# Miles  
def miles(rods):
    Miles = (rods*5.0292)/1609.34
    print("Miles:",Miles)

# Furlongs
def furlongs(rods):
    Furlongs = rods/40
    print("Furlongs:",Furlongs)

# Minutes to walk x rods
def minutes(rods):
    miles = (rods*5.0292)/1609.34
    minutes = (miles / 3.1)*60
    print("Minute to walk",rods,"rods:",minutes)

# Main program
print("\nConversions")
meters(rods)
feet(rods)
miles(rods)
furlongs(rods)
minutes(rods)
