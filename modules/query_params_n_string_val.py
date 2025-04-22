from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/countries/")
async def update_countries(continent: Annotated[str, Query(min_length=2, description="Filter by continent")] = "Europe"):
    available_countries = {
        "Europe": ["France", "Germany", "Italy"],
        "Asia": ["Japan", "China", "India"],
        "Americas": ["Brazil", "USA", "Canada"]
    }
    
    response = {}
    
    if continent in available_countries:
        response["countries"] = available_countries[continent]
    else:
        response["countries"] = []
        response["message"] = f"No countries found for {continent}"
    
    return response
