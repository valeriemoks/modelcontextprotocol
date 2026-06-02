from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

import os
import asyncio

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http",
            },
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()

    model = ChatGroq(
        model="llama3-8b-8192"
    )

    agent = create_react_agent(
        model,
        tools
    )

    math_response = await agent.ainvoke(
        {"messages": [("user", "What is 2 + 2?")]}
    )

    print(math_response)

    weather_response = await agent.ainvoke(
        {"messages": [("user", "What is the weather in Tokyo?")]}
    )
    print(weather_response)["messages"][-1].get("content")



if __name__ == "__main__":
    asyncio.run(main())