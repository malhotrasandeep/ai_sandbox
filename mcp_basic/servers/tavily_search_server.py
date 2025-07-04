from fastmcp import FastMCP
import os
import requests
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("Tavily Search MCP Server")

@mcp.tool
def search(query:str, max_results=3):
    """
    use this tool to do any web search
    """
    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {os.environ['TAVILY_API_KEY']}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "search_depth": "advanced",
        "include_answer": True,
        'max_results':max_results,
    }

    response = requests.post(url, headers=headers, json=payload)
    response.json()

if __name__ == '__main__':
    print("Will run")
    try:
        mcp.run(transport="streamable-http")
    except Exception as e:
        print(e)

