from tkinter import *
from tkinter import ttk



class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label1 = Label(self, text="scs", bg="#333", fg="#fff", font=("arial", 30)).grid(row=0, column=0, columnspan=2,pady=40)
       admlabel = Label(self, text="ADM NO:", bg="#333", fg="#fff", font=("arial", 16)).grid(row=1, column=0)
       admEntry = Entry(self, font=("arial", 16)).grid(row=1, column=1, pady=10)
       passwordlabel = Label(self, text="password:", bg="#333", fg="#fff", font=("arial", 16)).grid(row=2, column=0)
       passwordEntry = Entry(self, show=".", font=("arial", 16)).grid(row=2, column=1, pady=10)
       loginButton = Button(self, text="login", font=("arial", 16) ).grid(row=3, column=0, columnspan=2,pady=20)





class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Label(self,text="just winging it").pack()


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
       # p3 = Page3(self)

        buttonframe = Frame(self,bg="grey")
        container = Frame(self,bg="grey")
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        #p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="login",command=p1.show)
        b2 = Button(buttonframe, text="Page 2", command=p2.show)
       # b3 = Button(buttonframe, text="Page 3", command=p3.show)

        b1.grid()
        b2.grid(row=3, column=0, columnspan=2,pady=20)
       # b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("900x500")
    root.title("login form")
    #root.configure(background="#333")
    root.mainloop()


