from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a009be2239ae527255569d52bf41965d"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        temp_celsius = int(data['main']['temp'] - 273.15)
        temp_label1.config(text=f"{temp_celsius}°C")
        pre_label1.config(text=f"{data['main']['pressure']} hPa")
    else:
        w_label1.config(text="Weather data not available.")
        wd_label1.config(text="")
        temp_label1.config(text="")
        pre_label1.config(text="")

# Create main window
win = Tk()
win.title("Weather Application")
win.config(bg="sky blue")  # Set background color
win.geometry("500x570")
win.attributes('-alpha', 0.95)  # Set transparency level (0.0 to 1.0)

# Title label
name_label = Label(win, text="Weather Application", font=("Arial", 24, "bold"), bg="sky blue")
name_label.place(x=25, y=50, width=450, height=50)

# Combobox for city selection
list_name = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
    'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
    'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
    'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
    'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
    'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
]
city_name = StringVar()
com = ttk.Combobox(win, values=list_name, font=("Arial", 16), textvariable=city_name)
com.place(x=25, y=120, width=450, height=50)

# Weather labels
w_label = Label(win, text="Weather Climate", font=("Arial", 18), bg="sky blue", fg="white")
w_label.place(x=25, y=200, width=210, height=40)
w_label1 = Label(win, text="", font=("Arial", 18), bg="sky blue", fg="white")
w_label1.place(x=250, y=200, width=210, height=40)

wd_label = Label(win, text="Weather Description", font=("Arial", 18), bg="sky blue", fg="white")
wd_label.place(x=25, y=260, width=210, height=40)
wd_label1 = Label(win, text="", font=("Arial", 18), bg="sky blue", fg="white")
wd_label1.place(x=250, y=260, width=210, height=40)

temp_label = Label(win, text="Temperature", font=("Arial", 18), bg="sky blue", fg="white")
temp_label.place(x=25, y=320, width=210, height=40)
temp_label1 = Label(win, text="", font=("Arial", 18), bg="sky blue", fg="white")
temp_label1.place(x=250, y=320, width=210, height=40)

pre_label = Label(win, text="Pressure", font=("Arial", 18), bg="sky blue", fg="white")
pre_label.place(x=25, y=380, width=210, height=40)
pre_label1 = Label(win, text="", font=("Arial", 18), bg="sky blue", fg="white")
pre_label1.place(x=250, y=380, width=210, height=40)

# Done button
done_btn = Button(win, text="Get Weather", font=("Arial", 18, "bold"), bg="orange", fg="white", command=data_get)
done_btn.place(x=175, y=450, width=150, height=50)

# Start main event loop
win.mainloop()
