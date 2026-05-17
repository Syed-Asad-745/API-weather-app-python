## Weather App

A desktop weather application built with Python and tkinter that fetches 
live weather data using the OpenWeatherMap API.


## Features
- Search weather by city name
- Displays temperature, humidity, wind speed, and weather condition
- Error handling for invalid city names and empty input
- Clean GUI built with tkinter

## Requirements
- Python 3
- requests library

Install dependencies:
pip install requests

## Setup
1. Get a free API key from openweathermap.org
2. Create a file called openweather_api.txt in the project folder
3. Paste your API key inside the file
4. Run the app: python weather.py

## What I Learned
- How to make API calls using the requests library
- Parsing JSON responses from a REST API
- Building a GUI application with tkinter
- Handling errors gracefully in both the API layer and the UI


##Description
Built as part of my Python portfolio, this weather app taught me how to 
work with REST APIs, parse JSON responses, and build a functional GUI 
with tkinter. Users can search any city and instantly see temperature, 
humidity, wind speed, and weather conditions fetched live from the 
OpenWeatherMap API. Incorrect inputs such as not existing city names,
white spaces, empty strings etc; give rise to errors which are handled
with data verification steps.
