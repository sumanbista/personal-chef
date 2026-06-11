from src.tools.web_search import web_search

def test_web_search():
    result = web_search.invoke(
        {
            "query":"Chicken fried rice recipe"
        }
    )

    assert result is not None 
    assert "results" in result 
    assert len(result["results"]) > 0