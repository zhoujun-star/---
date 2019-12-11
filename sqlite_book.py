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
                    VALUES("数据挖掘与机器学习","徐桂秋","人民邮电出版社","978-7-115-50345-2","100","100","计算机技术")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("python编程基础与应用","林子雨","电子工业出版社","978-7-115-50345-3","100","100","计算机技术")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("数据挖掘","徐桂秋","人民邮电出版社","978-7-115-50345-4","100","100","计算机技术")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("大学物理","渊小春","同济大学出版社","978-7-115-50345-5","100","100","社会科学")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("恶之花","[法]波德莱尔","江西人民出版社","978-7-115-50345-6","100","100","文学教育")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("摄影","李安强,郑强","清华大学出版社","978-7-115-50345-7","100","100","摄影影视")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("音乐教育论","郭声键","湖南文艺出版社","978-7-115-50345-8","100","100","音乐")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("藏馆 创刊号","邱双炯","藏馆编辑部","978-7-115-50345-9","100","100","期刊")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("失去的胜利","冯.埃里希.曼施泰因","民主与建设出版社","978-7-115-50345-10","100","100","军事科学")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("钢铁是怎样炼成的","尼古拉.奥斯特洛夫斯基","文化发展出版社","978-7-115-50345-11","100","100","经典著作")''',
                  '''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,CANBORROW,TYPE)
                    VALUES("育儿百科","松田道雄","华夏出版社","978-7-115-50345-12","100","100","生活休闲")'''
                  ]
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

    def QueryAll(self):
        sql = f"""SELECT * FROM BOOKINFO;
        """
        book_dictionary = {"经典著作":[], "社会科学":[],"军事科学":[],"计算机技术":[],"生活休闲":[],"期刊":[],"文学教育":[],
                           "音乐":[], "摄影影视":[]}
        self.cur.execute(sql)
        cp_book_dictionary = book_dictionary
        for row in self.cur.fetchall():
            print(row)
            for key in book_dictionary.keys():
                if row[-2] == key:
                    cp_book_dictionary[key].append(row[0])
                    break

        print(cp_book_dictionary)
        return cp_book_dictionary
    def QueryByBookName(self, name):
        sql = f"""SELECT * FROM BOOKINFO WHERE BOOKNAME LIKE '%{name}%'"""

        self.cur.execute(sql)
        return self.cur.fetchone()

    def Update(self):
        pass
    def Delete(self):
        pass
    def close(self):
        self.cur.close()
        self.con.close()
