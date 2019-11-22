from sqlite_book import sql_book
from sqlite_user import sql_user
if __name__ == '__main__':
    BOOK = sql_book()
    BOOK.CreateTable()
    BOOK.close()
    User = sql_user()
    User.CreateTable()
    User.close()