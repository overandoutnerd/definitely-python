library = {
    "B101": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen"
    },
    "B102": {
        "title": "The Fellowship of The Ring",
        "author": "J.R.R. Tolkien"
    },
    "B103": {
        "title": "A Game of Thrones",
        "author": "George R.R. Martin"
    }
}

availableBooks = {"B101", "B102", "B103"}
issuedBooks = set()


def returnBook(bookId):
    if bookId in issuedBooks:
        issuedBooks.remove(bookId)
        availableBooks.add(bookId)
        returnStatus = "RETURNED"
    else:
        returnStatus = "NOT ISSUED"

    return returnStatus


choice = input("Enter operation (issue/return): ").lower().strip()
bookId = input("Enter Book ID: ").upper().strip()

if choice == "issue":

    if bookId in library and bookId in availableBooks:
        availableBooks.remove(bookId)
        issuedBooks.add(bookId)
        operationStatus = "BOOK ISSUED"
    elif bookId not in library:
        operationStatus = "INVALID BOOK ID"
    else:
        operationStatus = "BOOK ALREADY ISSUED"

elif choice == "return":

    if bookId in library:
        operationStatus = returnBook(bookId)
    else:
        operationStatus = "INVALID BOOK ID"

else:
    operationStatus = "INVALID OPERATION"


totalBooks = len(library)
availableCopies = len(availableBooks)
issuedCopies = len(issuedBooks)


print("\n====================================================")
print("        LIBRARY CATALOG STATUS DASHBOARD")
print("====================================================")
print("ID     | Book Title            | Status")
print("--------------------------------------------------")

for bookId in library:
    title = library[bookId]["title"]

    if bookId in availableBooks:
        status = "AVAILABLE"
    else:
        status = "ISSUED"

    print(f"{bookId:<6} | {title:<21} | {status}")

print("--------------------------------------------------")
print(f"Total Catalog Books   : {totalBooks}")
print(f"Available Copies      : {availableCopies}")
print(f"Issued Copies         : {issuedCopies}")
print(f"Operation Status      : {operationStatus}")
print("====================================================")