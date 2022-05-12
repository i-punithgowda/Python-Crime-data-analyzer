from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pandas as pd
import matplotlib .pyplot as plt




bgCol="#3A3845"
root=Tk()
root.title("Home")
root.minsize(900,800)
root.maxsize(900,800)
root.config(bg=bgCol)
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
labelHeading=Label(text="Cyber crime data analyzer",font=("roboto",23,"bold"),fg="#f2f2f2",bg="#3A3845").place(x=220,y=20)
labelYearwise=Label(text="Year wise data",font=("roboto",22,"bold"),fg="#f2f2f2",bg="#3A3845").place(x=330,y=100)

auth={"status":0}

    


def newWindow(year):
    if(auth["status"]==0):
        messagebox.showerror("Login error","You are not logged in!!")
    elif(auth["status"]==1):
        newTITLE="Showing data for the year " + str(year)
        root.withdraw()
        global lblYear;
        def onClose():
            yearWindow.destroy()
            root.deiconify()
        yearWindow = Toplevel(root)
        yearWindow.minsize(900,500)
        yearWindow.maxsize(900,500)
        yearWindow.config(bg=bgCol)
        lblYear=Label(yearWindow,text=newTITLE,font=("roboto",25),fg="#f2f2f2",bg="#3A3845").place(x=200,y=50)
        my_tree=ttk.Treeview(yearWindow)
        my_tree['columns']=("Revenge","Extortion","Sexual Exploitation","Causing Disrepute")

        my_tree.column("Revenge",width=100,minwidth=25,)
        my_tree.column("Extortion",anchor=W,width=120)
        my_tree.column("Sexual Exploitation",anchor=CENTER,width=180)
        my_tree.column("Causing Disrepute",anchor=W,width=123)

        my_tree.heading("Revenge",text="Revenge",anchor=W)
        my_tree.heading("Extortion", text="Extortion", anchor=W)
        my_tree.heading("Sexual Exploitation", text="Sexual Exploitation", anchor=CENTER)
        my_tree.heading("Causing Disrepute", text="Causing Disrepute", anchor=W)
        df=pd.read_csv(str(year)+".csv")
        listRevenge=[]
        listExtortion=[]
        listSexuallExploitation=[]
        listDisrepute=[]
        for i in df["Revenge"]:
            listRevenge.append(i)
        for i in df["Extortion"]:
            listExtortion.append(i)
        for i in df["Sexual Exploitation"]:
            listSexuallExploitation.append(i)
        for i in df["Causing Disrepute"]:
            listDisrepute.append(i)
        ttlRevenge=sum(listRevenge[0:10])
        ttlExtortion=sum(listExtortion[0:10])
        ttlSexualExploitation=sum(listSexuallExploitation[0:10])
        ttlDisrepute=sum(listDisrepute[0:10])
        for i in range(1,11):
            my_tree.insert(parent='',index='end',iid=i,text=i,values=(listRevenge[i],listExtortion[i],listSexuallExploitation[i],listDisrepute[i]))
            my_tree.place(x=100, y=150)

        lblTotal = Label(yearWindow, text="Total", font=("Roboto", 15, "bold"),bg="#3A3845",fg="#f2f2f2").place(x=100, y=400)
        lblttlRevenge=Label(yearWindow,text=str(ttlRevenge),font=("Roboto",15,"bold"),bg="#3A3845",fg="#f2f2f2").place(x=300,y=400)
        lblttlExtortion = Label(yearWindow, text=str(ttlExtortion), font=("Roboto", 15, "bold"),bg="#3A3845",fg="#f2f2f2").place(x=400, y=400)
        lblttlSexualExploitation = Label(yearWindow, text=str(ttlSexualExploitation), font=("Roboto", 15, "bold"),bg="#3A3845",fg="#f2f2f2").place(x=600, y=400)
        lblttlDisrepute = Label(yearWindow, text=str(ttlDisrepute), font=("Roboto", 15, "bold"),bg="#3A3845",fg="#f2f2f2").place(x=700, y=400)
        x = [ttlRevenge,ttlExtortion,ttlSexualExploitation,ttlDisrepute]
        y = ["Revenge","Extortion","Sexual Exploitation","Causing disreputes"]

        def percentGenerator(val):
            return str(round(val,1))+"%"

        def generateGraph():    
            plt.pie(x,labels=y,autopct=percentGenerator,shadow=True)
            plt.show()



        btngraph=Button(yearWindow,text="Click here to generate graph",bg="#FFA1A1",command=lambda:generateGraph())
        btngraph.place(x=350,y=450)



        yearWindow.protocol("WM_DELETE_WINDOW", onClose)


def statewise():
    if(auth["status"]==0):
        messagebox.showerror("Login error","You are not logged in!!!")
    elif(auth["status"]==1):
        state=Toplevel()
        root.withdraw()
        state.deiconify()
        state.config(bg=bgCol)
        state.minsize(900,500)
        state.maxsize(900,500)
        lblheading=Label(state,text="State wise data",font=("Roboto",24,"bold"),bg=bgCol,fg="#f2f2f2").place(x=300,y=20)
        stateList=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
        cmb=ttk.Combobox(state,value=stateList,width=40)
        cmb.place(x=300,y=90)
        cmb.current(0)

        def displayStatesData(self):

            statesTree=ttk.Treeview(state,height=5)
            statesTree['columns'] = ("Year","Revenge", "Extortion", "Sexual Exploitation", "Causing Disrepute")
            statesTree.column("Year",width=100)
            statesTree.column("Revenge", width=100, )
            statesTree.column("Extortion", anchor=W, width=120)
            statesTree.column("Sexual Exploitation", anchor=W, width=60)
            statesTree.column("Causing Disrepute", anchor=W, width=63)

            statesTree.heading("Year", text="Year", anchor=W)
            statesTree.heading("Revenge", text="Revenge", anchor=W)
            statesTree.heading("Extortion", text="Extortion", anchor=W)
            statesTree.heading("Sexual Exploitation", text="Sexual Exploitation", anchor=W)
            statesTree.heading("Causing Disrepute", text="Causing Disrepute", anchor=W)
            revenge=0
            extortion=0
            sexualExploitation=0
            causingDisrepute=0
            df = pd.read_csv("2017.csv")
            stateData = df.iloc[stateList.index(cmb.get())]

            statesTree.insert(parent='', index='end', iid=1, text=1, values=(2017, stateData["Revenge"], stateData["Extortion"], stateData["Sexual Exploitation"], stateData["Causing Disrepute"]))
            revenge += stateData["Revenge"]
            extortion += stateData["Extortion"]
            sexualExploitation += stateData["Sexual Exploitation"]
            causingDisrepute += stateData["Causing Disrepute"]

            df = pd.read_csv("2018.csv")
            stateData = df.iloc[stateList.index(cmb.get())]
            statesTree.insert(parent='', index='end', iid=2, text=2, values=(2018, stateData["Revenge"], stateData["Extortion"], stateData["Sexual Exploitation"], stateData["Causing Disrepute"]))
            revenge += stateData["Revenge"]
            extortion += stateData["Extortion"]
            sexualExploitation+=stateData["Sexual Exploitation"]
            causingDisrepute+=stateData["Causing Disrepute"]

            df = pd.read_csv("2019.csv")
            stateData = df.iloc[stateList.index(cmb.get())]
            statesTree.insert(parent='', index='end', iid=3, text=3, values=(2019, stateData["Revenge"], stateData["Extortion"], stateData["Sexual Exploitation"], stateData["Causing Disrepute"]))
            revenge += stateData["Revenge"]
            extortion += stateData["Extortion"]
            sexualExploitation += stateData["Sexual Exploitation"]
            causingDisrepute += stateData["Causing Disrepute"]

            df=pd.read_csv("2020.csv")
            stateData=df.iloc[stateList.index(cmb.get())]
            statesTree.insert(parent='',index='end',iid=4,text=4,values=(2020,stateData["Revenge"],stateData["Extortion"],stateData["Sexual Exploitation"],stateData["Causing Disrepute"]))
            revenge += stateData["Revenge"]
            extortion += stateData["Extortion"]
            sexualExploitation += stateData["Sexual Exploitation"]
            causingDisrepute += stateData["Causing Disrepute"]

            statesTree.insert(parent='',index='end',iid=5,text=5,values=("Total",revenge,extortion,sexualExploitation,causingDisrepute))
            statesTree.place(x=100, y=150)

            b = [revenge,extortion,sexualExploitation,causingDisrepute]
            a = ["Revenge", "Extortion", "Sexual Exploitation", "Causing disreputes"]

            def generateGraph():
                plt.bar(a,b,color="red")
                plt.show()

            btngraph = Button(state, text="Click here to generate graph", bg="#FFA1A1",command=lambda: generateGraph())
            btngraph.place(x=300,y=350)

        displayStatesData(" ")

        cmb.bind("<<ComboboxSelected>>", displayStatesData)
        def onClose():
            root.deiconify()
            state.destroy()

        state.protocol("WM_DELETE_WINDOW",onClose)

button2017=Button(image=my_img1,bg="#000",command=lambda : newWindow(2017)).place(x=200,y=180)
lbl2017=Label(text="2017",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=250,y=400)
button2018=Button(image=my_img2,bg="#000",command=lambda : newWindow(2018)).place(x=500,y=180)
lbl2018=Label(text="2018",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=550,y=400)
button2019=Button(image=my_img3,bg="#000",command=lambda : newWindow(2019)).place(x=200,y=470)
lbl2018=Label(text="2019",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=250,y=700)
button2020=Button(image=my_img4,bg="#000",command=lambda : newWindow(2020)).place(x=500,y=470)
lbl2019=Label(text="2020",fg="#f2f2f2",bg="#3A3845",font=("roboto",22)).place(x=550,y=700)
buttonStatewise=Button(text="State wise data",bg="#FFA1A1",command=statewise).place(x=750,y=750)


def login():
    loginWindow=Toplevel()
    root.withdraw()
    loginWindow.config(bg=bgCol)
    loginWindow.minsize(900,600)
    loginWindow.maxsize(900,600)
    lblHeading=Label(loginWindow,text="Welcome to Cyber crime data analyser",bg=bgCol,fg="#f2f2f2",font=("Roboto",22,"bold")).place(x=150,y=20)
    lblLoginHeading=Label(loginWindow,text="Login to your account",bg=bgCol,fg="#f2f2f2",font=("Roboto",18,"bold")).place(x=320,y=90)
    imgLogin = Image.open("./images/Login.png")
    fitImg= imgLogin.resize((200, 200))
    imgFinal=ImageTk.PhotoImage(fitImg)
    btnLoginImg=Button(loginWindow,image=imgFinal)  
    btnLoginImg.place(x=350,y=150)
   

    lblUserName=Label(loginWindow,text="Username : ",bg=bgCol,fg="#f2f2f2",font=("Roboto",15,"bold")).place(x=150,y=400)
    lblPassword=Label(loginWindow,text="Password : ",bg=bgCol,fg="#f2f2f2",font=("Roboto",15,"bold")).place(x=150,y=430)
    txtUsername=Entry(loginWindow,width=40)
    txtUsername.place(x=300,y=400)
    txtPassword=Entry(loginWindow,width=40,show="*")
    txtPassword.place(x=300,y=430)
    def authenticate():
        data=pd.read_csv("userDetails.csv")
        data.set_index("FirstName", inplace=True)
        if(txtUsername.get()=="" or txtPassword.get()==""):
            messagebox.showerror("Empty fields","Either username or password is empty!!")
        else:
            try:
                foundData=(dict(data.loc[txtUsername.get()]))
                if(foundData["Password"]==txtPassword.get()):
                    messagebox.showinfo("Login succesful","Welcome "+txtUsername.get() +"")
                    setAuth(1)
                    loginWindow.withdraw()
                    root.deiconify()
                else:
                    messagebox.showerror("Login unsuccesful","Entered password is wrong,Try again")
            except KeyError as e:
                messagebox.showerror("Login unsuccesful","Entered username doesnt exists!!")
       

    def signup(val):
        loginWindow.withdraw()
        register=Toplevel(root)
        register.maxsize(800,400)
        register.minsize(800,400)
        register.config(bg=bgCol)
        lblregisterHeading=Label(register,text="Create a new account",bg=bgCol,fg="#f2f2f2",font=("Roboto",22,"bold")).place(x=200,y=20)
        btnSignup=Button(register,image=imgFinal).place(x=100,y=150)
        lblfn=Label(register,text="First name",bg=bgCol,fg="#f2f2f2").place(x=350,y=180)
        firstName=Entry(register,width=30)
        firstName.place(x=450,y=180)
        lblln=Label(register,text="Last name",bg=bgCol,fg="#f2f2f2").place(x=350,y=210)
        lastName=Entry(register,width=30)
        lastName.place(x=450,y=210)
        lblpass=Label(register,text="Password",bg=bgCol,fg="#f2f2f2").place(x=350,y=240)
        password= Entry(register,show="*",width="30")
        password.place(x=450,y=240)
        lblConfirm=Label(register,text="Confirm",bg=bgCol,fg="#f2f2f2").place(x=350,y=270)
        confirmPass=Entry(register,show="*",width="30")
        confirmPass.place(x=450,y=270)
        def registration():
            fn=firstName.get()
            ln=lastName.get()
            ps=password.get()
            con=confirmPass.get()
            if(fn=="" or ln=="" or ps=="" or con==""):
                messagebox.showerror("Error","One or more fields are empty")
            elif(ps!=con):
                messagebox.showerror("Error","Passwords are not matching!")
            else:
                data=pd.DataFrame({
                    "FirstName":[fn],
                    "LastName":[ln],
                    "Password":[ps]
                })
                data.to_csv("userDetails.csv",mode="a",index=True,header=False)
                messagebox.showinfo("Success","Registration succesful")
                firstName.delete(0,END)
                lastName.delete(0,END)
                password.delete(0,END)
                confirmPass.delete(0,END)
        def closeRegister():
            register.withdraw()
            loginWindow.deiconify()
                    
        register.protocol("WM_DELETE_WINDOW",closeRegister)

        btnSignup=Button(register,text="Signup",bg="Coral",fg="#f2f2f2",command=registration).place(x=450,y=300)
    

    btnAuth=Button(loginWindow,text="Login" ,bg="coral", padx=12,pady=8,command=authenticate).place(x=400,y=480)  
    lblSignup=Label(loginWindow,text="New user ? click here to signup!",bg=bgCol,fg="skyblue",font=("Roboto",13,"bold"))
    lblSignup.place(x=300,y=550)
    lblSignup.bind('<Button-1>',signup)
  


    def onClose():
        loginWindow.withdraw()
        root.deiconify()
    loginWindow.protocol("WM_DELETE_WINDOW",onClose)


btnLogin=Button(text="Login/Signup",bg='#FFA1A1',command=login)
btnLogin.place(x=500,y=750)

def prediction():
    if(auth["status"]==0):
        messagebox.showerror("Login error","Login before performing this operation!")
    else:
        root.withdraw()
        prediction_frame=Toplevel()
        prediction_frame.config(bg=bgCol)
        prediction_frame.geometry("700x600")
        Label(prediction_frame,text="Prediction of crime data ",font=("Roboto",22,"bold"),bg=bgCol,fg="#f2f2f2").place(x=150,y=30)
        
        def onClose():
            root.deiconify()
            prediction_frame.withdraw()
        prediction_frame.protocol("WM_DELETE_WINDOW",onClose)   

btnPrediction=Button(text="Prediction",bg='#FFA1A1',command=prediction)
btnPrediction.place(x=630,y=750)


def setAuth(val):
    auth["status"]=val
    btnLogin.destroy()
    

def logout():
    setAuth(0)
    

root.mainloop()