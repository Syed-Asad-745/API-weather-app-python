import requests
import tkinter as tk

#-----------------------imports api key------------------------
def get_api_key():
    with open("openweather_api.txt", "r") as file:
        api_key = file.read()
        return api_key

#------------------------calls the url-------------------------
def fetch_weather(city):
    api_key = get_api_key()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

#--------------formats raw data into readable format------------
def parse_weather(data):
    city = data["name"]
    temperature = round((data["main"]["temp"] - 273.15),1)
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    weather_data = {"City" : city,
                    "Temperature" : temperature,
                    "Weather" : weather,
                    "Humidity" : humidity,
                    "Wind" : wind}
    
    return weather_data

#---------------------creates window widgets----------------------
def create_widgets(window):

    title_label = tk.Label(window,
                           text="Weather App",
                           font=("Consolas",40),
                           bg="#73ffef",
                           pady=20)
    title_label.pack()

    entry_box = tk.Entry(window,
                         font=("Consolas",30),
                         bg="#00ffe1")
    entry_box.pack(padx=30)

    fetch_button = tk.Button(window,
                             text="Fetch Weather",
                             font=("Consolas",20),
                             bg="#ffc800",
                             pady=20,
                             command=lambda :fetch_weather_data())
    fetch_button.pack()

    display_label = tk.Label(window,
                             text="Please enter a city name.",
                             font=("Consolas",20),
                             justify="left",
                             bg="#73ffef",
                             wraplength=500,
                             pady=20)
    display_label.pack()

    #-----------------------button command function------------------------
    def fetch_weather_data():
        city = entry_box.get().strip()
        if city == "":
            display_label.config(text="Please enter a city name!")
            return
        else:
            data =  fetch_weather(city)
            if data["cod"] == 200:
                weather_data = parse_weather(data)
                show = (f"City        : {weather_data['City']}\n"
                        f"Temperature : {weather_data['Temperature']}°C\n"
                        f"Weather     : {weather_data['Weather']}\n"
                        f"Humidity    : {weather_data['Humidity']}%\n"
                        f"Wind        : {weather_data['Wind']}m/s\n")
                display_label.config(text=show)
            else:
                display_label.config(text="City not found :(\nPlease check the spelling.")

#-----------------------main funtion------------------------
def main():
    weather_app_window = tk.Tk()
    weather_app_window.title("API Weather App")
    weather_app_window.geometry("500x500")
    weather_app_window.config(bg="#73ffef")

    create_widgets(weather_app_window)

    weather_app_window.mainloop()

if __name__ == "__main__":
    main()