import json
import pprint
from datetime import datetime

DEGREE_SYMBOL = u"Â\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    """
    temp = convert_f_to_c(temp)
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius
    """
    return round((temp_in_farenheit - 32) / 1.8,1)


def calculate_mean(total, num_items):
    """Calculates the mean.
    """
    return round(total/num_items,1)


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)

        num_items = 0
        weather_data = []

        for day in json_data["DailyForecasts"]:
            if num_items == 0:
                min_temp_date = day["Date"]
                max_temp_date = day["Date"]
                min_temp = day["Temperature"]["Minimum"]["Value"]
                max_temp = day["Temperature"]["Maximum"]["Value"]
                sum_max_temps = max_temp
                sum_min_temps = min_temp

            if num_items >= 1:
                temp_min = day["Temperature"]["Minimum"]["Value"]
                temp_max = day["Temperature"]["Maximum"]["Value"]

                sum_min_temps += temp_min
                sum_max_temps += temp_max

                if temp_min < min_temp:
                    min_temp = temp_min
                    min_temp_date = day["Date"]
                
                if temp_max > max_temp:
                    max_temp = temp_max
                    max_temp_date = day["Date"]
   
            num_items += 1
        
        mean_min_temp = format_temperature(calculate_mean(sum_min_temps, num_items))
        mean_max_temp = format_temperature(calculate_mean(sum_max_temps, num_items))

        min_temp = format_temperature(min_temp)
        max_temp = format_temperature(max_temp)

        min_temp_date = convert_date(min_temp_date)
        max_temp_date = convert_date(max_temp_date)

        weather_data.append(f"{num_items} Day Overview\n")
        weather_data.append(f"    The lowest temperature will be {min_temp}, and will occur on {min_temp_date}.\n")
        weather_data.append(f"    The highest temperature will be {max_temp}, and will occur on {max_temp_date}.\n")
        weather_data.append(f"    The average low this week is {mean_min_temp}.\n")
        weather_data.append(f"    The average high this week is {mean_max_temp}.\n\n")


        # print out weather for each day formatted
        for day in json_data["DailyForecasts"]:
            
            date = convert_date(day["Date"]) 
            weather_data.append(f"-------- {date} --------\n")

            temp_min = format_temperature(day["Temperature"]["Minimum"]["Value"])
            temp_max = format_temperature(day["Temperature"]["Maximum"]["Value"])
            weather_data.append(f"Minimum Temperature: {temp_min}\n")
            weather_data.append(f"Maximum Temperature: {temp_max}\n")

            day_phrase = day["Day"]["LongPhrase"]
            day_rain = day["Day"]["RainProbability"]

            weather_data.append(f"Daytime: {day_phrase}\n")
            weather_data.append(f"    Chance of rain:  {day_rain}%\n")

            night_phrase = day["Night"]["LongPhrase"]
            night_rain = day["Night"]["RainProbability"]

            weather_data.append(f"Nighttime: {night_phrase}\n")
            weather_data.append(f"    Chance of rain:  {night_rain}%\n\n")

    return "".join(weather_data)


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))

    with open("part1_output.txt", "w") as txt_file:
            txt_file.write(process_weather("data/forecast_5days_a.json"))
    





