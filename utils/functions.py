from utils.book import Book
from utils.member import Member

def input_book_details():
    print('----------------------------------------')
    title = input("Ingrese el título del libro: ")
    author = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")
    print('----------------------------------------')
    return Book(title, author, isbn)

def input_member_details():
    print('----------------------------------------')
    name = input("Ingrese el nombre del miembro: ")
    member_id = input("Ingrese el ID del miembro: ")
    print('----------------------------------------')
    return Member(name, member_id)