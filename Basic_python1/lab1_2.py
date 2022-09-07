import math

def f():
    print(" *** Wind classification ***")
    wind_speed = float(input("Enter wind speed (km/h) : "))
    if(wind_speed>=0 and wind_speed<=51.99):
        wc = "Breeze"
    elif(wind_speed>=52.00 and wind_speed <= 55.99):
        wc = "Depression"
    elif(wind_speed >= 56.00 and wind_speed <= 101.99):
        wc = "Tropical Storm"
    elif(wind_speed >= 102.00 and wind_speed <= 208.99):
        wc = "Typhoon"
    elif(wind_speed >= 209.00):
        wc = "Super Typhoon"
    print("Wind classification is",wc,end=("."))

f()