
import functions


from flask import Flask, render_template, request


import urllib.error
# Create an instance of Flask
app = Flask(__name__)


# Create a view function for /
@app.route('/')
def index():
    return render_template('index.html')




# Create a view function for /results
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        result = request.form.get('genre', '')
        if result:

            book = functions.safe_find_book(result)
            title = book["title"]
            author = book["author_name"][0]
            id = str(book["cover_i"])
            url = "https://covers.openlibrary.org/a/id/" + id + "-L.jpg"
            return render_template('results.html', title=title, author=author, url=url)
        else:
            book = functions.safe_find_book("fiction")
            title = book["title"]
            author = book["author_name"][0]
            id = str(book["cover_i"])
            url = "https://covers.openlibrary.org/a/id/" + id + "-L.jpg"
            return render_template('results.html', title=title, author=author, url=url)

    if request.method == 'GET':
        return "Wrong HTTP method", 400

    return "Wrong HTTP method", 400


if __name__ == '__main__':
    app.run(debug=True)
