import tkinter as tk
import requests
from datetime import datetime


root = tk.Tk()
root.title("🌤️ Weather App")
root.geometry("400x500")
root.configure(bg="#1e1e2f")


CARD_COLOR = "#2a2a40"
TEXT_COLOR = "white"
ACCENT_COLOR = "#ffca28"
FONT = ("Segoe UI", 12)
BIG_FONT = ("Segoe UI", 16, "bold")


def on_click(e):
    if city_entry.get() == "Enter city":
        city_entry.delete(0, tk.END)
        city_entry.config(fg=TEXT_COLOR)

def on_leave(e):
    if not city_entry.get():
        city_entry.insert(0, "Enter city")
        city_entry.config(fg="#aaa")

city_entry = tk.Entry(root, font=BIG_FONT, fg="#aaa", bg=CARD_COLOR, insertbackground="white", relief="flat", justify="center")
city_entry.insert(0, "Enter city")
city_entry.bind("<FocusIn>", on_click)
city_entry.bind("<FocusOut>", on_leave)
city_entry.pack(pady=20, ipadx=10, ipady=6)


card = tk.Frame(root, bg=CARD_COLOR, bd=0)
card.pack(pady=10, padx=20, fill="both", expand=True)
# text="🌤️"
# text="Welcome to the Weather App"
weather_label = tk.Label(card, text="Welcome to the Weather App" ,font=("Segoe UI", 48), bg=CARD_COLOR, fg=ACCENT_COLOR)
weather_label.pack(pady=10)

info_label = tk.Label(card, text="", font=BIG_FONT, bg=CARD_COLOR, fg=TEXT_COLOR, justify="center")
info_label.pack()

extra_label = tk.Label(card, text="", font=FONT, bg=CARD_COLOR, fg=TEXT_COLOR)
extra_label.pack(pady=5)

date_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#1e1e2f", fg="#888")
date_label.pack(pady=5)


def get_weather():
    city = city_entry.get()
    if city == "" or city == "Enter city":
        info_label.config(text="Please enter a city")
        return

    api_key = "ddd6a4c943487dd80b4a0a7a0cdfc471" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            info_label.config(text="City not found")
            extra_label.config(text="")
            weather_label.config(text="❌")
            return

        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        feels_like = data['main']['feels_like']
        visibility = data.get('visibility', 0)
        country = data['sys']['country']

        icon = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Haze": "🌫️",
            "Mist": "🌁",
            "Thunderstorm": "⛈️",
            "Snow": "❄️"
        }.get(condition, "🌡️")

        weather_label.config(text=icon)
        info_label.config(text=f"{city.title()}, {country}\n{temp}°C | {desc.capitalize()}")
        extra_label.config(text=f"Feels like: {feels_like}°C\nHumidity: {humidity}%\nWind: {wind} m/s\nVisibility: {visibility}m")

        date_label.config(text=datetime.now().strftime("Updated: %A %d %b | %I:%M %p"))

    except Exception as e:
        info_label.config(text="Error getting data")
        print(e)

# --- Search Button ---
search_btn = tk.Button(root, text="Get Weather", command=get_weather, font=FONT,
                       bg=ACCENT_COLOR, fg="black", relief="flat", padx=10, pady=5)
search_btn.pack()

# Bind Enter Key
root.bind("<Return>", lambda event: get_weather())

root.mainloop()
