from tkinter import *
from tkinter import ttk
from sqlite_book import sql_book
from sqlite_user import sql_user


class admin_system(object):
    def __init__(self, master, name):
        self.root = master
        self.root.geometry("800x600")
        canvas = Canvas(self.root)
        canvas.create_line(0, 27, 2000, 27, tags="line")
        canvas.pack(side=TOP, fill=X, pady=10)
        Button(canvas, text = "图书操作",relief=GROOVE,command=self.create_windows1).pack(side=LEFT, padx =10)
        Button(canvas, text = "用户操作",relief=GROOVE,command=self.create_windows2).pack(side=LEFT, padx =5)
        Label(canvas,text=f"{name}，欢迎进入图书管理系统").pack(side=LEFT, expand= YES)
        self.Frm_Book = Frame(self.root)
        self.Frm_Book.pack(expand=YES, fill=BOTH)
        frm_2 = Frame(self.Frm_Book)
        frm_2.pack(side=LEFT,fill = Y,padx= 10)
        self.varSearchBook = StringVar()
        entry=Entry(frm_2, textvariable=self.varSearchBook)
        entry.pack(fill=X,pady=10)
        button_search = Button(entry, relief=GROOVE, text="搜索", command=self.search_book)
        button_search.pack(side="right")
        type = ["经典著作","社会科学","军事科学","计算机技术","生活休闲","期刊","文学教育","音乐","摄影影视"]
        self.tree = ttk.Treeview(frm_2, show="tree")
        for type_ in type:
            self.tree.insert("", 0, type_, text=type_)
        book = sql_book()
        self.book_classified_dictionary = book.QueryAll()
        book.close()
        for key in self.book_classified_dictionary:
            for book in self.book_classified_dictionary[key]:
                self.tree.insert(key, 0, book,text=book,)

        # 分类框滚动条
            # y
        yscrollbar = Scrollbar(frm_2, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side=RIGHT, fill=Y)
            # x
        xscrollbar = Scrollbar(frm_2, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=xscrollbar.set)
        xscrollbar.pack(side=BOTTOM, fill=X)

        self.tree.pack(side=LEFT, expand=YES, fill=Y)
        def click(event):
            book = sql_book()
            iidy = self.tree.identify_row(event.y)
            if iidy in self.book_classified_dictionary:
                pass
            else:
                selected_book = book.QueryByBookName(iidy)
                self.var1.set(selected_book[0])
                self.var2.set(selected_book[1])
                self.var3.set(selected_book[2])
                self.var4.set(selected_book[3])
                self.var5.set(selected_book[4])
                self.var6.set(selected_book[5])
            book.close()


        self.tree.bind("<Button-1>", click)

        frm_3 = Frame(self.Frm_Book)
        frm_3.pack(expand=YES)
        frm_31 = Frame(frm_3)
        frm_31.pack(side=LEFT,fill=Y)
        Label(frm_31, text="书   名：",width=8,font=('Arial',20),justify=LEFT).pack(side=TOP, padx=10,pady=10)
        Label(frm_31, text="作   者：",width=8,font=('Arial',20),justify=LEFT).pack(side=TOP, padx=10,pady=10)
        Label(frm_31, text="出 版 社：",width=8,font=('Arial',20),justify=LEFT).pack(side=TOP, padx=10,pady=10)
        Label(frm_31, text="ISBN：",width=8,font=('Arial',20),justify=LEFT).pack(side=TOP, padx=10,pady=5)
        Label(frm_31, text="库   存：",width=8,font=('Arial',20),justify=LEFT).pack(side=TOP, padx=10,pady=10)
        Label(frm_31, text="已   借：",width=8,font=('Arial',20),justify=LEFT).pack(side=TOP, padx=10,pady=10)
        # 输入框框架
        frm_32 = Frame(frm_3)
        frm_32.pack(side=LEFT,fill=Y, expand=YES)
        # 编辑框架
        frm_33 = Frame(frm_32)
        frm_33.pack(side="right", fill=Y, expand=YES)
        # 结果显示区输入框
        self.var1 = StringVar(value="大数据挖掘与计算")
        self.et1 = Entry(frm_32,textvariable = self.var1,font=('Arial',20), state=DISABLED)
        self.et1.pack(side=TOP, padx=10,pady=10)
        self.var2 = StringVar(value="李白")
        self.et2 = Entry(frm_32, textvariable=self.var2,font=('Arial',20), state=DISABLED)
        self.et2.pack(side=TOP, padx=10, pady=10)
        self.var3 = StringVar(value="重庆第二师范学院")
        self.et3 = Entry(frm_32, textvariable=self.var3,font=('Arial',20), state=DISABLED)
        self.et3.pack(side=TOP, padx=10, pady=10)
        self.var4 = StringVar(value="123456789")
        self.et4 = Entry(frm_32, textvariable=self.var4, font=('Arial',20), state=DISABLED)
        self.et4.pack(side=TOP, padx=10, pady=10)
        self.var5 = StringVar(value="99")
        self.et5 = Entry(frm_32, textvariable=self.var5, font=('Arial',20), state=DISABLED)
        self.et5.pack(side=TOP, padx=10, pady=10)
        self.var6 = StringVar(value="0")
        self.et6 = Entry(frm_32, textvariable=self.var6, font=('Arial',20), state=DISABLED)
        self.et6.pack(side=TOP, padx=10, pady=10)
        # 编辑区

        self.lb1 = Label(frm_33, text="编辑")
        self.lb1.pack(side="top", padx=20, pady=17)
        self.lb1.bind("<Button-1>", lambda x: self.bindOfEdit(self, 1))
        #self.lb1.bind("<Enter>", lambda x: self.bindOfEditEnterColor(self, 1))
        self.lb2 = Label(frm_33, text="编辑")
        self.lb2.pack(side="top", padx=20,pady=16)
        self.lb2.bind("<Button-1>", lambda x: self.bindOfEdit(self, 2))
        #self.lb2.bind("<Enter>", lambda x: self.bindOfEditEnterColor(self, 2))
        self.lb3 = Label(frm_33, text="编辑")
        self.lb3.pack(side="top", padx=20,pady=16)
        self.lb3.bind("<Button-1>", lambda x: self.bindOfEdit(self, 3))
        #self.lb3.bind("<Enter>", lambda x: self.bindOfEditEnterColor(self, 3))
        self.lb4 = Label(frm_33, text="编辑")
        self.lb4.pack(side="top", padx=20,pady=16)
        self.lb4.bind("<Button-1>", lambda x: self.bindOfEdit(self, 4))
        #self.lb4.bind("<Enter>", lambda x: self.bindOfEditEnterColor(self, 4))
        self.lb5 = Label(frm_33, text="编辑")
        self.lb5.pack(side="top", padx=20,pady=16)
        self.lb5.bind("<Button-1>", lambda x: self.bindOfEdit(self, 5))
        #self.lb5.bind("<Enter>", lambda x: self.bindOfEditEnterColor(self, 5))
        self.lb6 = Label(frm_33, text="编辑")
        self.lb6.pack(side="top", padx=20, pady=16)
        self.lb6.bind("<Button-1>", lambda x: self.bindOfEdit(self, 6))
        #self.lb6.bind("<Enter>", lambda x: self.bindOfEditEnterColor(self, 6))
        frm_33 = Frame(self.Frm_Book)
        frm_33.pack(expand=YES)
        Button(frm_33, text="添加图书", relief=GROOVE,font=('Arial',20)).pack(side=LEFT,padx=20)
        Button(frm_33, text="修改图书", relief=GROOVE,font=('Arial',20)).pack(side=LEFT,padx=20)
        Button(frm_33, text="删除图书", relief=GROOVE,font=('Arial',20)).pack(side=LEFT,padx=20)
##
        self.lbs = [self.lb1, self.lb2, self.lb3, self.lb4, self.lb5, self.lb6]
        self.ets = [self.et1, self.et2, self.et3, self.et4, self.et5, self.et6]

        # 用户操作界面
        self.Frm_User = Frame(self.root)
        frm_4 = Frame(self.Frm_User)
        frm_4.pack(side=LEFT,fill=Y, padx=10)
        Entry(frm_4).pack(fill=X,pady=10)
        Listbox(frm_4).pack(side=LEFT,fill=Y,expand=YES)
        frm_5 = Frame(self.Frm_User)
        frm_5.pack(expand=YES)
        frm_51 = Frame(frm_5)
        frm_51.pack(side=LEFT, expand=YES, fill=Y)
        Label(frm_51, text="姓   名：", width=8, font=('Arial', 20), justify=LEFT).pack(side=TOP, padx=10, pady=10)
        Label(frm_51, text="学   校：", width=8, font=('Arial', 20), justify=LEFT).pack(side=TOP, padx=10, pady=10)
        Label(frm_51, text="账   号：", width=8, font=('Arial', 20), justify=LEFT).pack(side=TOP, padx=10, pady=10)
        Label(frm_51, text="密   码：", width=8, font=('Arial', 20), justify=LEFT).pack(side=TOP, padx=10, pady=10)
        Label(frm_51, text="额   度：", width=8, font=('Arial', 20), justify=LEFT).pack(side=TOP, padx=10, pady=5)
        Label(frm_51, text="已   借：", width=8, font=('Arial', 20), justify=LEFT).pack(side=TOP, padx=10, pady=10)
        frm_52 = Frame(frm_5)
        frm_52.pack(side=LEFT, expand=YES, fill=Y)
        var1 = StringVar(value="张三")
        Entry(frm_52, textvariable=var1, state=DISABLED, font=('Arial', 20)).pack(side=TOP, padx=20, pady=10)
        var2 = StringVar(value="重庆第二师范学院")
        Entry(frm_52, textvariable=var2, state=DISABLED, font=('Arial', 20)).pack(side=TOP, padx=20, pady=10)
        var3 = StringVar(value="123456")
        Entry(frm_52, textvariable=var3, state=DISABLED, font=('Arial', 20)).pack(side=TOP, padx=20, pady=13)
        var4 = StringVar(value="123456789")
        Entry(frm_52, textvariable=var4, state=DISABLED, font=('Arial', 20)).pack(side=TOP, padx=20, pady=10)
        var5 = StringVar(value="100")
        Entry(frm_52, textvariable=var5, state=DISABLED, font=('Arial', 20)).pack(side=TOP, padx=20, pady=10)
        var6 = StringVar(value="0")
        Entry(frm_52, textvariable=var6, state=DISABLED, font=('Arial', 20)).pack(side=TOP, padx=20, pady=10)
        frm_53 = Frame(self.Frm_User)
        frm_53.pack(expand=YES)
        Button(frm_53, text="添加用户", relief=GROOVE, font=('Arial', 20)).pack(side=LEFT, padx=10)
        Button(frm_53, text="更新用户", relief=GROOVE, font=('Arial', 20)).pack(side=LEFT, padx=10)
        Button(frm_53, text="删除用户", relief=GROOVE, font=('Arial', 20)).pack(side=LEFT, padx=10)
        Button(frm_53, text="借阅记录", relief=GROOVE, font=('Arial', 20)).pack(side=LEFT, padx=10)
    def search_book(self):
        for key in self.book_classified_dictionary:
            if self.varSearchBook.get() in self.book_classified_dictionary[key]:

                book = sql_book()
                bookName = self.varSearchBook.get()
                selected_book = book.QueryByBookName(bookName)
                book.close()
                self.var1.set(selected_book[0])
                self.var2.set(selected_book[1])
                self.var3.set(selected_book[2])
                self.var4.set(selected_book[3])
                self.var5.set(selected_book[4])
                self.var6.set(selected_book[5])
                break
            else:
                self.var1.set("无")
                self.var2.set("无")
                self.var3.set("无")
                self.var4.set("无")
                self.var5.set("无")
                self.var6.set("无")

    def bindOfEdit(event, self, number):

        i = 0
        for et in self.ets:
            if i == number-1:
                et["state"] = "normal"
            else:
                et["state"] = "disabled"
            i += 1

    # def bindOfEditEnterColor(event, self, number):
    #     i=0
    #     for lb in self.lbs:
    #         if i == number-1:
    #             lb["fg"] = "red"
    #         else:
    #             lb["fg"] = "black"
    #         i += 1

    def addBook(self):
        pass
    def delete(self):
        pass
    def alterBook(self):
        pass
    def create_windows1(self):
        self.Frm_Book.pack_forget()
        self.Frm_User.pack_forget()
        self.Frm_Book.pack(expand=YES, fill=BOTH)

    def create_windows2(self):
        self.Frm_Book.pack_forget()
        self.Frm_User.pack_forget()
        self.Frm_User.pack(expand=YES, fill=BOTH)


if __name__ == '__main__':
    root = Tk()
    start = admin_system(root,"kljdk")
    root.mainloop()
