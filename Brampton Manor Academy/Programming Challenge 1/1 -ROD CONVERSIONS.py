# Gets input from user

# Conversions
# Meters
def meters(rods):
    Meters = rods* 5.0292
    return Meters

#Feet  
def feet(rods):
    Feet = (rods*5.0292)/0.3048
    return Feet

# Miles  
def miles(rods):
    Miles = (rods*5.0292)/1609.34
    return Miles

# Furlongs
def furlongs(rods):
    Furlongs = rods/40
    return Furlongs

# Minutes to walk x rods
def minutes(rods):
    miles = (rods*5.0292)/1609.34
    minutes = (miles / 3.1)*60
    return minutes

# Run
def run():
    rods = float(input("Input rods: "))
    print("You input",rods,"rods.")
    print("\nConversions")
    print("Meters:",meters(rods))
    print("Feet:",feet(rods))
    print("Miles:",miles(rods))
    print("Furlongs:",furlongs(rods))
    print("Minute to walk",rods,"rods:",minutes(rods))
    
# Main program
if __name__ == '__main__':
    run()
