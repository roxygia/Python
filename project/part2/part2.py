import json
from datetime import datetime
import plotly.express as px
import pandas as pd

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    #Takes a temperature and returns it in string format with the degrees and celcius symbols.
    temp = convert_f_to_c(temp)
    return f"{temp}{DEGREE_SYMBOL} "

def convert_f_to_c(temp_in_farenheit):
    #Converts an temperature from farenheit to celcius

    return round((temp_in_farenheit - 32) / 1.8,1)

def convert_date(iso_string):
    #Converts and ISO formatted date into a human readable format.
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

with open("data/forecast_5days_a.json") as json_file:
    wd = json.load(json_file)

    dates = []
    min_temps = []
    max_temps = []
    min_real_temps = []
    min_shade_temps = []

    for day in wd["DailyForecasts"]:

            date = convert_date(day["Date"])
            dates.append(date)

            temp_max = format_temperature(day["Temperature"]["Maximum"]["Value"])
            temp_min = format_temperature(day["Temperature"]["Minimum"]["Value"])
            temp_min_real = format_temperature(day["RealFeelTemperature"]["Minimum"]["Value"])
            temp_min_shade = format_temperature(day["RealFeelTemperatureShade"]["Minimum"]["Value"])

            max_temps.append(temp_max)
            min_temps.append(temp_min)
            min_real_temps.append(temp_min_real)
            min_shade_temps.append(temp_min_shade)

df = {
    "Minimum Temperature": min_temps,
    "Maximum Temperature": max_temps,
    "Min Real Feel Temperature": min_real_temps,
    "Min Real Feel Temperature Shade": min_shade_temps,
    "Date": dates
}

fig = px.line(df, y=["Minimum Temperature", "Maximum Temperature"], x="Date", title="Time Series Graph:  Minimum and Maximum Temperatures")
fig.show()

fig2 = px.line(df, y=["Minimum Temperature", "Min Real Feel Temperature", "Min Real Feel Temperature Shade"], x="Date", title="Time Series Graph 2:  Minimum Temperatures")
fig2.show()
