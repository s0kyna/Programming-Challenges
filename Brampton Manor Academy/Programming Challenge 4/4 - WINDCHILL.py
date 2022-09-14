# 4 - WIND CHILL

# Calculation
def wind_chill(air_temp,air_speed):
    wind_chill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return wind_chill

# Run
def run():
    print("Temperature of 10 and speed of 15 gives windchill of:",wind_chill(10,15))
    print("Temperature of 0 and speed of 25 gives windchill of:",wind_chill(0,25))
    print("Temperature of -10 and speed of 35 gives windchill of:",wind_chill(-10,35))
    air_temp = float(input("Temperature: "))
    air_speed = float(input("Speed: "))
    print("Windchill: ",wind_chill(air_temp,air_speed))

if __name__ == '__main__':
    run()
