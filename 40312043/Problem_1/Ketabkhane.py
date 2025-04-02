class Book :
    def __init__(self , title , author) :
        self.title = title
        self.author = author
        self.status = "Avaliable"
    
    def borrow(self) :
        if self.status == "Avaliable" :
            self.status = "Borrowed"
            print(f"Borrowed {self.title}")
        else :
            print("already borrowed !")
    
    def return_book(self) :
        if self.status == "Borrowed" :
            self.status = "Avaliable"
            print(f"Returned {self.title}")
        else :
            print("the book not borrowed !")
    
    def get_details (self) :
        return f"{self.title} by {self.author} ({self.status})"

books = []

class Library:
    def __init__(self) :
        pass
    def add_book(self , title , author) :
        book = Book(title , author)
        books.append(book)
        print(f"Added {title} by {author}")
   
    def borrow_book(self, title):
        for book in books:
            if book.title == title :
                book.borrow()
                return

    def return_book(self, title):
        for book in books:
            if book.title == title:
                book.return_book()

    def show_books(self) :
        print("Library Books")
        for book in books :
            print(book.get_details())

commands = []

def input_command():
    while True:
        command = input().strip()
        if command == "":
            break
        commands.append(command)

def process_command(library) :
    for command in commands :
        if command.startswith("ADD") :
            parts = command.split('"')
            if len(parts) >= 3:
                title = parts[1].strip()
                author = parts[3].strip()
            library.add_book(title , author)
        elif command.startswith("BORROW") :
            parts = command.split('"')
            if len(parts) >= 3:
                title = parts[1].strip()
            library.borrow_book(title)
        elif command.startswith("RETURN") :
            parts = command.split('"')
            if len(parts) >= 3:
                title = parts[1].strip()
            library.return_book(title)
        elif command == "SHOW" :
            library.show_books()
        elif command == "" :
            break
    
def main() :
    library = Library()
    input_command()
    process_command(library)

if __name__ == '__main__':
    main()