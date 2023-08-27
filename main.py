from fastapi import FastAPI

from GoogleBooksAPIIntegration import GoogleBooksAPI

app = FastAPI()

@app.get("/search/{keywords}")
async def search_books(keywords: str, start_idx: int = 0):
    googleBooksAPI = GoogleBooksAPI(keywords, start_idx)
    return {"search_results": googleBooksAPI.getSearchResults()}