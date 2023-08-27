class GoogleBooksAPIResponseMapper:
    def __init__(self, response_json):
        self.response_json = response_json

    def map_response(self):
        result_count = self.response_json['totalItems']
        books = self.response_json['items']
        items = []
        for book in books:
            item = {
                'title': book['volumeInfo'].get('title',''),
                'subtitle': book['volumeInfo'].get('subtitle', ''),
                'description': book['volumeInfo'].get('description',''),
                'authors': book['volumeInfo'].get('authors',[]),
                'imageLinks': book['volumeInfo'].get('imageLinks', {}),
            }
            items.append(item)
        search_results = {
            'result_count': result_count,
            'items': items,
        }
        return search_results
