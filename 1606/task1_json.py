import json

with open("forecast.json", "r") as file:
    data = json.load(file)

inx = data["hourly"]["time"].index("2024-06-10T04:00")
res = data["hourly"]["temperature_2m"][inx]

print(res)