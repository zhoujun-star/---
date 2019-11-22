from tkinter import *
from sqlite_user import sql_user
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
        self.var = StringVar()
        self.var.set("A")
        self.root.update()
        self.login()

    # 登陆界面函数
    def login(self):
        Label(self.root, text="欢迎使用图书管理系统", height=6, font=10).pack(side="top")
        frm_user = Frame(self.root)
        frm_user.pack()
        r_user = Radiobutton(frm_user, text="读  者", variable= self.var, value='A',).pack(side="left", padx=30)
        r_mager = Radiobutton(frm_user, text="管理员", variable= self.var, value='B').pack(side="right", padx=10)
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
        Label(frm_Label, text="密  码：").pack(pady =10)
        Entry(frm_Entry, textvariable=self.user_varpassword,show='*',).pack(pady =10)
        Button(frm2,text = "登陆", command = self.in_system, ).pack(side="left", padx = 60, pady =2)         #relief = FLAT注意可以是备用样式
        Button(frm2,text = "退出", command = self.root.quit, ).pack(side="right",padx = 10, pady =2)
        Button(self.root, text = "点击游客模式进入图书馆", relief=FLAT,fg = "blue",underline=8).pack(side=RIGHT)
        self.root.mainloop()
    def in_system(self):
        user_name = self.user_Varname.get()
        user_password = self.user_varpassword.get()
        User = sql_user()
        result = User.QueryUser(user_name)
        User.close()
        print(result)
        print(user_name,"---",user_password)
        if len(result) != 0:
            if user_password == result[0][1]:
                self.root.withdraw()
                return True
            else:
                print("密码错误！")
        else:
            print("该用户名不存在！")

if __name__ == '__main__':
    User = sql_user()
    User.CreateTable()
    User.close()
    start = system()