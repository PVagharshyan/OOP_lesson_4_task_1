class Book:
    def __init__(self, tittle: str, author: str) -> None:
        self._tittle = tittle
        self._author = author

    @property
    def tittle(self) -> str:
        return self._tittle

    @tittle.setter
    def tittle(self, new_tittle: str) -> None:
        self._tittle = new_tittle

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        return self._author

    def __str__(self):
        return f"tittle : {self.tittle}, auther : {self.author}"
