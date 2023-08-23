import book
import copy

class Library:
    def __init__(self, books: list = []):
        self._books = books

    @property
    def books(self) -> list:
        return copy.deepcopy(self._books)

    def create_book(self, book: book.Book) -> None:
        self._books.append(book)

    def __getitem__(self, index: int) -> str:
        if (index < 0 or index > len(self.books)):
            raise IndexError("Error: out of range")
        return self._books[index]

    def __setitem__(self, index: str, value: book.Book) -> None:
        if (index < 0 or index > len(self.books)):
            raise IndexError("Error: out of range")
        self._books[index] = value

    def __delitem__(self, index: int) -> None:
        if (index < 0 or index > len(self.books)):
            raise IndexError("Error: out of range")
        del self._books[index]

    def __len__(self) -> int:
        return len(self._books)
