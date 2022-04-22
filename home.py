from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pandas as pd
import matplotlib .pyplot as plt


root=Tk()
root.title("Home")
root.minsize(900,800)
root.maxsize(900,800)
root.config(bg="#3A3845")

img1 = Image.open("./images/1.jpg")
img2 = Image.open("./images/2.jpg")
img3= Image.open("./images/3.jpg")
img4 = Image.open("./images/4.jpg")

resize_image1 = img1.resize((200, 200))
resize_image2= img2.resize((200, 200))
resize_image3 = img3.resize((200, 200))
resize_image4 = img4.resize((200, 200))

my_img1=ImageTk.PhotoImage(resize_image1)
my_img2=ImageTk.PhotoImage(resize_image2)
my_img3=ImageTk.PhotoImage(resize_image3)
my_img4=ImageTk.PhotoImage(resize_image4)
labelHeading=Label(text="Cyber crime management system",font=("roboto",23),fg="#f2f2f2",bg="#3A3845").place(x=200,y=20)
labelYearwise=Label(text="Year wise data",font=("roboto",22),fg="#f2f2f2",bg="#3A3845").place(x=330,y=100)




def newWindow(year):
    newTITLE="Showing data for the year " + str(year)
    root.withdraw()
    print(newTITLE)
    global lblYear;
    def onClose():
        yearWindow.destroy()
        root.deiconify()
    yearWindow = Toplevel(root)
    yearWindow.minsize(900,500)
    yearWindow.maxsize(900,500)
    yearWindow.config(bg="#3A3845")
    lblYear=Label(yearWindow,text=newTITLE,font=("roboto",25),fg="#f2f2f2",bg="#3A3845").place(x=200,y=50)
    my_tree=ttk.Treeview(yearWindow)
    my_tree['columns']=("Revenge","Extortion","piracy","Inciting hate")

    my_tree.column("Revenge",width=120,minwidth=25,stretch=NO)
    my_tree.column("Extortion",anchor=W,width=120)
    my_tree.column("piracy",anchor=CENTER,width=120)
    my_tree.column("Inciting hate",anchor=W,width=123)

    my_tree.heading("Revenge",text="Revenge",anchor=W)
    my_tree.heading("Extortion", text="Extortion", anchor=W)
    my_tree.heading("piracy", text="Piracy", anchor=CENTER)
    my_tree.heading("Inciting hate", text="Inciting hate", anchor=W)

    for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]:
        my_tree.insert(parent='',index='end',iid=i,text=i,values=(20,30,430,56))
        my_tree.place(x=100,y=150)
        x = [10, 30, 40, 56, 76, 43, 44, 67]
        y = [4, 5, 4, 3, 4, 5, 6, 7]
    def generateGraph():
        plt.xlabel('Model', fontsize=18)
        plt.ylabel('summne', fontsize=19)
        plt.bar(x,y)
        plt.show()

    btngraph=Button(yearWindow,text="Click here to generate graph",bg="#ff0000",command=lambda:generateGraph())
    btngraph.place(x=350,y=400)



    yearWindow.protocol("WM_DELETE_WINDOW", onClose)


def statewise():
    state=Toplevel()
    root.withdraw()
    state.deiconify()
    def onClose():
        state.destroy()
        root.deiconify()
    state.protocol("WM_DELETE_WINDOW",onClose)

button2017=Button(image=my_img1,bg="#000",command=lambda : newWindow(2017)).place(x=200,y=180)
lbl2017=Label(text="2017",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=250,y=400)
button2018=Button(image=my_img2,bg="#000",command=lambda : newWindow(2018)).place(x=500,y=180)
lbl2018=Label(text="2018",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=550,y=400)
button2019=Button(image=my_img3,bg="#000",command=lambda : newWindow(2019)).place(x=200,y=470)
lbl2018=Label(text="2019",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=250,y=700)
button2020=Button(image=my_img4,bg="#000",command=lambda : newWindow(2020)).place(x=500,y=470)
lbl2019=Label(text="2020",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=550,y=700)
buttonStatewise=Button(text="State wise data",bg="#FF6363",command=statewise).place(x=750,y=750)
root.mainloop()