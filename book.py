class Book:
    def __init__(self,title,author,pages,current_page=0,is_open=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.is_open = is_open
        
    def __str__(self):
        return f"the book {self.title} is written by {self.author} and has {self.pages}"
    
    def open_book(self):
        self.is_open = True
    print("The book is now open.")
    
    def close_book(self):
        self.is_open = False
    print("The book is now closed.")
    
    def turn_page(self):
        if self.is_open:
            if self.current_page < self.pages:
                self.current_page += 1
                print(f"You are now on page {self.current_page}.")
            else:
                print("You are already at the end of the book.")
        else:
            print("Warning: The book is closed. Open it first.")

            
    def go_to_page(self,page_number):
                if self.is_open:
                    if 1 <= page_number <= self.pages:
                        self.current_page = page_number
                        print(f"You are now on page {self.current_page}.")
                    else:
                        print("That page number is out of range.")
                else:
                    print("Warning: The book is closed. Open it first.")


        
    def is_book_long (self):
        return self.pages > 300
        
book1 = Book("The Great Man", "Diego Gracias", 400, 0)
print(book1.title)
print(book1.author)
print(book1.pages)
print(book1)

book1.open_book()
book1.turn_page()
book1.turn_page()
book1.go_to_page(150)
book1.close_book()
print(book1.is_book_long())