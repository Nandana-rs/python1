class Publisher:
    def __init__(self, Pname):
        self.Pname = Pname
    def display(self):
        print("Publisher name is:", self.Pname)
class Book(Publisher):
    def __init__(self, Pname, title, author):
        Publisher.__init__(self, Pname)
        self.title = title
        self.author = author
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
class Python(Book):
    def __init__(self, Pname, title, author, price, no_of_pages):
        Book.__init__(self, Pname, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publisher:",self.Pname)
        print("Price:", self.price)
        print("No of pages:", self.no_of_pages)
b1 = Python("Penguins", "History", "Nandana", 2000, 320)
b1.display()