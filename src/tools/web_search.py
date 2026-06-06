from typing import Any, Dict

from langchain.tools import tool
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool
def web_search(query:str) -> Dict[str, Any]:
    """
    Search the web for information
    """
    web_result = tavily_client.search(query)

    # print("\n=== WEB SEARCH RESULT ===")
    # print(web_result)
    # print("=========================\n")

    return web_result