# Determine the location we want to race at.
    # Wild Horse Pass Motorsports Park - Chandler, AZ
altitude = 0 #dummy value

# Get the local weather data.
    # API Call to Weather Site
    #https://api.darksky.net/forecast/85b406747dd735450a89f10a52b8f4fa/33.270568,-111.9710482

# Add that data to variables.

# Calculate the DA.
# Values needed to start calculations - will eventually come from API, currently test data
airTemp = 62.2
stationPressure = 1016.9
dewpointTemp = 45.78

#convert to Kelvin
airTemp = (airTemp - 32) * 5/9 + 273.15
print('temp in kelvin %s' %airTemp)

#convert to Celsius
dewpointTemp = (dewpointTemp - 32) * 5/9
print('dp in celc %s' %dewpointTemp)

vaporPressure = 6.11 * (10 * ((7.5 * dewpointTemp)/(237.7 + dewpointTemp)))
print('vapor pressure %s' %vaporPressure)
virtualTemp = airTemp/(1-(vaporPressure/stationPressure)*(1-0.622))
print('virtual temp %s' %virtualTemp)

#convert to Rankine
virtualTemp = virtualTemp * 1.8

#convert to inHG
stationPressure = stationPressure / 33.864

# finally
densityAltitude = 145366 * (1-((17.326 * stationPressure)/virtualTemp)**0.235)

print(densityAltitude)

# Send an SMS with that information.