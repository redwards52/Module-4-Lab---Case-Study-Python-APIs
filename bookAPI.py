"""Regine Benton
source: Module 4 Lab - Case Study: Python APIs
What I need to do is make sure that every thing is correct
then i need to do the terminal commands to add onto the 
API json file. I think I need stackoverflow.
The website that the the teacher assigned for me to use.
https://www.youtube.com/watch?v=qbLc5a9jdXo
"""
import requests

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# Initializing app
app = Flask(__name__)

# API calls the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datab.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Creating a Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique= True, nullable = False)
    publisher = db.Column(db.String(80), unique= True, nullable= False)
    
    
    def __repr__(self):
        return f"{self.name} - {self.description}"
        
@app.route('/')
def index():
    return 'Hello'

# Get all the books
@app.route('/books')
def get_books():
    books = book.query.all()
    output = []
    for book in books:
        book_data = {'id': book.id, 'name': book.name,
                     'author':book.author,
                     'publisher':book.publisher, }
        output.append(book_data)
    return{"books":output}

# Get a specific book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book= Book.query.get_or_404(id)
    return {'id': book.id, 'name': book.name,
                     'author':book.author,
                     'publisher':book.publisher,}

# Add a book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = Book(name= request.json['name'],)
    db.session.add(new_book)
    db.session.commit()
    return {'id': new_book.id}, 201

# Delete a book
@app.route('/books/<id>', methods = ['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return{"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book is deleted."}
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)