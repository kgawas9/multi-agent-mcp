# from mcp.server.fastmcp import FastMCP
# import requests
# from decouple import config
# import sys

# mcp = FastMCP()

# weather_api_key = config("weather_api_key")
# weather_url = config("weather_url")


# @mcp.tool()
# def get_weather(city: str) -> str:
#     params = {
#         "q": city,
#         "appid": weather_api_key,
#         "units": "metric",
#     }

#     response = requests.get(weather_url, params=params)
#     data = response.json()

#     desc = data["weather"][0]["description"]
#     temp = data["main"]["temp"]

#     return f"{city}: {desc}, {temp}°C"


# if __name__ == "__main__":
#     # 🔥 DO NOT print anything here
#     # 🔥 DO NOT add debug logs to stdout
#     mcp.run(transport="stdio")