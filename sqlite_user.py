import sqlite3
class sql_user(object):
    def __init__(self):
        self.con = sqlite3.connect("User.db")
        self.cur = self.con.cursor()
    def CreateTable(self):
        self.cur.execute("DROP TABLE IF EXISTS USERINFO")
        sql = """CREATE TABLE USERINFO(
                  ID CHAR(50) UNIQUE,
                  PERMISSIONS CHAR(50),
                  USERNAME CHAR(50),
                  USERPASSWORD CHAR(50) NOT NULL,
                  PEOPLENAME CHAR(50),
                  BALANCE CHAR(50),
                  ABLE CHAR(50),
                  ROWID integer PRIMARY KEY autoincrement)"""
        self.cur.execute(sql)
        sqlist = ["""INSERT INTO USERINFO(ID, PERMISSIONS, USERNAME, USERPASSWORD, PEOPLENAME, BALANCE, ABLE)
                    VALUES("A123456","A","123456","123456","张三","0","3")""",
                  """INSERT INTO USERINFO(ID, PERMISSIONS, USERNAME, USERPASSWORD, PEOPLENAME, BALANCE, ABLE)
                    VALUES("A111111","A","111111","111111","王五","0","3")""",
                  """INSERT INTO USERINFO(ID, PERMISSIONS, USERNAME, USERPASSWORD, PEOPLENAME, BALANCE, ABLE)
                    VALUES("B111111","B","111111","123456","管理员1","","3")""",
                  """INSERT INTO USERINFO(ID, PERMISSIONS, USERNAME, USERPASSWORD, PEOPLENAME, BALANCE, ABLE)
                    VALUES("B666666","B","666666","666666","管理员2","","3")"""]
        try:
            for sqli in sqlist:
                self.cur.execute(sqli)
        except BaseException as e:
            print("数据查询失败:", e)
            self.con.rollback()
        finally:
            self.flag = False
            self.con.commit()
    def QueryUser(self, Key, Type):
        sql = f"""SELECT * FROM USERINFO WHERE  PERMISSIONS ='{Type}' AND USERNAME='{Key}'"""
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            return results
        except BaseException as e:
            print("数据查询失败:", e)
        finally:
            self.con.commit()
    def Insert(self, BookName, Author, Publish, ISBN, INVENTORY, Type):
        sql = f'''INSERT INTO BOOKINFO(BOOKNAME,AUTHOR,PUBLISH,ISBN,INVENTORY,TYPE)
                    VALUES("{BookName}","{Author}","{Publish}","{ISBN}","{INVENTORY}","{Type}")'''
        try:
            self.cur.execute(sql)
        except BaseException as e:
            print("数据插入失败：", e)
            self.con.rollback()
        finally:
            self.con.commit()
    # USERPASSWORD-1,BALANCE-2,ABLE-3,BORROW-4,RETURN-5
    # ID, PERISSIONS, USERNAME, USERPASSWORD, PEOPLENAME, BALANCE, ABLE
    def Update(self, UserName, num, new):
        if   num ==1:
            sql = f"""UPDATE USERINFO SET USERPASSWORD = '{new}' where USERNAME = {UserName}"""
        elif num ==2:
            sql = f"""UPDATE USERINFO SET BALANCE = '{new}' where USERNAME = {UserName}"""
        else:
            sql = f"""UPDATE USERINFO SET ABLE    = '{new}' where USERNAME = {UserName}"""
        try:
            # 执行sql语句创建表
            self.cur.execute(sql)
            results = self.cur.fetchall()
        except BaseException as e:
            print("数据修改失败:", e)
            self.con.rollback()
        finally:
            self.con.commit()
    def close(self):
        self.cur.close()
        self.con.close()