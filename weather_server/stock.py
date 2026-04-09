from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP()

@mcp.tool()
def get_stock_price(symbol: str) -> str:
    """
    Fetch stock price using a free public API (Yahoo Finance).
    """

    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
        response = requests.get(url)
        data = response.json()

        result = data["quoteResponse"]["result"]

        if not result:
            return f"No data found for symbol: {symbol}"

        price = result[0]["regularMarketPrice"]
        name = result[0]["shortName"]

        return f"{name} ({symbol}): ₹{price}"

    except Exception as e:
        return f"Error fetching stock: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")