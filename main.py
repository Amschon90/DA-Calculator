import requests,time

# Determine the location we want to race at.
    # Wild Horse Pass Motorsports Park - Chandler, AZ
trackAltitude = 1145 #dummy value

# Get the local weather data.
    # API Call to Weather Site
response = requests.get('https://api.darksky.net/forecast/85b406747dd735450a89f10a52b8f4fa/33.270568,-111.9710482')

if not response.ok:
    print(response.json())

response = response.json()

# Add that data to variables.
airTemp = response['currently']['temperature']
stationPressure = response['currently']['pressure']
dewpointTemp = response['currently']['dewPoint'] # not currently used

print(airTemp)
print(stationPressure)
print(dewpointTemp)

# Convert millibar pressure to inHg
stationPressure = stationPressure/33.864
print (stationPressure)

# Convert F to C
airTemp = (airTemp - 32) * 5/9
print(airTemp)

# Simple DA formula
pressureAltitude = ((29.92 - stationPressure) * 1000) + trackAltitude
print(pressureAltitude)

densityAltitude = (airTemp - (15 + -2 * 1)) * 120 + pressureAltitude
print(densityAltitude)

# Send an SMS with that information.

# Include current estimated horsepower gain