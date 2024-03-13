import urllib.parse, urllib.request, urllib.error, json, random

def find_book(subject):

    base_url = 'https://openlibrary.org/search.json'
    params = {'subject': subject, 'limit': 50, 'rating': 4.5, 'new': 'first_publish_year desc' }
    paramster = urllib.parse.urlencode(params)
    book_request = base_url + '?' + paramster
    #book_request = base_url + '?subject=' + subject
    response = urllib.request.urlopen(book_request)
    book_response_str = response.read()
    books_data = json.loads(book_response_str)
    max = len(books_data['docs']) - 1
    rand = random.randint(0, max)
    #for book in books_data['docs']:
        #print(book['title'])
    return books_data['docs'][rand]
def safe_find_book(q):
    try:
        return find_book(q)
    except urllib.error.HTTPError:
        print('Error trying to retrieve data: HTTP Error 400: Bad Request')
        return None
