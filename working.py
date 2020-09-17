import datetime
import csv
from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd
import os
import json, requests, sys


"""
quickWeather.py - Prints the weather for a location from the command line.
A program from Automate the Boring Stuff
I reworked it so that it finds the weather from the location assigned to the
location variable.   The code for running the program from the command line is
commented out.   
"""





w=[]
cities = []


input_string = input("Enter a list elements separated by space ")

print("\n")
cities = input_string.split(',')
print("RRRRRRRRRRRRRR", cities)
print("user list is ", cities)

header = ("City","Weather","Temperature", "Humidity","Date")
City_data = 'afgweather.csv'
"""for i in range(1,5):
    global location
    location=(input("Enter City Name :"))
    cities.append(location)
"""




"""a=[]
a= input("Enter a two value: ").split()

print(a)
  """
for city in cities:
    
    
   

    # Download the JSON data from OpenWeatherMap.org's API.
    url ='http://api.openweathermap.org/data/2.5/forecast/?q={}&appid={}'.format(city,'8d195f72c65049d55c801a702f095e96')
    print("\n\n         ",city,"\n\n            ")
    response = requests.get(url)
    # print(response)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    weatherData = json.loads(response.text)


    temp=weatherData['list'][0]['main']['temp']
    humidity=weatherData['list'][1]['main']['humidity']

    print('Current weather in %s:' % (city))
    print("Temp",temp)
    print("humidity",humidity)
    #print("Temperature   :  ",weatherData['list'][0]['main']['temp'])
    #print("Humidity   :  " ,weatherData['list'][1]['main']['humidity'])
    
    w = weatherData['list']

    
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
    print()
    print('Day after the day after tomorrow:')
    print(w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
    print()
    print('Day after the day after tomorrow the day after:')
    print(w[4]['weather'][0]['main'], '-', w[4]['weather'][0]['description'])
    print()
    print('Day after the day after tomorrow the day after the day after:')
    print(w[5]['weather'][0]['main'], '-', w[5]['weather'][0]['description'])
    
    #City_data = 'weatherApp.csv'
    tomorrow_database7=[]
    name7='City : %s:' % (city)
    tomorrow7=""
    temp7=""
    humidity7=""
    dt7=""
    condition7=[name7,tomorrow7,temp7,humidity7,dt7]
    for value in condition7:
        data=value
        tomorrow_database7.append(data)


    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows([tomorrow_database7])










    name='%s:' % (city)
    weather=w[0]['weather'][0]['description']
    Temperature=temp
    humidity=humidity
    date=datetime.datetime.now().strftime("%d-%m-%Y")

    condition=[name,weather,Temperature,humidity,date]
    contacts_database = []
    tomorrow_database=[]
    tomorrow_database2=[]
    tomorrow_Database3=[]
    tomorrow_database4=[]



    for value in condition:
        print(value)
        data = value
        contacts_database.append(data)
    
    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        # writer.writerow()
        writer.writerows([contacts_database])
    
    
    name='%s:' % (city)
    tomorrow=w[1]['weather'][0]['description']
    temp=weatherData['list'][1]['main']['temp']
    humidity=weatherData['list'][1]['main']['humidity']
    dt1=datetime.date.today() + datetime.timedelta(days=1)
    condition1=[name,tomorrow,temp,humidity,dt1]
    for value in condition1:
        data=value
        tomorrow_database.append(data)


    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
       # writer.writerow(header)
        writer.writerows([tomorrow_database])

    #print('Day after tomorrow:')
    print(w[2]['weather'][0]['description'])
    name2='%s:'%  (city)
    tomorrow2=w[2]['weather'][0]['description']
    temp2=weatherData['list'][2]['main']['temp']
    humidity2=weatherData['list'][2]['main']['humidity']
    dt2=datetime.date.today() + datetime.timedelta(days=2)
    condition2=[name2,tomorrow2,temp2,humidity2,dt2]
    for value in condition2:
        data=value
        tomorrow_database2.append(data)


    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerows([tomorrow_database2])

    #print('Day after the day after tomorrow:')
    print(w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
    name3='%s:' % (city)
    tomorrow3=w[3]['weather'][0]['description']
    temp3=weatherData['list'][3]['main']['temp']
    humidity3=weatherData['list'][3]['main']['humidity']
    dt3=datetime.date.today() + datetime.timedelta(days=3)
    condition3=[name3,tomorrow3,temp3,humidity3,dt3]
    for value in condition3:
        data=value
        tomorrow_Database3.append(data)


    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerows([tomorrow_Database3])
    
    name4='%s' % (city)
    tomorrow4=w[4]['weather'][0]['description']
    temp4=weatherData['list'][4]['main']['temp']
    humidity4=weatherData['list'][4]['main']['humidity']
    dt4=datetime.date.today() + datetime.timedelta(days=4)
    condition4=[name4,tomorrow4,temp4,humidity4,dt4]
    for value in condition4:
        data=value
        tomorrow_database4.append(data)


    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerows([tomorrow_database4])
    
    tomorrow_database5=[]
    name5=""
    tomorrow5=""
    temp5=""
    humidity5=""
    dt5=""
    condition5=[name5,tomorrow5,temp5,humidity5,dt5]
    for value in condition5:
        data=value
        tomorrow_database5.append(data)


    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerows([tomorrow_database5])

    tomorrow_database6=[]
    name6=""
    tomorrow6=""
    temp6=""
    humidity6=""
    dt6=""
    condition6=[name6,tomorrow6,temp6,humidity6,dt6]
    for value in condition6:
        data=value
        tomorrow_database6.append(data)


    with open(City_data ,'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerows([tomorrow_database6])
        


print("Successfully")











"""

    #print(weatherData['list']['main']['weather']['description'])
    #print(weatherData)
    #print("\n\n")
    #print("\n\n")
    #print(weatherData['list'][1]["humidity"])
    #print(weatherData['list'][2]['Desciption'])
print(weatherData['list']["name"])
    print(weatherData['list']['weather'][0]['description'])
    print(weatherData['list']["main"]['temp'])
    print(weatherData['list']["main"]["humidity"])"""
    

# key = 'appid=8d195f72c65049d55c801a702f095e96'

#http://api.openweathermap.org/data/2.5/forecast?q=Valrico,us&appid=8d195f72c65049d55c801a702f095e96


 
# Print weather descriptions.
# w = weatherData['list']
# for i in w:
#     print("iiiiiiiiiiiiiiii", i)
#print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
print('Day after the day after tomorrow:')
print(w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
print()
print('Day after the day after tomorrow the day after:')
print(w[4]['weather'][0]['main'], '-', w[4]['weather'][0]['description'])
print()
print('Day after the day after tomorrow the day after the day after:')
print(w[5]['weather'][0]['main'], '-', w[5]['weather'][0]['description'])
"""


# print('\n\nweather data: \n', w)
# print('\n\ntoday\'s weather data\n', w[0])
# print('\n\ntoday\'s weather list\n', w[0]['weather'])
# print()
# print()
# print(w[0]['weather'][0])
# print()
# print()
# print(w[0]['weather'][0]['main'])"""