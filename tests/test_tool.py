from src.tools.web_search import web_search

result = web_search.invoke(
    {
        "query":"Chicken fried rice recipe"
    }
)

print(result)