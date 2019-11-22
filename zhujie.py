from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from sqlite_book import sql_book
from sqlite_user import sql_user
from admin import admin_system
class system(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("图书管理系统")
        scn_w, scn_h = self.root.maxsize()
        cen_x = (scn_w - 400)/2
        cen_y = (scn_h - 300)/2
        size_xy = '400x300+%d+%d' % (cen_x, cen_y)
        self.root.geometry(size_xy)
        self.root.resizable(0,0) #防止用户调整尺寸
        self.user_Varname = StringVar()
        self.user_varpassword = StringVar()
        self.content_tip = StringVar()
        self.var = StringVar(value="A")
        self.flag = True
        self.Type = None
        self.name = None
        self.admin_name = None
        self.login()

    # 登陆界面函数
    def login(self):
        Label(self.root, text="欢迎使用图书管理系统", height=5, font=10).pack(side="top")
        frm_user = Frame(self.root)
        frm_user.pack()
        Radiobutton(frm_user, text="读  者", variable= self.var, value="A").pack(side="left", padx=30)
        Radiobutton(frm_user, text="管理员", variable= self.var, value="B").pack(side="right", padx=10)
        frm1 = Frame(self.root)
        frm1.pack()
        frm_Label = Frame(frm1)
        frm_Entry = Frame(frm1)
        frm2 = Frame(self.root)
        frm_Label.pack(side = "left")
        frm_Entry.pack()
        frm2.pack()
        Label(frm_Label, text="用户名：").pack(pady =10)
        Entry(frm_Entry,textvariable=self.user_Varname).pack(pady =10)
        Label(frm_Label, text="密  码：").pack(pady =5)
        Entry(frm_Entry, textvariable=self.user_varpassword,show='*',).pack(anchor ="s",pady =5)
        self.tip = Label(frm2, text = "",fg='red')
        self.tip.pack(side=TOP)
        Button(frm2, text="登陆", command=self.in_system, ).pack(side="left", padx=60)  # relief = FLAT注意可以是备用样式
        Button(frm2, text="退出", command=self.root.quit, ).pack(side="right", padx=10)
        Button(self.root, text="点击游客模式进入图书馆", relief=FLAT, fg="blue").pack(side=RIGHT)
        self.root.mainloop()

    def in_system(self):
        user_name = self.user_Varname.get()
        user_password = self.user_varpassword.get()
        User = sql_user()
        result = User.QueryUser(user_name,self.var.get())
        User.close()
        print(result)
        self.Type = self.var.get()
        if len(result) != 0:
            if  self.Type is "A":
                self.name = user_name
            else:
                self.admin_name = result[0][4]
            if user_password == result[0][3]:
                self.flag = False
                self.root.destroy()
            else:
                self.tip.config(text='密码错误' )
        else:
            self.tip.config(text='该用户名不存在')
class main_():
    def __init__(self, master,user_,identity):
        self.root = master
        self.name = StringVar()
        self.type_cx = StringVar()
        self.type_jy = StringVar()
        self.user = user_
        self.identity = identity
        self.root.geometry("1000x600")
        self.root.update()  ###?
        # 几个功能的框架
        self.fm1 = Frame(self.root)
        self.fm2 = Frame(self.root)
        self.fm3 = Frame(self.root)
        self.fm4 = Frame(self.root)

        #基础按钮
        Label(self.root, text="重庆第二师范学院图书馆", bg="SteelBlue").pack(side=TOP, fill=X)
        frm_1 = Frame(self.root, bd=5)  ##bd?
        frm_1.pack(side="left", fill=Y)
        self.button_cx = Button(frm_1, text="查询图书", relief=GROOVE, command=self.create_windows1, bg="#4682B4")
        self.button_gr = Button(frm_1, text="个人中心", relief=GROOVE, command=self.create_windows2)
        self.button_xg = Button(frm_1, text="修改密码", relief=GROOVE, command=self.create_windows3)
        self.button_jy = Button(frm_1, text="借阅记录", relief=GROOVE, command=self.create_windows4)

        # 查询图书界面
        self.lable_frm1 = LabelFrame(self.fm1, text="条件检索", bd=2, pady=10, padx=5)
        self.lable_frm1.pack(fill="both")
        Label(self.lable_frm1, text="输入书名：", bg="SteelBlue").pack(side=LEFT)
        self.Find_name = Entry(self.lable_frm1, textvariable=self.name, highlightcolor='#87CEFA', highlightthickness=2, width=20)
        self.Find_name.pack(side=LEFT, padx=10, expand=YES, fill=X)
        type = ttk.Combobox(self.lable_frm1, textvariable=self.type_cx, width=8, state='readonly')
        type["values"] = ('书  名', '作  者', '出版社')
        type.current(0)
        type.pack(side=LEFT)
        Button(self.lable_frm1, text=" 搜 索 ", relief=RAISED, command = self.search_1).pack(side=LEFT, padx=20)
        lable_frm2 = LabelFrame(self.fm1, bd=2, pady=10, padx=5)  # destroy()  删除组件
        lable_frm2.config(text="结果显示")
        lable_frm2.pack(expand=YES, fill=BOTH)
        lable_frm2.pack_propagate(0)
        self.tree = ttk.Treeview(lable_frm2, show='headings')
        # 设置滚动条
        mycoll_1 = Scrollbar(lable_frm2, orient=VERTICAL)
        mycoll_1.pack(side=RIGHT, fill=Y)
        mycoll_2 = Scrollbar(lable_frm2, orient=HORIZONTAL)
        mycoll_2.pack(side=BOTTOM, fill=X)
        mycoll_1.config(command = self.tree.yview)
        mycoll_2.config(command=self.tree.xview)
        self.tree.config(xscrollcommand=mycoll_2.set, yscrollcommand=mycoll_1.set)
        self.tree.pack(fill=BOTH, expand=YES)


        # 个人中心
        frm = LabelFrame(self.fm2, text="个人中心")
        frm.pack(fill=BOTH, expand=YES)
        frm_1 = Frame(frm)
        frm_1.pack(expand=YES)
        frm_2 = Frame(frm)
        frm_2.pack(expand=YES)
        frm_3 = Frame(frm)
        frm_3.pack(expand=YES)
        Label(frm_1, text="姓       名：").pack(side=LEFT, pady=40, padx=20, expand=YES)
        Label(frm_2, text="账   户  名：").pack(side=LEFT, pady=40, padx=20, expand=YES)
        Label(frm_3, text="账 户 余 额：").pack(side=LEFT, pady=40, padx=20, expand=YES)
        self.myself_1 = Label(frm_1)
        self.myself_2 = Label(frm_2)
        self.myself_3 = Label(frm_3)
        self.myself_1.pack(side=LEFT, pady=20)
        self.myself_2.pack(side=LEFT, pady=20)
        self.myself_3.pack(side=LEFT, pady=20)
        Button(frm, text=" 充  值 ", relief=RAISED).pack(expand=YES)

        # 修改密码
        lable_frm1 = LabelFrame(self.fm3, text="账户信息", bd=2, pady=10, padx=5)
        lable_frm1.pack(fill=BOTH, expand=YES)
        frm1 = Frame(lable_frm1)
        frm1.pack(expand=YES, fill=Y)
        lable = Frame(frm1)
        lable.pack(side=LEFT, expand=YES,fill=BOTH)
        Label(lable, text="请输入原密码：").pack(pady=30)
        Label(lable, text="请输入新密码：").pack(pady=30)
        Label(lable, text="请确认新密码：").pack(pady=30)
        entry = Frame(frm1)
        entry.pack(side=LEFT, expand=YES,fill=BOTH)
        self.old = StringVar()
        self.new = StringVar()
        self.newtwo = StringVar()
        Entry(entry, textvariable=self.old,highlightcolor='#87CEFA', highlightthickness=2,show='*').pack(pady=30)
        Entry(entry, textvariable=self.new,highlightcolor='#87CEFA', highlightthickness=2,show='*').pack(pady=30)
        Entry(entry, textvariable=self.newtwo,highlightcolor='#87CEFA', highlightthickness=2,show='*').pack(pady=30)
        frm2 = Frame(lable_frm1)
        frm2.pack(expand=YES)
        Button(frm2, text="确 定", relief=RAISED, command=self.Resetting).pack(side=LEFT, padx=50, pady=20)
        Button(frm2, text="重 置", relief=RAISED).pack(side=RIGHT, padx=50, pady=20)

        # 借阅记录
        lable_frm1 = LabelFrame(self.fm4, text="借阅查询", bd=2, pady=10, padx=5)
        lable_frm1.pack(side=TOP, fill=X)
        Label(lable_frm1, text="时间：").pack(side=LEFT)
        Entry(lable_frm1).pack(side=LEFT, padx=10, expand=YES, fill=X)
        type = ttk.Combobox(lable_frm1, textvariable=self.type_jy, width=8, state='readonly')
        type["values"] = ('借书记录', '还书记录')
        type.current(0)
        type.pack(side=LEFT)
        Button(lable_frm1, text=" 确 定", relief=RAISED).pack(side=LEFT, padx=20)
        lable_frm2 = LabelFrame(self.fm4, text="结果呈现", bd=2, pady=10, padx=5)
        lable_frm2.pack(side=TOP, fill=BOTH, expand=YES)
        Text(lable_frm2).pack(expand=YES, fill=BOTH)
    def num(self):
        print(1)
    def search_1(self):
        a = sql_book()
        word = self.name.get()
        type = self.type_cx.get()
        print(type)
        results = a.Query(word,type)
        a.close()
        print(results)
        for row in results:
            BOOKNAME = row[0]
            AUTHOR = row[1]
            PUBLISH = row[2]
            ISBN = row[3]
            INVENTORY = row[4]
            CANBORROW = row[5]
            TYPE = row[6]
            print(
                 f"ISBN={ISBN},BOOKNAME={BOOKNAME},AUTHOR={AUTHOR},PUBLISH={PUBLISH},INVENTORY={INVENTORY},CANBORROW ={CANBORROW},TYPE={TYPE}")
        self.judge_list(results)

    def judge_list(self,search_list):
        if len(search_list) == 0:
            tkinter.messagebox.showinfo('提示', '暂无符合条件的图书')
            return
        else:
            return self.find(search_list)
    #   find_list参数为通过 self.search()函数查找之后得到的符合条件的数据列表,
    #   形式如：[('数据挖掘与机器学习', '徐桂秋', '人民邮电出版社', '978-7-115-50345-2', '100', 'YES', 1)
    def find(self, search_list):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        # 定义列
        self.tree["columns"] = ("书名", "作者", "出版社","ISBN","库存","可借","状态")  # 列名
        # 设置列，列还不显示
        self.tree.column("书名", minwidth=300, stretch=False, anchor='center')
        self.tree.column("作者", minwidth=150, anchor='center')
        self.tree.column("出版社", minwidth=300, anchor='center')
        self.tree.column("ISBN", minwidth=300, anchor='center')
        self.tree.column("库存", minwidth=150, anchor='center')
        self.tree.column("可借", minwidth=150, anchor='center')
        self.tree.column("状态", minwidth=100, stretch=False, anchor='center')
        # 设置表头
        self.tree.heading("书名", text="书名")  # 表头显示text
        self.tree.heading("作者", text="作者")
        self.tree.heading("出版社", text="出版社")
        self.tree.heading("ISBN", text="ISBN")
        self.tree.heading("库存", text="库存")
        self.tree.heading("可借", text="可借")
        self.tree.heading("状态", text="状态")
        for book in search_list:
            self.tree.insert('','end',value = (book[0],book[1],book[2],book[3],book[4],book[5],book[6]))
        for col in ("书名","作者", "出版社", "ISBN","库存","可借","状态"):  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

    def treeview_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def Resetting(self):
        name1 = self.old.get().strip()
        name2 = self.new.get().strip()
        name3 = self.newtwo.get().strip()
        a = sql_user()
        if name1=="" or name2=="" or name3=="":
            return tkinter.messagebox.showinfo('提示', '请填写完成！')
        result = a.QueryUser(self.user,self.identity)
        checkpassword = result[0][3]
        try:
            if name1 == checkpassword:
                if name2 == name3:
                    a.Update(self.user,1,name2)
                    tkinter.messagebox.showinfo('提示', f'修改成功"\n新密码为:{name2}')
                else:
                    tkinter.messagebox.showinfo('提示', '两次新密码输入不一致')
            else:
                tkinter.messagebox.showinfo('提示', '旧密码与用户名对应的密码不同')
        finally:
            a.close()
    def create_windows1(self):
        self.forget_fm()
        self.fm1.pack(side="left", expand=YES, fill=BOTH)

    def create_windows2(self):
        self.forget_fm()
        self.fm2.pack(side="left", expand=YES, fill=BOTH)
        User = sql_user()
        result = User.QueryUser(self.user,self.identity)
        for i in result:
            self.myself_1.config(text=i[4])
            self.myself_2.config(text=i[2])
            self.myself_3.config(text=i[5])

    def create_windows3(self):
        self.forget_fm()
        self.fm3.pack(side="left", expand=YES, fill=BOTH)

    def create_windows4(self):
        self.forget_fm()
        self.fm4.pack(side="left", expand=YES, fill=BOTH)

    def enter_change_cx_color(self, event):
        if self.button_cx["bg"] != "#4682B4":
            self.button_cx["bg"] = "#92C8F6"

    def enter_change_gr_color(self, event):
        if self.button_gr["bg"] != "#4682B4":
            self.button_gr["bg"] = "#92C8F6"

    def enter_change_xg_color(self, event):
        if self.button_xg["bg"] != "#4682B4":
            self.button_xg["bg"] = "#92C8F6"

    def enter_change_jy_color(self, event):
        if self.button_jy["bg"] != "#4682B4":
            self.button_jy["bg"] = "#92C8F6"

    def leave_change_cx_color(self, event):
        if self.button_cx["bg"] != "#4682B4":
            self.button_cx["bg"] = "#F0F0F0"

    def leave_change_gr_color(self, event):
        if self.button_gr["bg"] != "#4682B4":
            self.button_gr["bg"] = "#F0F0F0"

    def leave_change_xg_color(self, event):
        if self.button_xg["bg"] != "#4682B4":
            self.button_xg["bg"] = "#F0F0F0"

    def leave_change_jy_color(self, event):
        if self.button_jy["bg"] != "#4682B4":
            self.button_jy["bg"] = "#F0F0F0"

    def click_change_cx_color(self, event):
        self.button_jy["bg"] = "#F0F0F0"
        self.button_gr["bg"] = "#F0F0F0"
        self.button_xg["bg"] = "#F0F0F0"
        self.button_cx["bg"] = "#4682B4"

    def click_change_gr_color(self, event):
        self.button_gr["bg"] = "#4682B4"
        self.button_jy["bg"] = "#F0F0F0"
        self.button_cx["bg"] = "#F0F0F0"
        self.button_xg["bg"] = "#F0F0F0"

    def click_change_xg_color(self, event):
        self.button_xg["bg"] = "#4682B4"
        self.button_jy["bg"] = "#F0F0F0"
        self.button_cx["bg"] = "#F0F0F0"
        self.button_gr["bg"] = "#F0F0F0"

    def click_change_jy_color(self, event):
        self.button_jy["bg"] = "#4682B4"
        self.button_cx["bg"] = "#F0F0F0"
        self.button_gr["bg"] = "#F0F0F0"
        self.button_xg["bg"] = "#F0F0F0"

    def put_basic_module(self):
        self.button_cx.pack(side=TOP, expand=YES, fill=Y, pady=5)
        self.button_cx.bind("<Enter>", self.enter_change_cx_color)
        self.button_cx.bind("<Leave>", self.leave_change_cx_color)
        self.button_cx.bind("<Button-1>", self.click_change_cx_color)
        self.button_gr.pack(side=TOP, expand=YES, fill=Y, pady=5)
        self.button_gr.bind("<Enter>", self.enter_change_gr_color)
        self.button_gr.bind("<Leave>", self.leave_change_gr_color)
        self.button_gr.bind("<Button-1>", self.click_change_gr_color)
        self.button_xg.pack(side=TOP, expand=YES, fill=Y, pady=5)
        self.button_xg.bind("<Enter>", self.enter_change_xg_color)
        self.button_xg.bind("<Leave>", self.leave_change_xg_color)
        self.button_xg.bind("<Button-1>", self.click_change_xg_color)
        self.button_jy.pack(side=TOP, expand=YES, fill=Y, pady=5)
        self.button_jy.bind("<Enter>", self.enter_change_jy_color)
        self.button_jy.bind("<Leave>", self.leave_change_jy_color)
        self.button_jy.bind("<Button-1>", self.click_change_jy_color)

        self.create_windows1()

    def forget_fm(self):
        self.fm1.pack_forget()
        self.fm2.pack_forget()
        self.fm3.pack_forget()
        self.fm4.pack_forget()

    def system_Button1(self):
        pass


if __name__ == '__main__':
    login = system()
    if login.flag == False and login.var.get() == "A":
        root = Tk()
        start = main_(root,login.name,login.Type)
        start.put_basic_module()   # 放置基本组件
        root.mainloop()
    elif login.flag == False and login.var.get() == "B":
        root = Tk()
        start = admin_system(root,login.admin_name)
        root.mainloop()