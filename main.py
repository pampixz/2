from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia
app = FastAPI()
@app.get("/{people}")
def search(people: str, page_number: int):
    results = ""
    for i in range(page_number):
        results += f"{i + 1}" + str(wikipedia.search(people)) + ""
    return results
class person_search(BaseModel):
    person: str = "Bill"
    page: int = 5
@app.post("/person")
def wikipedia_search(searching: person_search):
    return wikipedia.search(searching.person, results=searching.page)
