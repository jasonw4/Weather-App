from tkinter import *
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.wm_title("Global Weather")
root.geometry("900x500+300+200")
root.resizable(False, False)

counter =0

def getWeather():
    global counter
    counter+= 1
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent = "geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text = current_time)
        name.config(text = "CURRENT WEATHER")

        #weather
        api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=0220250bd57828b129475481feb6d8dd"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(1.8*(json_data['main']['temp']-273.15) + 32)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text = (temp, "°"))
        c.config(text = (condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text = wind)
        h.config(text = humidity)
        d.config(text = description)
        p.config(text = pressure)
        counterlbl.config(text = "# of cities searched:   " + str(counter))
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry... Please try again...")

textfield = tk.Entry(root, justify = "center",font=('Comic Sans MS', 12, 'bold italic'),bg = "#FFFFFF", highlightthickness=2)
textfield.config(highlightbackground = "red", highlightcolor= "red")
 
textfield.place(x = 40, y= 110, height = 50, width = 300)

search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image = search_icon, borderwidth = 0, cursor = "hand2", bg = "#040404", command = getWeather)
myimage_icon.place(x = 340, y = 105)

#logo

logo_image = PhotoImage(file = "logo.png")
logo = Label(image = logo_image)
logo.place(x = 500, y = 100)

#bottombox
box_image = PhotoImage(file = "box.png")
box_img_lbl = Label(image = box_image)
box_img_lbl.pack(padx = 5, pady =5, side = BOTTOM)

#clock
timer = Label(root, text = "", font = ("arial", 12))
timer.pack(padx = 5, pady =5, side = TOP)
#time
name = Label(root, font = ("Courier", 15, "bold"))
name.place(x = 30, y=200)
clock = Label(root, font = ("Helvetica",20))
clock.place(x = 30, y= 250)

#label
label1 = Label(root, text = "WIND", font =("Helvetica", 15, "bold"), bg = "#1ab5ef")
label1.place(x = 120, y = 400)

label2 = Label(root, text = "HUMIDITY", font =("Helvetica", 15, "bold"), bg = "#1ab5ef")
label2.place(x = 240, y = 400)

label3 = Label(root, text = "DESCRIPTION", font =("Helvetica", 15, "bold"), bg = "#1ab5ef")
label3.place(x = 430, y = 400)

label4 = Label(root, text = "PRESSURE", font =("Helvetica", 15, "bold"), bg = "#1ab5ef")
label4.place(x = 650, y = 400)

t = Label(font = ("Courier", 50, "bold"), fg = "#0000ff")
t.place(x = 200, y = 200)
c = Label(font = ("Courier", 15, "bold"))
c.place(x = 200, y = 250)

w = Label(text = "...", font = ("Courier", 20, "bold"), bg = "#1ab5ef")
w.place(x = 120, y=430)

h = Label(text = "...", font = ("Courier", 20, "bold"), bg = "#1ab5ef")
h.place(x = 240, y=430)

d = Label(text = "...", font = ("Courier", 20, "bold"), bg = "#1ab5ef")
d.place(x = 430, y=430)

p = Label(text = "...", font = ("Courier", 20, "bold"), bg = "#1ab5ef")
p.place(x = 650, y=430)

#message
welcome = Label(root, text = "Welcome to Global Weather Search! Please enter a city...", font = ("Helvetica", 20))
welcome.place(x = 20, y =20)

#counter
counterlbl = Label(root, text = "# of cities searched:   " + str(counter), font = ("Helvetica", 20))
counterlbl.place(x = 500, y =350)
root.mainloop()