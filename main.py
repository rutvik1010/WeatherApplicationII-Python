# -*- coding: utf-8 -*-

import datetime
import time
import json
import tkFont
import requests
import urllib2
from PIL import ImageTk
import PIL.Image
import forecastio
try:\

    from tkinter import *
except ImportError:
    from Tkinter import *

#Window Setup
root = Tk()
root.geometry("800x480")
root.title("Weatherly")
#root.attributes('-fullscreen', True)
#root.configure(cursor='none')
root.resizable(width = False, height = False)
root.bind("<Escape>", lambda e: e.widget.quit()) # Handling escape key

#Background Image
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = bg_copy.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo
bg_image = PIL.Image.open('bg.jpg')
bg_copy = bg_image.copy()
photo = ImageTk.PhotoImage(bg_image)
label = Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

#Upper Image
sec_bg_u = PIL.Image.open('upper_bg.png')
sec_photo_u = ImageTk.PhotoImage(sec_bg_u)
label_sec_bg_u = Label(root, image = sec_photo_u)
label_sec_bg_u.place(x = 100, y = 75, width = 600, height = 150)

#Weather Image
cloudy_dft = PIL.Image.open('cloudy.jpg')
cloudy = ImageTk.PhotoImage(cloudy_dft)
clearday_dft = PIL.Image.open('clear-day.jpg')
clearday = ImageTk.PhotoImage(clearday_dft)
clearnight_dft = PIL.Image.open('clear-night.jpg')
clearnight = ImageTk.PhotoImage(clearnight_dft)
partlycloudyday_dft = PIL.Image.open('partly-cloudy-day.jpg')
partlycloudyday = ImageTk.PhotoImage(partlycloudyday_dft)
partlycloudynight_dft = PIL.Image.open('partly-cloudy-night.jpg')
partlycloudynight = ImageTk.PhotoImage(partlycloudynight_dft)
rain_dft = PIL.Image.open('rain.jpg')
rain = ImageTk.PhotoImage(rain_dft)
snow_dft = PIL.Image.open('snow.jpg')
snow = ImageTk.PhotoImage(snow_dft)
wind_dft = PIL.Image.open('wind.jpg')
wind = ImageTk.PhotoImage(wind_dft)
fog_dft = PIL.Image.open('fog.jpg')
fog = ImageTk.PhotoImage(fog_dft)
sleet_dft = PIL.Image.open('sleet.jpg')
sleet = ImageTk.PhotoImage(sleet_dft)

#Cloud
cloud = PIL.Image.open('cloud.png')
cloud_p = ImageTk.PhotoImage(cloud)
label_cloud = Label(root, image = cloud_p, borderwidth='0')
label_cloud.place(x = 340, y = 120)

#Lower Image
sec_bg_l = PIL.Image.open('lower_bg.png')
sec_photo_l = ImageTk.PhotoImage(sec_bg_l)
label_sec_bg_l = Label(root, image = sec_photo_l)
label_sec_bg_l.place(x = 100, y = 225, width = 600, height = 200)

#Region Label
region_label = Label(root, text = "Jersey City", font = ('Comic Sans MS', 15), fg = 'white', bg = 'dodger blue')
region_label.place(x = 110, y = 80)

#Time Label
time1 = ''
def tick_time_sec():
    global time1
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
        time_label.config(text = time2)
    time_label.after(500, tick_time_sec)
time_label = Label(root, font = ('Comic Sans MS', 15), fg = 'white', bg = 'dodger blue')
time_label.place(x = 620, y = 80)

#Weather Label
opw_api = 'API KEY'
api_key = "API KEY"
#lat = 40.7276
#lng = -74.0308
lat = 51.260197
lng = 4.402771
temp_hour1 = ''
weather_link = "http://api.openweathermap.org/data/2.5/weather?id=5099357&units=metric&APPID=" + opw_api
forecast_link = "http://api.openweathermap.org/data/2.5/forecast?id=5099357&units=metric&APPID=" + opw_api


def fetchHTML(string1):
    URL = string1
    req = urllib2.Request(URL)
    response = urllib2.urlopen(req)
    return response.read()

def tick_today_temp_hourly():
    global temp_hour1
    tock_temp = fetchHTML(weather_link)
    tock_weather = json.loads(tock_temp)
    temp_hour2 = str(int(tock_weather.get('main').get('temp')))
    if temp_hour2 != temp_hour1:
        temp_hour1 = temp_hour2
        d_temp_label.config(text = str(int(temp_hour2)))
        d_humidity_label.config(text = "Humidity: " + str((tock_weather.get('main').get('humidity'))) + "%")
        d_wind_label.config(text = "Wind: " + str(tock_weather.get('wind').get('speed')) + "m/s")
    d_temp_label.after(1000*60*60, tick_today_temp_hourly)

d_temp_label = Label(root, font = ('Comic Sans MS', 30), fg = 'black', bg = 'white')
d_temp_label.place(x = 110, y = 240)

d_temp_label_deg = Label(root, text = '°C', font = ('Comic Sans MS', 15), fg = 'black', bg = 'white')
d_temp_label_deg.place(x = 165, y = 240)

d_humidity_label = Label(root, font = ('Helevetica', 8), fg = 'black', bg = 'white')
d_humidity_label.place(x = 110, y = 340)

d_wind_label = Label(root, font = ('Helevetica', 8), fg = 'black', bg = 'white')
d_wind_label.place(x = 110, y = 360)


#DAY OF THE WEEK
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
date_today1 = ''

def day_int(i):
    date_dft = datetime.datetime.now().date() + datetime.timedelta(days=i)
    d_int = date_dft.weekday()
    return d_int

def tick_date_min():
    global date_today1
    date_today2 = str(datetime.datetime.now().date())
    if date_today2 != date_today1:
        date_today1 = date_today2
        date_today_label.config(text = str(days_of_the_week[datetime.datetime.now().date().weekday()]))
        date_one_label.config(text = str(days_of_the_week[day_int(1)]))
        date_two_label.config(text = str(days_of_the_week[day_int(2)]))
        date_three_label.config(text = str(days_of_the_week[day_int(3)]))
        date_four_label.config(text = str(days_of_the_week[day_int(4)]))
        date_five_label.config(text = str(days_of_the_week[day_int(5)]))
    date_today_label.after(1000*10, tick_date_min)

date_today_label = Label(root, font = ('Comic Sans MS', 12), fg = 'brown', bg = 'white')
date_today_label.place(x = 110, y = 310)
date_one_label = Label(root, font = ('Comic Sans MS', 10), fg = 'brown', bg = 'white')
date_one_label.place(x = 210, y = 390)
date_two_label = Label(root, font = ('Comic Sans MS', 10), fg = 'brown', bg = 'white')
date_two_label.place(x = 310, y = 390)
date_three_label = Label(root,font = ('Comic Sans MS', 10), fg = 'brown', bg = 'white')
date_three_label.place(x = 410, y = 390)
date_four_label = Label(root,font = ('Comic Sans MS', 10), fg = 'brown', bg = 'white')
date_four_label.place(x = 510, y = 390)
date_five_label = Label(root,font = ('Comic Sans MS', 10), fg = 'brown', bg = 'white')
date_five_label.place(x = 610, y = 390)

#FORECAST WEATHER

def icon_string(byDay, i):
    icon_des = byDay.data[i].icon
    return icon_des

def icon_implement(descp, label_i):
    if (descp == 'cloudy'):
        label_i.configure(image='cloudy.jpg')
    elif (descp == 'partly-cloudy-day'):
        label_i.config(image=partlycloudyday)
    elif (descp == 'partly-cloudy-night'):
        label_i.configure(image=partlycloudynight)
    elif (descp == 'rain'):
        label_i.configure(image=rain)
    elif (descp == 'clear-night'):
        label_i.configure(image=clearnight)
    elif (descp == 'clear-day'):
        label_i.configure(image=clearday)
    elif (descp == 'fog'):
        label_i.configure(image=fog)
    elif (descp == 'wind'):
        label_i.configure(image=wind)
    elif (descp == 'sleet'):
        label_i.configure(image=sleet)
    elif (descp == 'snow'):
        label_i.configure(image=snow)
    else:
        label_i.configure(image=cloudy)

date_today4 =''
def tick_forecast():
    global date_today4
    date_today3 = str(datetime.datetime.now().date())
    if date_today3 != date_today4:
        date_today4 = date_today3
        forecast = forecastio.load_forecast(api_key, lat, lng)
        byDay = forecast.daily()
        for_one_label.config(text = str("Max: " + str(int((byDay.data[1].temperatureMax - 32)*5/9))  + "°C" + "\n\nMin: " + str(int((byDay.data[1].temperatureMin - 32)*5/9)) + "°C"))
        for_two_label.config(text = str("Max: " + str(int((byDay.data[2].temperatureMax - 32)*5/9))  + "°C" + "\n\nMin: " + str(int((byDay.data[2].temperatureMin - 32)*5/9)) + "°C"))
        for_three_label.config(text = str("Max: " + str(int((byDay.data[3].temperatureMax - 32)*5/9))  + "°C" + "\n\nMin: " + str(int((byDay.data[3].temperatureMin - 32)*5/9)) + "°C"))
        for_four_label.config(text = str("Max: " + str(int((byDay.data[4].temperatureMax - 32)*5/9))  + "°C" + "\n\nMin: " + str(int((byDay.data[4].temperatureMin - 32)*5/9)) + "°C"))
        for_five_label.config(text = str("Max: " + str(int((byDay.data[5].temperatureMax - 32)*5/9))  + "°C" + "\n\nMin: " + str(int((byDay.data[5].temperatureMin - 32)*5/9)) + "°C"))

        day_one_icon_string = icon_string(byDay, 1)
        day_two_icon_string = icon_string(byDay, 2)
        day_three_icon_string = icon_string(byDay, 3)
        day_four_icon_string = icon_string(byDay, 4)
        day_five_icon_string = icon_string(byDay, 5)

        icon_implement(day_one_icon_string, icon_day_one)
        icon_implement(day_two_icon_string, icon_day_two)
        icon_implement(day_three_icon_string, icon_day_three)
        icon_implement(day_four_icon_string, icon_day_four)
        icon_implement(day_five_icon_string, icon_day_five)

        summary_label.config(text = "Today's weather summary: " + str(byDay.data[0].summary))

    date_today_label.after(1000*60*5, tick_forecast)

for_one_label = Label(root, font = ('Helevetica', 10), fg = 'black', bg = 'white')
for_one_label.place(x = 215, y = 330)
for_two_label = Label(root, font = ('Helevetica', 10), fg = 'black', bg = 'white')
for_two_label.place(x = 315, y = 330)
for_three_label = Label(root,font = ('Helevetica', 10), fg = 'black', bg = 'white')
for_three_label.place(x = 415, y = 330)
for_four_label = Label(root,font = ('Helevetica', 10), fg = 'black', bg = 'white')
for_four_label.place(x = 515, y = 330)
for_five_label = Label(root,font = ('Helevetica', 10), fg = 'black', bg = 'white')
for_five_label.place(x = 615, y = 330)

#ICON LABELS
icon_day_one = Label(root, borderwidth=0)
icon_day_one.place(x = 215, y = 250)
icon_day_two = Label(root, borderwidth=0)
icon_day_two.place(x = 315, y = 250)
icon_day_three = Label(root, borderwidth=0)
icon_day_three.place(x = 415, y = 250)
icon_day_four = Label(root, borderwidth=0)
icon_day_four.place(x = 515, y = 250)
icon_day_five = Label(root, borderwidth=0)
icon_day_five.place(x = 615, y = 250)


#API LABEL
darksky_label = Label(root, text = "Powered by Dark Sky", font = ('Helevetica', 5))
darksky_label.place(x = 700, y = 460)

#Summary Label
summary_label = Label(root, font = ('Helevetica', 8), bg = 'dodger blue', fg = 'black')
summary_label.place(x = 110, y = 200)

tick_time_sec()
tick_date_min()
tick_today_temp_hourly()
tick_forecast()
mainloop()