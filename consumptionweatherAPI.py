import pyowm  #must be installed before by using $ pip install pyowm

owm = pyowm.OWM('API key')  # To have a key you need to be registered here https://openweathermap.org

# Current weather in Montreal
print('Current weather in Montreal, CA')
observation = owm.weather_at_place('Montreal,CA')
weather = observation.get_weather()
print(weather)                      
                              

# Weather details
print('Wind ' + str(weather.get_wind()))                  
print('Humidity ' + str(weather.get_humidity()))              
print('Temperature ' + str(weather.get_temperature('celsius')))  
