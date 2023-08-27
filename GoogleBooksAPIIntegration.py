import requests

from GoogleBooksAPIConstants import GoogleBooksSearchAPIContants
from GoogleBooksAPIResponseMapper import GoogleBooksAPIResponseMapper


class GoogleBooksAPI:
    __MAX_RESULTS = GoogleBooksSearchAPIContants.MAX_RESULTS
    __BOOK_SEARCH_API_URI = GoogleBooksSearchAPIContants.BOOK_SEARCH_API_URI

    def __init__(self, keywords, start_index=0):
        self.keywords = keywords
        self.start_index = start_index

    def getSearchResults(self):
        search_params = {'q':self.keywords, 'startIndex': self.start_index}
        search_result = requests.get(url=self.__BOOK_SEARCH_API_URI, params=search_params)
        google_response_mapper = GoogleBooksAPIResponseMapper(search_result.json())
        return google_response_mapper.map_response()
