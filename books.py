from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


#Create a class for perfrom Data vaildation using pydantic
class BookRequest(BaseModel):  # inherting the Basemodel of pydantic 
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)  #gt - greater than, lt - lesser than
    published_date: int = Field(gt=1999, lt=2031)

# Create a general schema messaage to show in flassger
    class Config:
        schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'persone name',
                'description': 'A new description of a book',
                'rating': 5,
                'published_date': 2029
            }
        }   
BOOKS = [
    Book(id=1, title='Computer Science Pro', author='codingwithroby', description='A very nice book!', rating=5, published_date=2030),
    Book(id=2, title='Be Fast with FastAPI', author='codingwithroby', description='A great book!', rating=5, published_date=2030),
    Book(id=3, title='Master Endpoints', author='codingwithroby', description='An awesome book!', rating=5, published_date=2029),
    Book(id=4, title='HP1', author='Author 1', description='Book Description', rating=2, published_date=2028),
    Book(id=5, title='HP2', author='Author 2', description='Book Description', rating=3, published_date=2027),
    Book(id=6, title='HP3', author='Author 3', description='Book Description', rating=1, published_date=2026)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


# sample body content
"""
    {
  "id": 7,
  "title": "New Book",
  "author": "John Doe",
  "description": "A fantastic book",  
  "rating": 4,
  "published_date": 2023
}
"""


