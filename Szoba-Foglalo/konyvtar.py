class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    return f"A könyv '{book.title}' sikeresen kölcsönözve lett."
                else:
                    return f"A könyv '{book.title}' jelenleg nem elérhető."
        return f"A könyv '{title}' nem található a könyvtárban."

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                return f"A könyv '{book.title}' sikeresen visszahozva."
        return f"A könyv '{title}' nem található a könyvtárban."


library = Library()

book1 = Book("A Gyűrűk Ura", "J.R.R. Tolkien")
book2 = Book("Harry Potter és a Bölcsek Köve", "J.K. Rowling")

library.add_book(book1)
library.add_book(book2)

print(library.borrow_book("A Gyűrűk Ura"))  # A könyv 'A Gyűrűk Ura' jelenleg nem elérhető.
print(library.borrow_book(
    "Harry Potter és a Bölcsek Köve"))  # A könyv 'Harry Potter és a Bölcsek Köve' jelenleg nem elérhető.
print(library.borrow_book(
    "Harry Potter és a Bölcsek Köve"))  # A könyv 'Harry Potter és a Bölcsek Köve' sikeresen kölcsönözve lett.
print(library.return_book(
    "Harry Potter és a Bölcsek Köve"))  # A könyv 'Harry Potter és a Bölcsek Köve' sikeresen visszahozva.
