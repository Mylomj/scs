import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from customtkinter import *
from PIL import Image,ImageTk
import socket
import threading





class FisrtPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,bg="#333")
        box = Frame(self,bg="#333")

        label1 = Label(box, text="scs", bg="#333", fg="#fff", font=("arial", 30)).grid(row=0, column=0, columnspan=2,pady=40)

        admlabel = Label(box, text="ADM NO:", bg="#333", fg="#fff", font=("arial", 16)).grid(row=1, column=0)
        admEntry = Entry(box, font=("arial", 16))
        admEntry.grid(row=1, column=1, pady=10)

        passwordlabel = Label(box, text="password:", bg="#333", fg="#fff", font=("arial", 16)).grid(row=2, column=0)
        passwordEntry = Entry(box, show=".", font=("arial", 16))
        passwordEntry.grid(row=2, column=1, pady=10)

        def verify():
            if admEntry.get() == "milo" and passwordEntry.get() == "milo":
                controller.show_frame(SecondPage)
            else:
                messagebox.showinfo("error","wrong admno or password")
        loginButton = CTkButton(box, text="login", font=("arial", 16),command= verify).grid(row=3, column=0, columnspan=2,pady=20)

        admin_button = CTkButton(self,text="admin",font=("arial",16),height=10,width=10,command=lambda :controller.show_frame(AdminPage)).place(x=700,y=10)

        box.pack()


class AdminPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,bg="#fff")
        box = Frame(self,bg="#333")





        box.pack()


class SecondPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,bg="#fff")
        box = Frame(self,bg="#333")
        infotab = Frame(self,bg="#fff")
        notification_frame= Frame(self,bg="#333",height=50,width=50)

        l1 = CTkLabel(self, text="Name:", font=("arial", 16))
        l2 = CTkLabel(self, text="ADM NO:", font=("arial", 16))
        l3 = CTkLabel(self, text="Course:", font=("arial", 16))
        l1.place(x=10,y=140)
        l2.place(x=10,y=170)
        l3.place(x=10,y=200)

        global img
        img = PhotoImage(file="pictures/user.png")
        img_label = CTkLabel(self, image=img,text="")
        img_label.place(x=10,y=10)



        imgg = ImageTk.PhotoImage(Image.open("pictures/email-message-icon-4.png").resize((50,50)))
        b1 = CTkButton(master=self,image  =imgg,text="",height=5, width=5,fg_color="#fff",hover_color="#fff",command=lambda:controller.show_frame(ThirdPage)).place(x=640,y=3)

        imgg = ImageTk.PhotoImage(Image.open("pictures/menu.png").resize((30, 30)))
        b1 = CTkButton(master=self, image=imgg, text="", height=30, width=30,fg_color="#fff",hover_color="#fff",command=lambda: controller.show_frame(ThirdPage)).place(x=700, y=10)

        imgg = ImageTk.PhotoImage(Image.open("pictures/more-vertical-alt.png").resize((30, 30)))
        b1 = CTkButton(master=self, image=imgg, text="", height=30, width=30,fg_color="#fff",hover_color="#fff",command=lambda: controller.show_frame(ThirdPage)).place(x=740, y=10)

        #b1=Button(self,image=(img),height=30,width=30)
        #b1.place(x=600,y=30)

        Listbox(notification_frame, font=("arial",16),height=13,width=40).pack()
        CTkButton(infotab, text="fee statement",font=("arial", 16)).pack()
        CTkButton(infotab, text="School schedule", font=("arial",16)).pack(pady=10)
        CTkButton(infotab, text="Exams", font=("arial",16)).pack()


        box.pack()
        notification_frame.place(x=300,y=150)
        infotab.place(x=10,y=250)



class ThirdPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,bg="#333")

       

        #xi= 0
        #yi= 0

        #def show_message():

            #u = user_entry.get()
            #user = Label(chat_bg,height=1,width=55,bg="#a6a6a6",text= u,font=12,anchor="e")
            #user.place(x=xi,y=yi)

            #if 'hello' in u:
                #other_user = Label(chat_bg, height=1, width=55, bg="#a6a6a6", text="almost there", font=12, anchor="w")
                #other_user.place(x=xi, y=yi+25)



        entry_bg = Frame(self,height=50,width=500,bg="white")
        entry_bg.place(x=299,y=448)

        other_info_bg = Frame(self, height=50, width=299, bg="green")
        other_info_bg.place(x=0, y=0)

        global chat_bg_img
        chat_bg_img = ImageTk.PhotoImage(Image.open("pictures/original whatsapp.png").resize((500,390)))
        chat_bg = Listbox(self,height=20,width=500)
        chat_bg.place(x=299,y=51)
        chat_label = Label(chat_bg,image=chat_bg_img)
        chat_label.pack()





        info_bg = Frame(self, height=50, width=500, bg="white")
        info_bg.place(x=299, y=0)

        user_entry = Entry(entry_bg,width=28,font=("helvetica",20))
        user_entry.place(x=0,y=10)




        #l4= Label(self,text="jkaf").pack(side='left'),Label(self,text="mibd").pack(side="left")
       # img = ImageTk.PhotoImage(Image.open("C:/Users/mylo/Desktop/rcs project/pictures/1000011412.jpg"))
       # b1=Button(self,image=(img)).pack()
        ljd= Button(self,text="send").place(x=750,y=470)


        imgg = ImageTk.PhotoImage(Image.open("pictures/arrow-left.png").resize((30, 30)))
        back_button = CTkButton(self,image=imgg, text="",width=10,fg_color="#fff",command=lambda:controller.show_frame(SecondPage)).grid()







class Application(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        #creating window
        window = Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0,minsize=800)

        self.frames ={}
        for F in(FisrtPage,SecondPage,ThirdPage,AdminPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(FisrtPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()

