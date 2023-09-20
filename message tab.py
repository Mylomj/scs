from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.geometry("750x500")

menu_frame = Frame(root, bg="#c3c3c3")

menu_frame.pack(side=LEFT)
menu_frame.pack_propagate(False)
menu_frame.configure(width=300,height=750)

bgimg = PhotoImage(file="pictures/original whatsapp.png")
message_label = scrolledtext.ScrolledText(root).pack(side=RIGHT)
e=Entry(width=50)
e.place(x=350, y=450)
menu_label1 = Label(menu_frame,text="temp",padx=300,pady=20,bg="#767373").pack()
menu_label2 = Label(menu_frame,text="temp",padx=300,pady=10).pack()



main_frame=Frame(root,highlightbackground="black",highlightthickness=2)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=750)

#main_frame_label1 = LabelFrame(main_frame,text="temp",padx=300,pady=20,bg="#767373").grid()


mainloop()