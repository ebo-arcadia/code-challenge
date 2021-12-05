# When we want to access a method without an object, you can use the @staticmethod
# @staticmethod makes the method immediately below it a static method.
# A static method does not belong to the object and hence does not have the `self` attribute.
# In other words the first parameter is NOT considered as an implicit reference to the object
# and hence it cannot access the self attributes of an object of its class.

class Book:
    __no_of_categories = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def set_no_of_categories(self):
        Book.__no_of_categories += 1

    @staticmethod
    def get_all_categories():
        return Book.__no_of_categories

    def __str__(self):
        return "The new book is titled: " + self.title + " and it is written by " + self.author


new_book = Book("Denial of death", "Ernest Becker")
new_book.set_no_of_categories()
another_new_book = Book("Modern man searching for meaning", "Carl Jung")
another_new_book.set_no_of_categories()
print(new_book.__str__())
print(another_new_book.__str__())
print("get_all_categories method is called via class name", Book.get_all_categories())
print("get_all_categories method is invoked using object reference: ", Book.get_all_categories())

# it is good practice to invoke static method using class name instead of object reference
