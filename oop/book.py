class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1
    
    def move_bookmark(self, page_number):
        self.bookmarked_page = page_number

    def turn_page(self, forward):
        if forward:
            self.current_page += 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def __len__(self):
        return self.num_pages

    def go_to_page(self, page_number):
        self.current_page = page_number

    def restart_book(self):
        self.current_page = 1
        print("Restarted book")

book_1 = Book("Cats", "Real Person", 150, 1)
print(f"Current page is: {book_1.current_page}")

page_number = int(input("Which page do you want to bookmark? "))
book_1.move_bookmark(page_number)
print(f"Current page is {book_1.current_page}, Bookmark is: {book_1.bookmarked_page}")


page_number = int(input("Which page do you want to go to? "))
book_1.go_to_page(page_number)
print(book_1.current_page, book_1.bookmarked_page)

if book_1.current_page == len(book_1):
    book_1.restart_book()







