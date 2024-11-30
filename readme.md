# Weather App Project

This is a simple Weather App built using Python, Tkinter for the GUI, and the WeatherAPI for fetching real-time weather data. The app allows users to enter a city name, fetch current weather details, and display them in a user-friendly interface.

## Features

- Fetches real-time weather data using the [WeatherAPI]
- Displays the current temperature, humidity, and weather condition for a city.
- Basic GUI built with Tkinter.
- Handles errors such as invalid city names or API issues.
  
## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `requests` library (for API requests)

## How It Works:
- The user enters a city name in the text box and clicks the "Get Weather" button.
- The app sends a request to the WeatherAPI, using the provided city and your API key.
- If successful, the app displays the temperature, weather condition, and humidity in the Tkinter window.
- If the city is invalid or there is an issue with the API request, an error message is displayed.



