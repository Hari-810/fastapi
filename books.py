from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint") # creating a api endpoint using decorator
async def first_api():  # by default FastAPI take function as Asyncoronus here we giving explicitly
    return {"message" : "Hello World"}


#to view this api run the file and visit " 127.0.0.1:8000/api-endpoint "

# to view the swagger docs  visit  " 127.0.0.1:8000/docs "


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books") # /show_books also know as path
async def first_api():  
    return BOOKS


#--------------------------------------   Path parameters   ----------------------------------------                                        
                                        
# path parameters allows to get the dynamic value of the records
@app.get("/books/{book_title}")
async def read_book(book_title):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# to execute this try below url
#       http://127.0.0.1:8000/books/title%20one       

# over the above %20 is representing " "(space)


#--------------------------------------   Query parameters --------------------------------------   

@app.get("/query_subject/")
async def read_category_by_query(category):  # here category was my parameter
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# to execute this try below url
#       http://127.0.0.1:8000/books/?category=science    


# ? is known for query

#--------------------------------------   Path and Query parameters --------------------------------------  

@app.get("/book_and_author/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return
 
# here book_author was a path parameter and category was a query parameter

#-----------------------------------------------------------------------------------------------------------
#--------------------------------------   POST Request   --------------------------------------  

from fastapi import FastAPI, Body
# POST method requires body and GET doesn't needs that


@app.post("/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    
    
# run the server give body content as dict of values
#    ex:   {"title": "Title Seven", "author": "Author Six", "category": "History"}  always use ""

#-----------------------------------------------------------------------------------------------------------
#--------------------------------------   PUT Request   --------------------------------------  

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            
#-----------------------------------------------------------------------------------------------------------
#--------------------------------------   DELETE Request   --------------------------------------  


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

#-----------------------------------------------------------------------------------------------------------
#--------------------------------------  Assignment  --------------------------------------  


    """
    Assignment
    
    1. Create a new API Endpoint that can fetch all books from a specific author 
    using either Path Parameters or Query Parameters.
    """
 
 
# Query parameter    
@app.get("/author_books_query")
async def author_books_query(author):
    author_books = []
    for book in BOOKS:
        if book.get("author") == author:
            author_books.append(book)
    if len(author_books) == 0:
        return "No Books were founded"
    else:
        return author_books
    
    
@app.get("/author_books_path/{autor}")
async def author_books_path(author):
    author_books = []
    for book in BOOKS:
        if book.get("author") == author:
            author_books.append(book)
    if len(author_books) == 0:
        return "No Books were founded"
    else:
        return author_books
    