import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    API_KEY = "a3c2b589292b448fae840921243011" 
    location = location_entry.get()

    if not location:
        messagebox.showwarning("Input Error", "Please enter a location!")
        return

    # WeatherAPI URL
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"

    try:

        response = requests.get(url)
        data = response.json()

        if "error" in data:
            raise Exception(data["error"]["message"])

        temp = data['current']['temp_c']
        rain_chances = data['current']['precip_mm']

        temperature_label.config(text=f"Temperature: {temp}°C")
        rain_label.config(text=f"Rain Chances: {rain_chances} mm")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve weather data:\n{e}")

# Tkinter window
root = tk.Tk()
root.title("Weather App")

# GUI Components
tk.Label(root, text="Enter Location:", font=("Arial", 14)).pack(pady=10)
root.geometry("400x300+500+300")
root.resizable(False, False)
frame = tk.Frame(root)
location_entry = tk.Entry(root, font=("Segoe ui", 14), width=20)
location_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Check", font=("Arial", 14), command=get_weather)
get_weather_button.pack(pady=10)

temperature_label = tk.Label(root, text="Temperature: N/A", font=("Segoe ui", 14))
temperature_label.pack(pady=5)

rain_label = tk.Label(root, text="Rain Chances: N/A", font=("Segoe ui", 14))
rain_label.pack(pady=5)

root.mainloop()
