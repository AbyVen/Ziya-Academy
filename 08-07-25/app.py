from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = []
reviews = {}

@app.route('/')
def index():
    return render_template('index.html', books=books, reviews=reviews)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        description = request.form['description']
        book_id = len(books)
        books.append({'id': book_id, 'title': title, 'author': author, 'description': description})
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/add_review/<int:book_id>', methods=['GET', 'POST'])
def add_review(book_id):
    if request.method == 'POST':
        review = request.form['review']
        if book_id not in reviews:
            reviews[book_id] = []
        reviews[book_id].append(review)
        return redirect(url_for('index'))
    book = books[book_id]
    return render_template('add_review.html', book=book)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    global books, reviews
    books = [book for book in books if book['id'] != book_id]
    reviews.pop(book_id, None)
    # Reassign IDs
    for idx, book in enumerate(books):
        book['id'] = idx
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
