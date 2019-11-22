import sqlite3
class sql_book():
    def __init__(self):
        self.con = sqlite3.connect("Book.db")
        self.cur = self.con.cursor()
    def CreateTable(self):
        self.cur.execute("DROP TABLE IF EXISTS BOOKINFO")
        sql = """CREATE TABLE BOOKINFO(
                BOOKNAME CHAR(100) NOT NULL,
                AUTHOR CHAR(50),
                PUBLISH CHAR(50),
                ISBN  CHAR(100) UNIQUE,
                INVENTORY  CHAR(50),
                CANBORROW CHAR(50),
                TYPE CHAR(50),
                ROWID integer PRIMARY KEY autoincrement)"""
        self.cur.execute(sql)
        sqlist = ['''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("数据挖掘与机器学习","徐桂秋","人民邮电出版社","978-7-115-50345-2","100","100","YES")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("python编程基础与应用","林子雨","电子工业出版社","978-7-115-50345-3","100","100","YES")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                              VALUES("数据挖掘","徐桂秋","人民邮电出版社","978-7-115-50345-4","100","100","YES")''']
        try:
            for sql_ in sqlist:
                self.cur.execute(sql_)
        except BaseException as e:
            print("数据插入失败：", e)
            self.con.rollback()
        finally:

            self.con.commit()
            # BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE
    def Insert(self, BookName, Author, Publish, ISBN, INVENTORY, CANBORROW, Type):
        sql = f'''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("{BookName}","{Author}","{Publish}","{ISBN}","{INVENTORY}","{CANBORROW,}","{Type}")'''
        try:
            self.cur.execute(sql)
        except BaseException as e:
            print("数据插入失败：", e)
            self.con.rollback()
        finally:
            self.con.commit()
    def Query(self, Key, Type):
        if Type == '书  名':
            sql = f"""SELECT * FROM BOOKINFO WHERE BOOKNAME LIKE '%{Key}%'"""
        elif Type == '作  者':
            sql = f"""SELECT * FROM BOOKINFO WHERE AUTHOR LIKE '%{Key}%'"""
        else:
            sql = f"""SELECT * FROM BOOKINFO WHERE PUBLISH LIKE '%{Key}%'"""
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            return results
        except BaseException as e:
            print("数据查询失败:", e)
        finally:
            self.con.commit()
    def Update(self):
        pass
    def Delete(self):
        pass
    def close(self):
        self.cur.close()
        self.con.close()
