from utils.library import Library
from utils.functions import input_book_details, input_member_details

library = Library()

book1 = input_book_details()
book2 = input_book_details()
member1 = input_member_details()

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)

library.list_books()
library.list_members()

member1.borrow_book(book1)
library.list_books()

member1.return_book(book1)
library.list_books()


