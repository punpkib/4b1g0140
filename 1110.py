class Library:
    def __init__(self, name, location, books):
        self.name = name
        self.location = location
        self.books = books

    def display_library_info(self):
        print(f"圖書館名稱: {self.name}")
        print(f"地點: {self.location}")
        print(f"書籍數量: {len(self.books)}")
        print("-----------------------------")

    def add_book(self, book_title):
        self.books.append(book_title)
        print(f"書籍 '{book_title}' 已成功新增。")

    def borrow_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            print(f"書籍 '{book_title}' 已成功借閱。")
        else:
            print(f"圖書館中沒有 '{book_title}' 這本書。")

# 建立三個圖書館物件
library1 = Library("城市圖書館", "市中心", ["書籍1", "書籍2", "書籍3"])
library2 = Library("大學圖書館", "大學校園", ["書籍4", "書籍5", "書籍6"])
library3 = Library("社區圖書館", "社區中心", ["書籍7", "書籍8", "書籍9"])

# 呼叫副函式共9次
library1.display_library_info()
library1.add_book("新書")
library1.borrow_book("書籍1")
library1.display_library_info()

library2.display_library_info()
library2.add_book("另一本書")
library2.borrow_book("書籍5")
library2.display_library_info()

library3.display_library_info()
library3.add_book("額外的書")
library3.borrow_book("書籍9")
library3.display_library_info()

