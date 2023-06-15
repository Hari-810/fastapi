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



