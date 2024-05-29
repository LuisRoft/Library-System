class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def list_books(self):
        for book in self.books:
            status = 'Available' if not book.is_checked_out else 'Checked out'
            print(f"{book.title} by {book.author} - {status}")

    def list_members(self):
        for member in self.members:
            print(f"Member: {member.name}, ID: {member.member_id}")