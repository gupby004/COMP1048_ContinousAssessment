#Activity3.1
from tensorflow.python.ops.gen_array_ops import tile_grad


class Clock:
    def __init__(self, hour, minute, second, duration):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__duration = duration

    def display_time(self):
        period = None
        if self.__duration:
            period = "am"
        else:
            period = "pm"
        print(f"{self.__hour}:{self.__minute}:{self.__second}{period}")

#Activity3.2

class Clock:
    def __init__(self, hour, minute, second, duration):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__duration = duration

    def set_hour(self, hour):
        self.__hour = hour

    def set_minute(self, minute):
        self.__minute = minute

    def set_second(self, second):
        self.__second = second

    def display_time(self):
        period = None
        if self.__duration:
            period = "am"
        else:
            period = "pm"
        print(f"{self.__hour}:{self.__minute}:{self.__second}{period}")

#Activity3.3

class Book:
    def __init__(self, title, author, page_count):
        self.__title = title
        self.__author = author
        self.__page_count = page_count

    def __str__(self):
        return f"{self.__title} was written by {self.__author} and is {self.__page_count} pages long."

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def display_books(self):
        print("--Collection--")
        for book in self.__books:
            print(book)
