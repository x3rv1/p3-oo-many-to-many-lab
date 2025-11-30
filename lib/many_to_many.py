class Book:
    all = []

    def __init__(self, title: str):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string.")
        self._title = title.strip()
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise Exception("Title must be a non-empty string.")
        self._title = value.strip()

    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Author:
    all = []

    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string.")
        self._name = name.strip()
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise Exception("Name must be a non-empty string.")
        self._name = value.strip()

    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date: str, royalties: int):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")

        self._author = author
        self._book = book
        self._date = date.strip()
        self._royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise Exception("Date must be a non-empty string.")
        self._date = value.strip()

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise Exception("Royalties must be a non-negative integer.")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date: str):
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        # Filter by exact date string
        return [c for c in cls.all if c.date == date.strip()]