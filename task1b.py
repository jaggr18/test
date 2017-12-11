class Book(object):
    isbn_counter = 9780000000000
    valid_isbn = []

    def __init__(self, title, author, isbn=None):
        self.__title = title
        self.__author = author
        if isbn is not None:
            if Book.check_isbn(str(isbn)):
                self.__isbn = isbn
            else:
                self.__isbn = Book.generate_isbn()
                Book.isbn_counter += 1
        else:
            self.__isbn = Book.generate_isbn()
            Book.isbn_counter += 1
        Book.valid_isbn.append(self.__isbn)

    @staticmethod
    def check_isbn(string):
        val = True
        if len(string) != 13:
            val = False
        elif not string.isdigit():
            val = False
        elif not string[:3] == '978':
            val = False
        elif int(string) in Book.valid_isbn:
            val = False
        return val

    @staticmethod
    def generate_isbn():
        isbn = Book.isbn_counter
        return isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn


book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 9780747532743)
book2 = Book("My Story", "Max Muster")
book3 = Book("My Story Part 2", "Max Muster", 970)
print(book1.get_isbn())
print(book1.get_title())
print(book1.get_author())
print(book2.get_isbn())
print(book3.get_isbn())
