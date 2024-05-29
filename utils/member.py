class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_checked_out:
            book.is_checked_out = True
            self.borrowed_books.append(book)
        else:
            print(f"Book '{book.title}' is already checked out.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_checked_out = False
            self.borrowed_books.remove(book)
        else:
            print(f"Book '{book.title}' was not borrowed by {self.name}.")
