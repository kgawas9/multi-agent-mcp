import asyncio
from pydantic_ai import Agent
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

agent = Agent(model="groq:llama-3.3-70b-versatile")


async def main():
    server = StdioServerParameters(
        command="uv",
        args=[
            "--directory",
            "D:/intermediate/mcp_ai/mcp_agent_clean/weather_server",
            "run",
            "tools.py",
        ],
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:

            # 🔥 REQUIRED handshake
            await session.initialize()

            # 🔥 FIX (correct for your version)
            tools_result = await session.list_tools()
            tools = tools_result.tools

            print("Available tools:", [t.name for t in tools])

            # 🔥 call tool
            weather_result = await session.call_tool(
                "get_weather",
                {"city": "Pune"},
            )

            stock_result = await session.call_tool(
                "get_stock_price",
                {"symbol": "RELIANCE.NS"},
            )

            # 🔥 format response
            final = await agent.run(
                f"""
                Format this nicely:

                Weather:
                {weather_result.content}

                Stock:
                {stock_result.content}
                """
            )

            print(final)


if __name__ == "__main__":
    asyncio.run(main())