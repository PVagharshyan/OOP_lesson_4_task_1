import book
import library

def main() -> None:
    print('test')
    books = [book.Book("tittle", "author") for i in range(10)]
    lib = library.Library(books)
    arr = lib.books
    for item in arr:
        print(item)
    lib.create_book(book.Book('tittle_1', 'auther_1'))
    print('---test_create_book----')
    arr = lib.books
    for item in arr:
        print(item)
    print('---del_book---')
    del lib[len(lib.books) - 1]
    arr = lib.books
    for item in arr:
        print(item)
    print('---assign_book---- ')
    lib[0] = book.Book("tittle_assigned", "auther_assigned")
    arr = lib.books
    for item in arr:
        print(item)
    print('---select_book_i---')
    print(lib[0])
    print('----len_library-----')
    print("len:", len(lib))
if __name__ == "__main__":
    main()
