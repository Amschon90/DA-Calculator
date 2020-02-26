import requests,sys,time,os,smtplib

# Secrets
gmailUser = os.environ.get('GMAIL_USER')
gmailPass = os.environ.get('GMAIL_PASS')
apiSecret = os.environ.get('DS_SECRET_KEY')
smsSecret = os.environ.get('SMS_SECRET')

# Hardcoded values, will be removed eventually
trackCoordinates = '33.270568,-111.9710482'
trackAltitude = 1145

def getWeather():
    response = requests.get('https://api.darksky.net/forecast/%s/%s' %(apiSecret,trackCoordinates))
    # Checks if API call was successful
    if not response.ok:
        print('There was an error connecting to Dark Sky.')
        print(response.json())
        sys.exit()
    response = response.json()
    weather = dict()
    # Insert values from API call into dictionary
    weather['airTemp'] = response['currently']['temperature']
    weather['stationPressure'] = response['currently']['pressure']
    weather['dewpointTemp'] = response['currently']['dewPoint']
    return weather

def calculateDA(w):
    # Convert millibar pressure to inHg
    stationPressureinHG = w.get('stationPressure')/33.864
    # Convert F to C
    airTempC = (w.get('airTemp') - 32) * 5/9
    # Simple PA and DA formula
    pressureAltitude = ((29.92 - stationPressureinHG) * 1000) + trackAltitude
    densityAltitude = int((airTempC - (15 + -2 * 1)) * 120 + pressureAltitude)
    return densityAltitude

def sendSMS(msg):
    # Connect to Gmail, send an SMS
    server = smtplib.SMTP( 'smtp.gmail.com',587)
    server.starttls()
    server.login(gmailUser,gmailPass)
    print(gmailUser,smsSecret,myMessage) # This line prints what goes into the SMS
    # Keep below line commented out to prevent text from being sent
    #server.sendmail(gmailUser,smsSecret,myMessage)

# Makes call to API to get the weather at the track
trackWeather = getWeather()

# Calulate DA, compose message, and then send it
myMessage = 'Current DA for WHP is %s' %(calculateDA(trackWeather))
sendSMS(myMessage)