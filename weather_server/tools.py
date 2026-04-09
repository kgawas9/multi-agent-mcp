from mcp.server.fastmcp import FastMCP
import requests
from decouple import config

mcp = FastMCP()

weather_api_key = config("weather_api_key")
weather_url = config("weather_url")


# 🌦️ WEATHER TOOL
@mcp.tool()
def get_weather(city: str) -> str:
    try:
        params = {
            "q": city,
            "appid": weather_api_key,
            "units": "metric",
        }

        response = requests.get(weather_url, params=params)

        if response.status_code != 200:
            return f"API error: {response.text}"

        data = response.json()

        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        return f"{city}: {desc}, {temp}°C"

    except Exception as e:
        return f"Error: {str(e)}"


# 📈 STOCK TOOL
# @mcp.tool()
# def get_stock_price(symbol: str) -> str:
#     url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
#     response = requests.get(url)
#     data = response.json()

#     result = data["quoteResponse"]["result"]

#     if not result:
#         return f"No data found for {symbol}"

#     price = result[0]["regularMarketPrice"]
#     name = result[0]["shortName"]

#     return f"{name} ({symbol}): ₹{price}"


# if __name__ == "__main__":
#     mcp.run(transport="stdio")


@mcp.tool()
def get_stock_price(symbol: str) -> str:
    try:
        import requests  # ensure import inside

        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return f"API error: {response.text}"

        data = response.json()

        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return f"No data found for {symbol}"

        stock = result[0]

        price = stock.get("regularMarketPrice")
        name = stock.get("shortName", symbol)

        if price is None:
            return f"Price not available for {symbol}"

        return f"{name} ({symbol}): ₹{price}"

    except Exception as e:
        return f"Stock error: {str(e)}"
    

if __name__ == "__main__":
    mcp.run(transport="stdio")