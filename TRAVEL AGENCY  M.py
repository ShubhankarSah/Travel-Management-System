from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import time
import random
import sqlite3
global  x1,x2,x3,x4
import tkinter.ttk as ttk
import datetime
import mysql.connector as sqlcon
import pymysql

#=========================================================================================================================================
con=sqlcon.connect(host="localhost",user="root",password="Aman1234")#connection to mysql 
cur=con.cursor()
cur = con.cursor(buffered=True)
cur.execute("create database if not exists travell")
cur.execute("use travell")
cur.execute("create table if not exists new"
        "("
        "Receipt_Ref varchar(50),"
        "DateofOrder char(50),"
        "Firstname char(50),"
        "Surname char(50),"
        "Address char(50),"
        "PostCode varchar(50),"
        "Telephone varchar(50),"
        "Mobile varchar(50),"
        "Email varchar(50),"
        "var11 varchar(50),"
        "var12 varchar(50),"
        "var13 varchar(50),"
        "Standard varchar(50),"
        "Economy varchar(50),"
        "FirstClass varchar(50),"
        "PaidTax varchar(50),"
        "SubTotal varchar(50),"
        "TotalCosx varchar(50))")
       



class Travel:

    def __init__(self,root):
        self.root = root
        self.root.title("ASRD Airways")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='black')

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()    

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=StringVar()
        var12=StringVar()
        var13=StringVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Mobile=StringVar()
        Email=StringVar()

        AirportTax =StringVar()
        Mile =StringVar()
        Travel_Ins =StringVar()
        Luggage =StringVar()

        Standard=StringVar()
        Economy=StringVar()
        FirstClass=StringVar()


        AirportTax.set("0")
        Mile.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")

        Standard.set("0")
        Economy.set("0")
        FirstClass.set("0")

        
#========================================Defined Function======================================
        
        def iExit():
            iExit=tkinter.messagebox.askyesno("ASRD Airways","Are you sure want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():

            AirportTax.set("0")
            Mile.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            Economy.set("0")
            FirstClass.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            Mobile.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")            
            self.txtReceipt.delete("1.0",END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set("0")
            var12.set("0")
            var13.set("0")

            self.cboDeparture.current(0)
            self.cboDestination.current(0)
            self.cboAccommodation.current(0)

            self.txtAirportTax.configure(state =DISABLED)
            self.txtMile.configure(state =DISABLED)
            self.txtTravelling_Insurance.configure(state =DISABLED)
            self.txtExt_Luggage.configure(state =DISABLED)
            
            self.txtStandard.configure(state =DISABLED)
            self.txtEconomy.configure(state =DISABLED)
            self.txtFirstClass.configure(state =DISABLED)

        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853, 500831)
            randomRef = str(x)
            Receipt_Ref.set("Travel Bill: " + randomRef)

            self.txtReceipt.insert(END,'Receipt Ref:\t\t\t\t\t' + Receipt_Ref.get() + "\n")
            self.txtReceipt.insert(END,'Date:\t\t\t\t\t' + DateofOrder.get() + "\n")
            self.txtReceipt.insert(END,'Flight:\t\t\t\t\t' + "Travelling Details \n")
            self.txtReceipt.insert(END,'Firstname:\t\t\t\t\t' + Firstname.get() + "\n")
            self.txtReceipt.insert(END,'Surname:\t\t\t\t\t' + Surname.get() + "\n")
            self.txtReceipt.insert(END,'Address:\t\t\t\t\t' + Address.get() + "\n")
            self.txtReceipt.insert(END,'PostCode: \t\t\t\t\t' + PostCode.get()+ "\n")
            self.txtReceipt.insert(END,'Telephone: \t\t\t\t\t' + Telephone.get()+ "\n")
            self.txtReceipt.insert(END,'Mobile: \t\t\t\t\t' + Mobile.get() + "\n")
            self.txtReceipt.insert(END,'Email: \t\t\t\t\t'+ Email.get()+ "\n")
            self.txtReceipt.insert(END,'Standard: \t\t\t\t\t'+ var11.get()+ "\n")
            self.txtReceipt.insert(END,'Economy: \t\t\t\t\t'+ var12.get()+ "\n")
            self.txtReceipt.insert(END,'FirstClass: \t\t\t\t\t'+ var13.get()+ "\n")
            self.txtReceipt.insert(END,'Standard: \t\t\t\t\t'+ Standard.get()+ "\n")
            self.txtReceipt.insert(END,'Economy: \t\t\t\t\t'+ Economy.get()+ "\n")
            self.txtReceipt.insert(END,'FirstClass: \t\t\t\t\t'+ FirstClass.get()+ "\n")
            self.txtReceipt.insert(END,'Paid:\t\t\t\t\t' + PaidTax.get()+"\n")
            self.txtReceipt.insert(END,'SubTotal:\t\t\t\t\t' + str(SubTotal.get()) +"\n")
            self.txtReceipt.insert(END,'Total Cost:\t\t\t\t\t' + str(TotalCost.get()))
#===========================================================SQL ADDITION =======================================================================


            sqlCon = pymysql.connect(host="localhost", user="root",password="scott",database="travell")
            cur=sqlCon.cursor()
            cur.execute("insert into new values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                Receipt_Ref.get(),
                DateofOrder.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                PostCode.get(),
                Telephone.get(),
                Mobile.get(),
                Email.get(),
                var11.get(),
                var12.get(),
                var13.get(),
                Standard.get(),
                Economy.get(),
                FirstClass.get(),
                PaidTax.get(),
                SubTotal.get(),
                TotalCost.get()
                ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("success","record entered succefully")



        def Airport_Tax():
            global paid1
            if (var1.get() == 1):
                self.txtAirportTax.configure(state= NORMAL)                       
                Item1=float(45)
                
                AirportTax.set("INR" + str(Item1))
                paid1 = AirportTax.get()
                AirportTax.set("INR" + str(Item1))
            elif var1.get()== 0:
                self.txtAirportTax.configure(state= DISABLED)
                AirportTax.set("0")


        def Mileage():
            global Item2
            if (var2.get() == 1):
                self.txtMile.configure(state= NORMAL)                       
                Item2=(23345)
                Mile.set((Item2))
            elif var1.get()== 0:
                self.txtMile.configure(state= DISABLED)
                Mile.set("0")

        def Travelling():
            global Item3
            if (var3.get() == 1):
                self.txtTravelling_Insurance.configure(state= NORMAL)                      
                Item3=float(63)
                Travel_Ins.set("INR" + str(Item3))
            elif var3.get()== 0:
                self.txtTravelling_Insurance.configure(state= DISABLED)
                Travel_Ins.set("0")

        
        def Lug():
            global Item4
            if (var4.get() == 1):
                self.txtExt_Luggage.configure(state= NORMAL)                      
                Item4=float(334.59)
                Luggage.set("INR" + str(Item4))
            elif var4.get()== 0:
                self.txtExt_Luggage.configure(state= DISABLED)
                Luggage.set("0")

        def Standard_Fees():
            global Item5
            if (var5.get() == 1):
                self.txtStandard.configure(state= NORMAL)                      
                Item5=float(274.9)
                Standard.set("INR" + str(Item5))
            elif var5.get()== 0:
                self.txtStandard.configure(state= DISABLED)
                Standard.set("0")


        def Economy_Fees():
            global Item6
            if (var7.get() == 1):
                self.txtEconomy.configure(state= NORMAL)                      
                Item6=float(365.5)
                Economy.set("INR" + str(Item6))
            elif var7.get()== 0:
                self.txtEconomy.configure(state= DISABLED)
                Economy.set("0")

        def FirstClass_Fees():
            global Item7
            if (var9.get() == 1 ):
                self.txtFirstClass.configure(state= NORMAL)                      
                Item7=float(564.3)
                FirstClass.set("INR" + str(Item7))
            elif (var9.get() == 0):
                self.txtFirstClass.configure(state= DISABLED)                      
                FirstClass.set("0")

        def Total_Paid():
            if ( var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 and
                 var5.get() == 1 and  var11.get() =="Delhi"
                 and var12.get()=="Kolkata" and var13.get() =="1"):        
                
                q1 =float(45)
                q2 =float(63)
                q3 =float(334.59)
                q4 = float(274.9)

               
                Cost_of_Fare = q1 + q2 + q3 + q4 
                
                Tax="INR"+ str('%.2f'%((Cost_of_Fare)*0.09))
                ST="INR"+ str('%.2f'%((Cost_of_Fare)))
                TT =  "INR"+ str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
                
            elif ( var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 and
                 var7.get() == 1 and var11.get() =="Kolkata"
                 and var12.get()=="Delhi" and var13.get() =="1"):        
                
                q1 =float(45)
                q2 =float(63)
                q3 =float(334.59)                
                q4 = float(365.5)
                
               
                Cost_of_Fare = q1 + q2 + q3 + q4 
                
                Tax="INR"+ str('%.2f'%((Cost_of_Fare)*0.09))
                ST="INR"+ str('%.2f'%((Cost_of_Fare)))
                TT =  "INR"+ str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif ( var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 and
                 var9.get() == 1 and var11.get() =="Mumbai"
                 and var12.get()=="Delhi" and var13.get() =="1"):        
                
                q1 =float(45)
                q2 =float(63)
                q3 =float(334.59)
                q4 = float(564.3)
               
                Cost_of_Fare = q1 + q2 + q3 + q4 
                
                Tax="INR "+ str('%.2f'%((Cost_of_Fare)*0.09))
                ST="INR "+ str('%.2f'%((Cost_of_Fare)))
                TT =  "INR "+ str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif ( var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 and
                 var9.get() == 1 and var11.get() =="Mumbai"
                 and var12.get()=="Kolkata" and var13.get() =="1"):        
                
                q1 =float(45)
                q2 =float(63)
                q3 =float(334.59)
                q4 = float(564.3)
               
                Cost_of_Fare = q1 + q2 + q3 + q4 
                
                Tax="INR "+ str('%.2f'%((Cost_of_Fare)*0.09))
                ST="INR "+ str('%.2f'%((Cost_of_Fare)))
                TT =  "INR "+ str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif ( var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 and
                 var9.get() == 1 and var11.get() =="Delhi"
                 and var12.get()=="Mumbai" and var13.get() =="1"):        
                
                q1 =float(45)
                q2 =float(63)
                q3 =float(334.59)
                q4 = float(564.3)
               
                Cost_of_Fare = q1 + q2 + q3 + q4 
                
                Tax="INR "+ str('%.2f'%((Cost_of_Fare)*0.09))
                ST="INR "+ str('%.2f'%((Cost_of_Fare)))
                TT =  "INR "+ str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)



            
                

        #==============================================================================================
        MainFrame=Frame(self.root)
        MainFrame.grid()

        Tops = Frame(MainFrame, bd=20, width=750,relief=RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle=Label(Tops, font=('arial',70,'bold'),width=25,bg="blue",fg="white",text="ASRD Airways")
        self.lblTitle.grid()
        #==============================================================================================
        CustomerDetailsFrame=Frame(MainFrame, width=750,height=500, bd=20, pady=5,relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)

        FrameDetails=Frame(CustomerDetailsFrame, width=600,height=400, bd=10,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250, bd=10,
                                font=('arial',12,'bold'), text='Customer Details', relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10,width=300,height=250,
                    font=('arial',12, 'bold'),text = 'Travel Details',relief=RIDGE)
        TravelFrame.grid(row=0,column=1)
        
        Ticket_Frame = LabelFrame(FrameDetails, width=300,height=150,relief=FLAT)
        Ticket_Frame.grid(row=1,column=0)
    
        CostFrame = LabelFrame(FrameDetails, width=150,height=150,relief=FLAT)
        CostFrame.grid(row=1,column=1)

        #==============================================================================================
        Receipt_ButtonFrame=Frame(CustomerDetailsFrame, bd=10,width=350,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=300, 
                                font=('arial',12,'bold'), text='Receipt', relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350,height=100,relief=RIDGE)
                                
        ButtonFrame.grid(row=1,column=0)

        #=====================================CustomerName==========================================
        self.lblFirstname = Label(CustomerName,font=('arial', 14,'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=0,column=0, sticky=W)
        self.txtFirstname  = Entry(CustomerName,font=('arial', 14,'bold'), textvariable=Firstname, bd=7, 
                               insertwidth=2, justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)

        self.lblSurname = Label(CustomerName,font=('arial', 14,'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=1,column=0, sticky=W)
        self.txtSurname= Entry(CustomerName,font=('arial', 14,'bold'), textvariable=Surname, bd=7,
                                  insertwidth=2, justify=RIGHT)
        self.txtSurname.grid(row=1,column=1)

        self.lblAddress = Label(CustomerName,font=('arial', 14,'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=2,column=0, sticky=W)
        self.txtAddress = Entry(CustomerName,font=('arial', 14,'bold'), textvariable=Address, bd=7,
                                  insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)

        self.lblPostCode = Label(CustomerName,font=('arial', 14,'bold'), text="Post Code", bd=7)
        self.lblPostCode .grid(row=3,column=0, sticky=W)
        self.txtPostCode   = Entry(CustomerName,font=('arial', 14,'bold'), textvariable=PostCode , bd=7, 
                               insertwidth=2, justify=RIGHT)
        self.txtPostCode .grid(row=3,column=1)

        self.lblTelephone = Label(CustomerName,font=('arial', 14,'bold'), text="Telephone", bd=7)
        self.lblTelephone.grid(row=4,column=0, sticky=W)
        self.txtTelephone= Entry(CustomerName,font=('arial', 14,'bold'), textvariable=Telephone, bd=7, 
                                  insertwidth=2, justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.Mobile  = Label(CustomerName,font=('arial', 14,'bold'), text="Mobile No.", bd=7)
        self.Mobile.grid(row=5,column=0, sticky=W)
        self.Mobile  = Entry(CustomerName,font=('arial', 14,'bold'), textvariable=Mobile, bd=7,
                                  insertwidth=2,justify=RIGHT)
        self.Mobile.grid(row=5,column=1)

        self.lblEmail = Label(CustomerName,font=('arial', 14,'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=6,column=0, sticky=W)
        self.txtEmail = Entry(CustomerName,font=('arial', 14,'bold'), textvariable=Email, bd=7,
                                  insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)

        #======================================Flight Information=====================================
        self.lblDeparture = Label(TravelFrame,font=('arial', 14,'bold'), text="Departure", bd=7)
        self.lblDeparture.grid(row=0,column=0, sticky=W)

        self.cboDeparture =ttk.Combobox(TravelFrame, textvariable = var11, state='readonly', font=('arial',20, 'bold'),
                                     width=14)
        self.cboDeparture['value']=('','Delhi', 'Mumbai','Kolkata','Luton')
        self.cboDeparture.current(0)
        self.cboDeparture.grid(row=0,column=1)

        self.lblDestination = Label(TravelFrame,font=('arial', 14,'bold'), text="Destination", bd=7)
        self.lblDestination.grid(row=1,column=0, sticky=W)

        self.cboDestination =ttk.Combobox(TravelFrame,textvariable = var12, state='readonly', font=('arial',20, 'bold'),
                                     width=14)
        self.cboDestination['value']=('','Delhi', 'Mumbai','Kolkata')
        self.cboDestination.current(0)
        self.cboDestination.grid(row=1,column=1)

        self.lblAccommodation = Label(TravelFrame,font=('arial', 14,'bold'), text="Accommodation", bd=7)
        self.lblAccommodation.grid(row=2,column=0, sticky=W)
     
        self.cboAccommodation =ttk.Combobox(TravelFrame,textvariable = var13,state='readonly',font=('arial',20, 'bold'),
                                     width=14)
        self.cboAccommodation['value']=('','1', '2','3','4')
        self.cboAccommodation.current(1)
        self.cboAccommodation.grid(row=2,column=1)
        #==============================================================================================
        self.chkAirportTax=Checkbutton(TravelFrame,text="Airport Tax",variable = var1, onvalue=1, offvalue=0,
                                       font=('arial', 16,'bold'), command=Airport_Tax).grid(row =3, column=0, sticky=W)
        self.txtAirportTax = Entry(TravelFrame,font=('arial', 14,'bold'), textvariable=AirportTax, bd=7,
                                  insertwidth=2,state = DISABLED,justify=RIGHT)
        self.txtAirportTax.grid(row=3,column=1)

        self.chkMile =  Checkbutton(TravelFrame, text="Air  Mile", variable=var2, onvalue = 1, offvalue = 0,
                 font=('arial',16, 'bold'),command=Mileage).grid(row=4, column=0,sticky=W)
        self.txtMile= Entry(TravelFrame,font=('arial', 14,'bold'), textvariable=Mile, bd=7, 
                                  insertwidth=2,state= DISABLED,  justify=RIGHT)
        self.txtMile.grid(row=4,column=1)

        self.chkTravelling_Insurance =  Checkbutton(TravelFrame, text="Travelling Insurance ", variable=var3,
                                               onvalue = 1, offvalue = 0,
                 font=('arial',16, 'bold'), command= Travelling).grid(row=5, column=0,sticky=W)

        self.txtTravelling_Insurance= Entry(TravelFrame,font=('arial', 14,'bold'), textvariable=Travel_Ins, bd=7,
                                  insertwidth=2,state= DISABLED,  justify=RIGHT)
        self.txtTravelling_Insurance.grid(row=5,column=1)
        
        self.chkExt_Luggage  =  Checkbutton(TravelFrame, text="Ext. Luggage", variable=var4, onvalue = 1, offvalue = 0,
                 font=('arial',16, 'bold'), command= Lug).grid(row=6, column=0,sticky=W)
        self.txtExt_Luggage= Entry(TravelFrame,font=('arial', 14,'bold'), textvariable=Luggage, bd=7,
                                  insertwidth=2, state= DISABLED, justify=RIGHT)
        self.txtExt_Luggage.grid(row=6,column=1)

        #=======================================Payment Information====================================

        self.lblPaidTax = Label(CostFrame,font=('arial', 14,'bold'), text="Paid Tax\t\t", bd=7,)
        self.lblPaidTax.grid(row=0,column=2, sticky=W)
        self.txtPaidTax  = Entry(CostFrame,font=('arial', 14,'bold'), textvariable=PaidTax, bd=7, 
                               width=26, justify=RIGHT)
        self.txtPaidTax.grid(row=0,column=3)

        self.lblSubTotal = Label(CostFrame,font=('arial', 14,'bold'), text="Sub Total", bd=7,)
        self.lblSubTotal.grid(row=1,column=2, sticky=W)
        self.txtSubTotal= Entry(CostFrame,font=('arial', 14,'bold'), textvariable=SubTotal, bd=7, 
                                  width=26, justify=RIGHT)
        self.txtSubTotal.grid(row=1,column=3)

        self.lblTotalCost = Label(CostFrame,font=('arial', 14,'bold'), text="Total Cost", bd=7,)
        self.lblTotalCost.grid(row=2,column=2, sticky=W)
        self.txtTotalCost = Entry(CostFrame,font=('arial', 14,'bold'), textvariable=TotalCost, bd=7,
                                  width=26,justify=RIGHT)
        self.txtTotalCost.grid(row=2,column=3)

        #==============================================================================================
        self.chkStandard =Checkbutton(Ticket_Frame,text="Standard", variable=var5, onvalue = 1, offvalue = 0,
                 font=('arial',14, 'bold'),command=Standard_Fees).grid(row=0,column=0)
        self.txtStandard= Entry(Ticket_Frame,font=('arial', 14,'bold'),width=6,textvariable=Standard,bd=5,
                                state =DISABLED,justify=RIGHT)                                   
        self.txtStandard.grid(row=0,column=1)
        
        self.chkSingle =  Checkbutton(Ticket_Frame, text="Single", variable=var6, onvalue = 1, offvalue = 0,
                 font=('arial',14, 'bold')).grid(row=0, column=2,sticky=W)       

        self.chkEconomy =  Checkbutton(Ticket_Frame, text="Economy", variable=var7,onvalue = 1, offvalue = 0,                                               
                 font=('arial',14, 'bold'),command= Economy_Fees).grid(row=1, column=0,sticky=W)

        self.txtEconomy= Entry(Ticket_Frame,font=('arial', 14,'bold'),width=6,textvariable=Economy,bd=5,
                               state =DISABLED,justify=RIGHT)                                  
        self.txtEconomy.grid(row=1,column=1)
        
        self.chkReturn  =  Checkbutton(Ticket_Frame, text="Return", variable=var8, onvalue = 1, offvalue = 0,
                 font=('arial',14, 'bold')).grid(row=1, column=2,sticky=W)        
       
        self.chkFirstClass = Checkbutton(Ticket_Frame,text="FirstClass", variable=var9, onvalue = 1, offvalue = 0,
                 font=('arial',14, 'bold'), command= FirstClass_Fees).grid(row=2,column=0)
        self.txtFirstClass= Entry(Ticket_Frame,font=('arial', 14,'bold'),width=6,textvariable=FirstClass,bd=5,
                                  state =DISABLED,justify=RIGHT)
        self.txtFirstClass.grid(row=2,column=1)
        
        self.chkSpecialsNeeds =  Checkbutton(Ticket_Frame, text="Specials Needs",variable=var10, onvalue = 1,
                      offvalue = 0, font=('arial',14, 'bold')).grid(row=2, column=2,sticky=W)
        #==========================================Receipt=============================================
        self.txtReceipt=Text(ReceiptFrame, width=40, height=21,font=('arial', 10,'bold'))
        self.txtReceipt.grid(row=0,column=0)

        #===========================================Buttons============================================
        self.btnTotal=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4,
                             text='Total', command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4,
                             text='Receipt', command=Receipt).grid(row=0,column=1)
        self.btnReset=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4,
                             text='Reset', command=Reset).grid(row=0,column=2)
        self.btnExit=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4,
                             text='Exit', command=iExit).grid(row=0,column=3)  
        #==============================================================================================

def air():
        if __name__=='__main__':
            root = Toplevel(master)
        
            application = Travel (root)
            root.mainloop()


#======Main Screen======#
master = Tk()                                
master.geometry('1020x750+0+0')
master.title('Travel Agency')
master.configure(bg="medium violet red")
notif = Label(master, font=('Calibri',12))
notif.grid(row=6,sticky=N,pady=10)

def road(): 
	global conn, cursor
	conn = sqlite3.connect('Railway.db')
	c = conn.cursor()
	global root
	global LoginId,count
	global Password
	global FROM
	global DESTINATION
	global Date
	global Name
	global Age,Gender,IdProof
	global variable,variable1,variable2,v2,var
	global DepartureTime, TrainNumber, Number
	
	
	
	   
	
def createWindow():
	    global conn, cursor
	    conn = sqlite3.connect('Railway.db')
	    cursor = conn.cursor()
	    global root
	    global head
	    global FROM
	    global DESTINATION
	    global Date
	    global Name
	    global Age,Gender,Id_Proof
	    global variable,variable1,variable2,v2,var
	    global DepartureTime, TrainNumber, Number
	    root = Toplevel(master)
	    root.title("Railways 1")
	    customFont = tkFont.Font(family="Segoe Print", size=14)
	    root.geometry('1020x750+0+0')
	    root.config(bg='coral')

	    entry1 = Entry(root,justify='center',font=('Slab Serif',3))
	    entry1.place(x=320,y=10)
	
	    entry2 = Entry(root, justify='center',font=('Slab Serif', 3))
	    entry2.place(x=320,y=10)
	
	    entry3 = Entry(root, justify='center',font=('Slab Serif', 3))
	    entry3.place(x=320,y=10)


	    Label(root, text="ASRD Raliways",font=('Gabriola',50,'bold'),fg="gold2", bg="magenta4").place(x=320,y=10)
	
	
	    def fun_1(*args):
	        entry1.insert(10,variable.get())
	    def fun_2(*args):
	        entry2.insert(10,variable1.get())
	    def fun_3(*args):
	        entry3.insert(10,variable2.get())
	
	    variable = StringVar(root)
	    choices = {'Howrah', 'Lucknow','Ranchi','Hatia'}
	    variable.set('Choose')
	    variable.trace("w", fun_1)
	    popupMenu = OptionMenu(root, variable, *choices)
	    popupMenu.place(x=550, y=180,width=200)
	    popupMenu.config(font=('Segoe UI Black',18),bg="light sea green",fg="coral4")
	    Label(root, text="FROM:",font=('Segoe Print',15,'bold'),fg="violetred4", bg="olivedrab2").place(x=220,y=180)
	
	    variable1 = StringVar(root)
	    trains = {'New Delhi','Chandigarh','Patna','Gaya'}
	    variable1.set('Choose')
	    variable1.trace("w", fun_2)
	
	    popupMenu1 = OptionMenu(root, variable1, *trains)
	    Label(root, text="DESTINATION:",font=('Segoe Print',15,'bold'),fg="violetred4", bg="olivedrab2").place(x=220,y=240)
	    popupMenu1.config(font=('Segoe UI Black',18),bg="light sea green",fg="coral4")
	    popupMenu1.place(x=550, y=240,width=200)
	
	    variable2 = StringVar(root)
	    classes = {'1A','2A','3A'}
	    variable2.set('Choose')
	    variable2.trace("w", fun_3)
	
	    popupMenu1 = OptionMenu(root, variable2, *classes)
	    Label(root, text="ALL CLASSES:",font=('Segoe Print',15,'bold'),fg="violetred4", bg="olivedrab2").place(x=220,y=300)
	    popupMenu1.config(font=('Segoe UI Black', 18), bg="light sea green",fg="coral4")
	    popupMenu1.place(x=550, y=300,width=200)
	
	    Label(root,text="DATE:",font=('Segoe Print',15,'bold'),fg="violetred4", bg="olivedrab2").place(x=220,y=360)
	    Date=StringVar()
	    e1=Entry(root,textvariable=Date)
	
	
	    def Check():
	        if len(e1.get()) == 0 or len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
	            tkinter.messagebox.showinfo('Error!!','Select the required options')
	        else:
	            Check1()
	    def Check1():
	        if (entry1.get() == "Lucknow" and entry2.get() == "Chandigarh" and entry3.get() == "3A") or (entry1.get() == "Lucknow" and entry2.get() == "New Delhi" and entry3.get() == "3A"):
	            tkinter.messagebox.showinfo('Sorry!!!','No Trains Available!')
	        else:
	            ops = e1.get()
	
	            len1 = len(ops)
	            if len1==10:
	                date1=ops[0]+ops[1]
	                month1=ops[3]+ops[4]
	                year11=ops[6]+ops[7]+ops[8]+ops[9]
	
	
	            if(len1==10):
	                if(int(date1)<=31 and int(date1)>=1):
	                    if(int(month1)>=1 and int(month1)<=12):
	                        if(int(year11)>=2010 and int(year11)<=2030):
	                            print('')
	                        else:
	                            tkinter.messagebox.showinfo('Error!', 'Enter in Correct DD-MM-YYYY Format')
	                    else:
	                        tkinter.messagebox.showinfo('Error!', 'Enter in Correct DD-MM-YYYY Format')
	                else:
	                    tkinter.messagebox.showinfo('Error!', 'Enter in Correct DD-MM-YYYY Format')
	                root.destroy()
	                Search()
	            else:
	                tkinter.messagebox.showinfo('Error!', 'Enter the date Correctly!')
	
	            #print('list1 print',list1)
	            #window.destroy()
	
	            #Search()
	
	    def Search():
	        global x1
	
	        window1=Toplevel(master)
	        window1.title("Trains' Schedule")
	        window1.config(bg='palevioletred4')
	        window1.geometry('1020x450+0+0')
	       
	
	        height =2
	        width =7
	        for i in range(height):  # Rows
	            for j in range(width):  # Columns
	                e1 = Entry(window1, justify="center",font=('Gabriola',11,'bold'), bg="orange2", fg="red3")
	                e2 = Entry(window1, justify="center",font=('Gabriola',11,'bold'), bg="orange2", fg="red3")
	                e3 = Entry(window1, justify="center",font=('Gabriola',11,'bold'), bg="orange2", fg="red3")
	                e4 = Entry(window1, justify="center",font=('Gabriola',11,'bold'), bg="orange2", fg="red3")
	                e5 = Entry(window1, justify="center",font=('Gabriola',11,'bold'), bg="orange2", fg="red3")
	                e6 = Entry(window1, justify="center",font=('Gabriola',11,'bold'), bg="orange2", fg="red3")
	                e7 = Entry(window1, justify="center",font=('Gabriola',11,'bold'), bg="orange2", fg="red3")
	
	                en8 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e9 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e10 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e11 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e12 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e13 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e14 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	
	                en15 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e16 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e17 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e18 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e19 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e20 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e21 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	
	                en22 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e23 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e24 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e25 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e26 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e27 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e28 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	
	                en29 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e30 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e31 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e32 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e33 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	                e34 = Entry(window1, justify="center",font=('Comic Sans MS',9), bg="light pink")
	                e35 = Entry(window1, justify="center",font=('Comic Sans MS',9),fg="lemon chiffon", bg="firebrick1")
	
	                e1.grid(row=0, column=0)
	                e2.grid(row=0, column=1)
	                e3.grid(row=0, column=2)
	                e4.grid(row=0, column=3)
	                e5.grid(row=0, column=4)
	                e6.grid(row=0, column=5)
	                e7.grid(row=0, column=6)
	                en8.grid(row=1, column=0)
	                e9.grid(row=1, column=1)
	                e10.grid(row=1, column=2)
	                e11.grid(row=1, column=3)
	                e12.grid(row=1, column=4)
	                e13.grid(row=1, column=5)
	                e14.grid(row=1, column=6)
	                en15.grid(row=2, column=0)
	                e16.grid(row=2, column=1)
	                e17.grid(row=2, column=2)
	                e18.grid(row=2, column=3)
	                e19.grid(row=2, column=4)
	                e20.grid(row=2, column=5)
	                e21.grid(row=2, column=6)
	                en22.grid(row=3, column=0)
	                e23.grid(row=3, column=1)
	                e24.grid(row=3, column=2)
	                e25.grid(row=3, column=3)
	                e26.grid(row=3, column=4)
	                e27.grid(row=3, column=5)
	                e28.grid(row=3, column=6)
	                en29.grid(row=4, column=0)
	                e30.grid(row=4, column=1)
	                e31.grid(row=4, column=2)
	                e32.grid(row=4, column=3)
	                e33.grid(row=4, column=4)
	                e34.grid(row=4, column=5)
	                e35.grid(row=4, column=6)
	
	                e1.insert(10, "Train Number")
	                e2.insert(10, "Train Name")
	                e3.insert(10, "FROM")
	                e4.insert(10, "Departure Time")
	                e5.insert(10, "DESTINATION")
	                e6.insert(10, "Arrival")
	                e7.insert(10, "Class")
	
	
	            if variable.get() == "Howrah" and variable1.get()== "New Delhi":
	                    en8.insert(10, "12235")
	
	                    e9.insert(10, "Rajdhani Express")
	                    e10.insert(10, "Howrah")
	                    e11.insert(10, "14:30")
	                    e12.insert(10, "New Delhi")
	                    e13.insert(10, "7:55")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12236")
	
	                    e16.insert(10, "Howrah Juntion")
	                    e17.insert(10, "Howrah")
	                    e18.insert(10, "16:30")
	                    e19.insert(10, "New Delhi")
	                    e20.insert(10, "5:50")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12237")
	                    e23.insert(10, "New Delhi 07")
	                    e24.insert(10, "Howrah")
	                    e25.insert(10, "8:35")
	                    e26.insert(10, "New Delhi")
	                    e27.insert(10, "15:50")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12238")
	                    e30.insert(10, "Anand Vihar")
	                    e31.insert(10, "Howrah")
	                    e32.insert(10, "12:30")
	                    e33.insert(10, "New Delhi")
	                    e34.insert(10, "7:20")
	                    e35.insert(10, "1A,2A,3A")
	
	
	            if variable.get() == "Howrah" and variable1.get()== "Chandigarh":
	                    en8.insert(10, "12239")
                                                                                                                                    
	                    e9.insert(10, "Howrah Amritsar Express")
	                    e10.insert(10, "Howrah")
	                    e11.insert(10, "6:30")
	                    e12.insert(10, "Chandigarh")
	                    e13.insert(10, "18:20")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12240")
	                    e16.insert(10, "Kalka Mail")
	                    e17.insert(10, "Howrah")
	                    e18.insert(10, "14:30")
	                    e19.insert(10, "Chandigarh")
	                    e20.insert(10, "23:30")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12241")
	                    e23.insert(10, "JallianwalaBagh Express")
	                    e24.insert(10, "Howrah")
	                    e25.insert(10, "12:30")
	                    e26.insert(10, "Chandigarh")
	                    e27.insert(10, "8:40")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12242")
	                    e30.insert(10, "Durgiana Express")
	                    e31.insert(10, "Howrah")
	                    e32.insert(10, "8:30")
	                    e33.insert(10, "Chandigarh")
	                    e34.insert(10, "16:20")
	                    e35.insert(10, "1A,2A,3A")

	
	            if variable.get() == "Lucknow" and variable1.get()== "Chandigarh":
	                    en8.insert(10, "12243")
	                    ach12243=12243
	                    e9.insert(10, "Garibrath")
	                    e10.insert(10, "Lucknow")
	                    e11.insert(10, "9:30")
	                    e12.insert(10, "Chandigarh")
	                    e13.insert(10, "14:40")
	                    e14.insert(10, "1A,2A")
	
	                    en15.insert(10, "12244")
	                    e16.insert(10, "Mumbai Bandra (T)")
	                    e17.insert(10, "Lucknow")
	                    e18.insert(10, "1:00")
	                    e19.insert(10, "Chandigarh")
	                    e20.insert(10, "00:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12245")
	                    e23.insert(10, "Pooja SF Express")
	                    e24.insert(10, "Lucknow")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "Chandigarh")
	                    e27.insert(10, "3:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12246")
	                    e30.insert(10, "Gandhidham")
	                    e31.insert(10, "Howrah")
	                    e32.insert(10, "14:05")
	                    e33.insert(10, "Chandigarh")
	                    e34.insert(10, "6:45")
	                    e35.insert(10, "1A,2A")
	
	            if variable.get() == "Lucknow" and variable1.get()== "New Delhi":
	                    en8.insert(10, "12247")
	                    and12247=12247
	                    e9.insert(10, "Uttaranchal Express")
	                    e10.insert(10, "Lucknow")
	                    e11.insert(10, "1:40")
	                    e12.insert(10, "New Delhi")
	                    e13.insert(10, "10:40")
	                    e14.insert(10, "1A,2A")
	
	                    en15.insert(10, "12248")
	                    e16.insert(10, "Rajkot Express")
	                    e17.insert(10, "Lucknow")
	                    e18.insert(10, "6:30")
	                    e19.insert(10, "New Delhi")
	                    e20.insert(10, "10:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12249")
	                    e23.insert(10, "Corbet park link Express")
	                    e24.insert(10, "Lucknow")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "New Delhi")
	                    e27.insert(10, "20:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12250")
	                    e30.insert(10, "Ranikhet Express")
	                    e31.insert(10, "Lucknow")
	                    e32.insert(10, "12:10")
	                    e33.insert(10, "New Delhi")
	                    e34.insert(10, "21:10")
	                    e35.insert(10, "1A,2A")

	            if variable.get() == "Ranchi" and variable1.get()== "New Delhi":
	                    en8.insert(10, "12251")
	
	                    e9.insert(10, "Jan Satabdi Express")
	                    e10.insert(10, "Ranchi")
	                    e11.insert(10, "13:30")
	                    e12.insert(10, "New Delhi")
	                    e13.insert(10, "7:55")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12252")
	
	                    e16.insert(10, "Ranchi Express")
	                    e17.insert(10, "Ranchi")
	                    e18.insert(10, "16:30")
	                    e19.insert(10, "New Delhi")
	                    e20.insert(10, "5:50")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12253")
	                    e23.insert(10, "New Delhi Duronto")
	                    e24.insert(10, "Ranchi")
	                    e25.insert(10, "8:35")
	                    e26.insert(10, "New Delhi")
	                    e27.insert(10, "15:50")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12254")
	                    e30.insert(10, "Ranchi Road Exp.")
	                    e31.insert(10, "Ranchi")
	                    e32.insert(10, "12:30")
	                    e33.insert(10, "New Delhi")
	                    e34.insert(10, "7:20")
	                    e35.insert(10, "1A,2A,3A")
	
	
	            if variable.get() == "Ranchi" and variable1.get()== "Chandigarh":
	                    en8.insert(10, "12255")
	
	                    e9.insert(10, "Ranchi-Amritsar Express")
	                    e10.insert(10, "Ranchi")
	                    e11.insert(10, "6:30")
	                    e12.insert(10, "Chandigarh")
	                    e13.insert(10, "18:20")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12256")
	                    e16.insert(10, "Kalka Mail")
	                    e17.insert(10, "Ranchi")
	                    e18.insert(10, "14:30")
	                    e19.insert(10, "Chandigarh")
	                    e20.insert(10, "23:30")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12257")
	                    e23.insert(10, "Aanchal Express")
	                    e24.insert(10, "Ranchi")
	                    e25.insert(10, "12:30")
	                    e26.insert(10, "Chandigarh")
	                    e27.insert(10, "8:40")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12258")
	                    e30.insert(10, "Samvaad Express")
	                    e31.insert(10, "Ranchi")
	                    e32.insert(10, "8:30")
	                    e33.insert(10, "Chandigarh")
	                    e34.insert(10, "16:20")
	                    e35.insert(10, "1A,2A,3A")

	            if variable.get() == "Hatia" and variable1.get()== "Patna":
	                    en8.insert(10, "12259")
	                    ach12259=12259
	                    e9.insert(10, "Sapnarath")
	                    e10.insert(10, "Hatia")
	                    e11.insert(10, "9:30")
	                    e12.insert(10, "Patna")
	                    e13.insert(10, "14:40")
	                    e14.insert(10, "1A,2A")
	
	                    en15.insert(10, "12260")
	                    e16.insert(10, "Hatia Patna Express")
	                    e17.insert(10, "Hatia")
	                    e18.insert(10, "1:00")
	                    e19.insert(10, "Patna")
	                    e20.insert(10, "00:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12261")
	                    e23.insert(10, "Rajdhani Express")
	                    e24.insert(10, "Hatia")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "Patna")
	                    e27.insert(10, "3:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12262")
	                    e30.insert(10, "Bodhgaya Express")
	                    e31.insert(10, "Hatia")
	                    e32.insert(10, "14:05")
	                    e33.insert(10, "Patna")
	                    e34.insert(10, "6:45")
	                    e35.insert(10, "1A,2A")
	
	            if variable.get() == "Hatia" and variable1.get()== "Gaya":
	                    en8.insert(10, "12263")
	                    and12263=12263
	                    e9.insert(10, "Chotanagpur Express")
	                    e10.insert(10, "Hatia")
	                    e11.insert(10, "1:40")
	                    e12.insert(10, "Gaya")
	                    e13.insert(10, "10:40")
	                    e14.insert(10, "1A,2A")
	
	                    en15.insert(10, "12264")
	                    e16.insert(10, "Rajnath Express")
	                    e17.insert(10, "Hatia")
	                    e18.insert(10, "6:30")
	                    e19.insert(10, "Gaya")
	                    e20.insert(10, "10:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12265")
	                    e23.insert(10, "Gaya Hatia link Express")
	                    e24.insert(10, "Hatia")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "Gaya")
	                    e27.insert(10, "20:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12266")
	                    e30.insert(10, "Maurya Express")
	                    e31.insert(10, "Hatia")
	                    e32.insert(10, "12:10")
	                    e33.insert(10, "Gaya")
	                    e34.insert(10, "21:10")
	                    e35.insert(10, "1A,2A")

	            if variable.get() == "Howrah" and variable1.get()== "Patna":
	                    en8.insert(10, "12267")
	
	                    e9.insert(10, "Rajdhani Express")
	                    e10.insert(10, "Howrah")
	                    e11.insert(10, "14:30")
	                    e12.insert(10, "Patna")
	                    e13.insert(10, "7:55")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12268")
	
	                    e16.insert(10, "Howrah Patna Rath")
	                    e17.insert(10, "Howrah")
	                    e18.insert(10, "16:30")
	                    e19.insert(10, "Patna")
	                    e20.insert(10, "5:50")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12269")
	                    e23.insert(10, "Patna Central Exp.")
	                    e24.insert(10, "Howrah")
	                    e25.insert(10, "8:35")
	                    e26.insert(10, "Patna")
	                    e27.insert(10, "15:50")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12270")
	                    e30.insert(10, "Vastu Vihar Rath")
	                    e31.insert(10, "Howrah")
	                    e32.insert(10, "12:30")
	                    e33.insert(10, "Patna")
	                    e34.insert(10, "7:20")
	                    e35.insert(10, "1A,2A,3A")
	
	
	            if variable.get() == "Howrah" and variable1.get()== "Gaya":
	                    en8.insert(10, "12271")
	
	                    e9.insert(10, "Howrah Gaya Express")
	                    e10.insert(10, "Howrah")
	                    e11.insert(10, "6:30")
	                    e12.insert(10, "Gaya")
	                    e13.insert(10, "18:20")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12272")
	                    e16.insert(10, "Raftaar Express")
	                    e17.insert(10, "Howrah")
	                    e18.insert(10, "14:30")
	                    e19.insert(10, "Gaya")
	                    e20.insert(10, "23:30")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12273")
	                    e23.insert(10, "Bodh Gaya Express")
	                    e24.insert(10, "Howrah")
	                    e25.insert(10, "12:30")
	                    e26.insert(10, "Gaya")
	                    e27.insert(10, "8:40")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12274")
	                    e30.insert(10, "Durrani Express")
	                    e31.insert(10, "Howrah")
	                    e32.insert(10, "8:30")
	                    e33.insert(10, "Gaya")
	                    e34.insert(10, "16:20")
	                    e35.insert(10, "1A,2A,3A")


	            if variable.get() == "Lucknow" and variable1.get()== "Patna":
	                    en8.insert(10, "12275")
	                    ach12275=12275
	                    e9.insert(10, "Lucknow Patna Rath")
	                    e10.insert(10, "Lucknow")
	                    e11.insert(10, "9:30")
	                    e12.insert(10, "Patna")
	                    e13.insert(10, "14:40")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12276")
	                    e16.insert(10, "Lucknow Bengal Rath")
	                    e17.insert(10, "Lucknow")
	                    e18.insert(10, "1:00")
	                    e19.insert(10, "Patna")
	                    e20.insert(10, "00:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12277")
	                    e23.insert(10, "Sandhya Express")
	                    e24.insert(10, "Lucknow")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "Patna")
	                    e27.insert(10, "3:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12278")
	                    e30.insert(10, "Nehru Express")
	                    e31.insert(10, "Lucknow")
	                    e32.insert(10, "14:05")
	                    e33.insert(10, "Patna")
	                    e34.insert(10, "6:45")
	                    e35.insert(10, "1A,2A")
	
	            if variable.get() == "Lucknow" and variable1.get()== "Gaya":
	                    en8.insert(10, "12279")
	                    and12279=12279
	                    e9.insert(10, "Paschim UP Express")
	                    e10.insert(10, "Lucknow")
	                    e11.insert(10, "1:40")
	                    e12.insert(10, "Gaya")
	                    e13.insert(10, "10:40")
	                    e14.insert(10, "1A,2A")
	
	                    en15.insert(10, "12280")
	                    e16.insert(10, "Raniganj Express")
	                    e17.insert(10, "Lucknow")
	                    e18.insert(10, "6:30")
	                    e19.insert(10, "Gaya")
	                    e20.insert(10, "10:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12281")
	                    e23.insert(10, "Spark Express")
	                    e24.insert(10, "Lucknow")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "Gaya")
	                    e27.insert(10, "20:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12282")
	                    e30.insert(10, "Chambal Express")
	                    e31.insert(10, "Lucknow")
	                    e32.insert(10, "12:10")
	                    e33.insert(10, "Gaya")
	                    e34.insert(10, "21:10")
	                    e35.insert(10, "1A,2A")


	            if variable.get() == "Ranchi" and variable1.get()== "Patna":
	                    en8.insert(10, "12283")
	
	                    e9.insert(10, "Jan Satabdi Express")
	                    e10.insert(10, "Ranchi")
	                    e11.insert(10, "13:30")
	                    e12.insert(10, "Patna")
	                    e13.insert(10, "7:55")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12284")
	
	                    e16.insert(10, "Ranchi Juntion")
	                    e17.insert(10, "Ranchi")
	                    e18.insert(10, "16:30")
	                    e19.insert(10, "Patna")
	                    e20.insert(10, "5:50")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12285")
	                    e23.insert(10, "Danapur Cantt Exp.")
	                    e24.insert(10, "Ranchi")
	                    e25.insert(10, "8:35")
	                    e26.insert(10, "Patna")
	                    e27.insert(10, "15:50")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12286")
	                    e30.insert(10, "Bokaro Express")
	                    e31.insert(10, "Ranchi")
	                    e32.insert(10, "12:30")
	                    e33.insert(10, "Patna")
	                    e34.insert(10, "7:20")
	                    e35.insert(10, "1A,2A,3A")
	
	
	            if variable.get() == "Ranchi" and variable1.get()== "Gaya":
	                    en8.insert(10, "12287")
	
	                    e9.insert(10, "Ranchi-Chapra Express")
	                    e10.insert(10, "Ranchi")
	                    e11.insert(10, "6:30")
	                    e12.insert(10, "Gaya")
	                    e13.insert(10, "18:20")
	                    e14.insert(10, "1A,2A,3A")
	
	                    en15.insert(10, "12288")
	                    e16.insert(10, "Jahanabad Rath")
	                    e17.insert(10, "Ranchi")
	                    e18.insert(10, "14:30")
	                    e19.insert(10, "Gaya")
	                    e20.insert(10, "23:30")
	                    e21.insert(10, "1A,2A,3A")
	
	                    en22.insert(10, "12289")
	                    e23.insert(10, "Rana Express")
	                    e24.insert(10, "Ranchi")
	                    e25.insert(10, "12:30")
	                    e26.insert(10, "Gaya")
	                    e27.insert(10, "8:40")
	                    e28.insert(10, "1A,2A,3A")
	
	                    en29.insert(10, "12290")
	                    e30.insert(10, "Anuvaad Express")
	                    e31.insert(10, "Ranchi")
	                    e32.insert(10, "8:30")
	                    e33.insert(10, "Gaya")
	                    e34.insert(10, "16:20")
	                    e35.insert(10, "1A,2A,3A")


	            if variable.get() == "Hatia" and variable1.get()== "New Delhi":
	                    en8.insert(10, "12291")
	                    ach12251=12291
	                    e9.insert(10, "Jannrath")
	                    e10.insert(10, "Hatia")
	                    e11.insert(10, "9:30")
	                    e12.insert(10, "New Delhi")
	                    e13.insert(10, "14:40")
	                    e14.insert(10, "1A,2A")
	
	                    en15.insert(10, "12292")
	                    e16.insert(10, "Hatia Delhi Express")
	                    e17.insert(10, "Hatia")
	                    e18.insert(10, "1:00")
	                    e19.insert(10, "New Delhi")
	                    e20.insert(10, "00:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12293")
	                    e23.insert(10, "Rajdhani Express")
	                    e24.insert(10, "Hatia")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "New Delhi")
	                    e27.insert(10, "3:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12294")
	                    e30.insert(10, "Gorakhpur Express")
	                    e31.insert(10, "Hatia")
	                    e32.insert(10, "14:05")
	                    e33.insert(10, "New Delhi")
	                    e34.insert(10, "6:45")
	                    e35.insert(10, "1A,2A")
	
	            if variable.get() == "Hatia" and variable1.get()== "Chandigarh":
	                    en8.insert(10, "12295")
	                    and12295=12295
	                    e9.insert(10, "Chambal Express")
	                    e10.insert(10, "Hatia")
	                    e11.insert(10, "1:40")
	                    e12.insert(10, "Chandigarh")
	                    e13.insert(10, "10:40")
	                    e14.insert(10, "1A,2A")
	
	                    en15.insert(10, "12296")
	                    e16.insert(10, "Yuvraj Express")
	                    e17.insert(10, "Hatia")
	                    e18.insert(10, "6:30")
	                    e19.insert(10, "Chandigarh")
	                    e20.insert(10, "10:45")
	                    e21.insert(10, "1A,2A")
	
	                    en22.insert(10, "12297")
	                    e23.insert(10, "Chandigarh Hatia link Express")
	                    e24.insert(10, "Hatia")
	                    e25.insert(10, "11:05")
	                    e26.insert(10, "Chandigarh")
	                    e27.insert(10, "20:00")
	                    e28.insert(10, "1A,2A")
	
	                    en29.insert(10, "12298")
	                    e30.insert(10, "Rajdhani Express")
	                    e31.insert(10, "Hatia")
	                    e32.insert(10, "12:10")
	                    e33.insert(10, "Chandigarh")
	                    e34.insert(10, "21:10")
	                    e35.insert(10, "1A,2A")

	        def PassengerDetails1():
	            global x1
	
	            if en8.get()=="12235":
	                x1=12235
	            elif en8.get()=="12239":
	                x1=12239
	            elif en8.get() == "12243":
	                x1 = 12243
	            else:
	                x1 = 12247
	
	            def PassengerDetails():
	                window1.destroy()
	                window2 = Toplevel(master)
	                window2.title("Passenger Details")
	                window2.config(bg="indianred2")
	                screen_width = window2.winfo_screenwidth()
	                screen_height = window2.winfo_screenheight()
	                width = 1020
	                height = 700
	                x = (screen_width / 2) - (width / 2)
	                y = (screen_height / 2) - (height / 2)
	                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                
	
	                height = 5
	                width = 5
	                for i in range(height):  # Rows
	                    for j in range(width):  # Columns
	                        e1 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn2 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn3 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn4 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e5 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e6 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn7 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn8 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn9 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e10 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e11 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e12 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e13 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e14 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e15 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e16 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e17 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e18 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e19 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e20 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e21 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e22 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e23 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e24 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e25 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	
	                        e1.insert(10, "S.no")
	                        enn2.insert(10, "Name")
	                        enn3.insert(10, "Age")
	                        enn4.insert(10, "Gender")
	                        e5.insert(10, "Id_Proof")
	                        e6.insert(10, "1.")
	
	                        e11.insert(10, "2.")
	                        e16.insert(10, "3.")
	                        e21.insert(10, "4.")
	
	                        e1.grid(row=0, column=0)
	                        enn2.grid(row=0, column=1)
	                        enn3.grid(row=0, column=2)
	                        enn4.grid(row=0, column=3)
	                        e5.grid(row=0, column=4)
	                        e6.grid(row=1, column=0)
	                        enn7.grid(row=1, column=1)
	                        enn8.grid(row=1, column=2)
	                        enn9.grid(row=1, column=3)
	                        e10.grid(row=1, column=4)
	
	                        e11.grid(row=2, column=0)
	                        e12.grid(row=2, column=1)
	                        e13.grid(row=2, column=2)
	                        e14.grid(row=2, column=3)
	                        e15.grid(row=2, column=4)
	
	                        e16.grid(row=3, column=0)
	                        e17.grid(row=3, column=1)
	                        e18.grid(row=3, column=2)
	                        e19.grid(row=3, column=3)
	                        e20.grid(row=3, column=4)
	
	                        e21.grid(row=4, column=0)
	                        e22.grid(row=4, column=1)
	                        e23.grid(row=4, column=2)
	                        e24.grid(row=4, column=3)
	                        e25.grid(row=4, column=4)
	
	                        def fun(*args):
	                            enn9.insert(10, v2.get())
	
	                        def fun1(*args):
	                            e14.insert(10, v3.get())
	
	                        def fun2(*args):
	                            e19.insert(10, v4.get())
	
	                        def fun3(*args):
	                            e24.insert(10, v5.get())
	
	                        def fun4(*args):
	                            e10.insert(10, v6.get())
	
	                        def fun5(*args):
	                            e15.insert(10, v7.get())
	
	                        def fun6(*args):
	                            e20.insert(10, v8.get())
	
	                        def fun7(*args):
	                            e25.insert(10, v9.get())
	
	                        v2 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v2.set('Choose')
	                        v2.trace("w", fun)
	                        popupMenu1 = OptionMenu(window2, v2, *gender)
	                        popupMenu1.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu1.grid(row=1, column=3)
	
	                        v3 = StringVar(window2)
	                        gender1 = {'Male', 'Female'}
	                        v3.set('Choose')
	                        v3.trace("w", fun1)
	                        popupMenu2 = OptionMenu(window2, v3, *gender1)
	                        popupMenu2.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu2.grid(row=2, column=3)
	
	                        v4 = StringVar(window2)
	                        gender2 = {'Male', 'Female'}
	                        v4.set('Choose')
	                        v4.trace("w", fun2)
	                        popupMenu3 = OptionMenu(window2, v4, *gender2)
	                        popupMenu3.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu3.grid(row=3, column=3)
	
	                        v5 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v5.set('Choose')
	                        v5.trace("w", fun3)
	                        popupMenu4 = OptionMenu(window2, v5, *gender)
	                        popupMenu4.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu4.grid(row=4, column=3)
	
	                        v6 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v6.set('Choose')
	                        v6.trace("w", fun4)
	                        popup = OptionMenu(window2, v6, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=1, column=4)
	
	                        v7 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v7.set('Choose')
	                        v7.trace("w", fun5)
	                        popup = OptionMenu(window2, v7, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=2, column=4)
	
	                        v8 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v8.set('Choose')
	                        v8.trace("w", fun6)
	                        popup = OptionMenu(window2, v8, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=3, column=4)
	
	                        v9 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v9.set('Choose')
	                        v9.trace("w", fun7)
	                        popup = OptionMenu(window2, v9, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	
	                        popup.grid(row=4, column=4)
	
	                def Check1():
	
	                    def Show():
	
	                        global x1,count
	                        window3 = Toplevel(master)
	
	                        window3.title("Ticket")
	                        screen_width = window3.winfo_screenwidth()
	                        screen_height = window3.winfo_screenheight()
	                        width = 780
	                        height = 480
	                        x = (screen_width / 2) - (width / 2)
	                        y = (screen_height / 2) - (height / 2)
	                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                        window3.config(bg='gray23')
	
	                        Label(window3, text="Name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=50)
	                        Label(window3, text="Gender:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=50)
	                        Label(window3, text="Departure time:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=90)
	                        Label(window3, text="Age:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=90)
	                        Label(window3, text="Class:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=130)
	                        Label(window3, text="Train no.:",bg='dark turquoise',font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=130)
	                        Label(window3, text="Train name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=170)
	                        Label(window3, text="Source:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=210)
	                        Label(window3, text="Destination:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=250)
	                        Label(window3, text="No. of tickets:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=290)
	
	                        Label(window3, text="PNR no.:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=170)
	
	                        Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10)).place(x=170, y=290,  height=25)
	
	
	                        Class = Label(window3, justify="center",bg='white',text=variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
	                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
	                        TrainNumber.place(x=170, y=130, height=25)
	
	
	                        global conn, cursor, x1, x2
	                        if x1 == 12235:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12235")
	                            fetch = cursor.fetchall()
	
	
	                            for data in fetch:
	                                Source = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[5],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	                            a=111111
	                            b=999999
	                            pnr=(random.randint(a, b))
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()),int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ",(pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3, justify="center",bg='white',text=data[0],
	                                            font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3,text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(x=170, y=50,height=25)
	                                Age = Label(window3,text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(x=380, y=90, height=25)
	                                Gender = Label(window3,text=data[3] ,bg='white',justify="center", font=('Slab Serif', 9)).place(x=380, y=50, height=25)
	
	
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12239:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12239")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2], justify="center",bg='white',
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[5], justify="center",bg='white',
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12243:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12243")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	                                pnr1 = Label(window3, justify="center",bg='white',text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12247:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12247")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5], justify="center",bg='white', font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2], justify="center",bg='white',
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1], justify="center",bg='white',
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	
	                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	
	
	
	                        Label(window3, text="Have a happy & safe Journey!!",bg='white',fg='orange red',font=('Comic Sans MS', 23,'bold')).place(x=200, y=340)
	
	                        mainloop()
	
	
	
	                    global count
	                    count=0
	                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
	                            e15.get()) != 0) and (
	                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
	                        e25.get()) != 0) and (
	                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
	                            e10.get()) != 0) and (
	                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
	                        e20.get()) != 0) and (
	                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
	                        count=1
	                        Show()
	                    elif e12.get()!="" and e17.get()=="":
	                        count=2
	                        Show()
	                    elif e17.get()!="" and e22.get()=="":
	                        count=3
	                        Show()
	                    elif e22.get()!="":
	                        count=4
	                        Show()
	                    else:
	                        Show()
	
	                b = Button(window2, text='Proceed', bg="slategray3", font=('Britannic Bold', 16), command=Check1)
	                b.place(x=450, y=255)
	
	                mainloop()
	
	            PassengerDetails()
	
	        def PassengerDetails2():
	            global x1
	            if en15.get()=="12236":
	                x1=12236
	            elif en15.get()=="12240":
	                x1=12240
	            elif en15.get() == "12244":
	                x1 = 12244
	            else:
	                x1 = 12248
	
	            def PassengerDetails():
	                window1.destroy()
	                window2 = Toplevel(master)
	                window2.title("Passenger Details")
	                window2.config(bg="indianred2")
	                screen_width = window2.winfo_screenwidth()
	                screen_height = window2.winfo_screenheight()
	                width = 1020
	                height = 700
	                x = (screen_width / 2) - (width / 2)
	                y = (screen_height / 2) - (height / 2)
	                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                
	
	                height = 5
	                width = 5
	                for i in range(height):  # Rows
	                    for j in range(width):  # Columns
	                        e1 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn2 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn3 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn4 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e5 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e6 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn7 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn8 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn9 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e10 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e11 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e12 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e13 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e14 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e15 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e16 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e17 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e18 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e19 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e20 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e21 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e22 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e23 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e24 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e25 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	
	                        e1.insert(10, "S.no")
	                        enn2.insert(10, "Name")
	                        enn3.insert(10, "Age")
	                        enn4.insert(10, "Gender")
	                        e5.insert(10, "Id_Proof")
	                        e6.insert(10, "1")
	
	                        e11.insert(10, "2")
	                        e16.insert(10, "3")
	                        e21.insert(10, "4")
	
	                        e1.grid(row=0, column=0)
	                        enn2.grid(row=0, column=1)
	                        enn3.grid(row=0, column=2)
	                        enn4.grid(row=0, column=3)
	                        e5.grid(row=0, column=4)
	                        e6.grid(row=1, column=0)
	                        enn7.grid(row=1, column=1)
	                        enn8.grid(row=1, column=2)
	                        enn9.grid(row=1, column=3)
	                        e10.grid(row=1, column=4)
	
	                        e11.grid(row=2, column=0)
	                        e12.grid(row=2, column=1)
	                        e13.grid(row=2, column=2)
	                        e14.grid(row=2, column=3)
	                        e15.grid(row=2, column=4)
	
	                        e16.grid(row=3, column=0)
	                        e17.grid(row=3, column=1)
	                        e18.grid(row=3, column=2)
	                        e19.grid(row=3, column=3)
	                        e20.grid(row=3, column=4)
	
	                        e21.grid(row=4, column=0)
	                        e22.grid(row=4, column=1)
	                        e23.grid(row=4, column=2)
	                        e24.grid(row=4, column=3)
	                        e25.grid(row=4, column=4)
	
	                        def fun(*args):
	                            enn9.insert(10, v2.get())
	
	                        def fun1(*args):
	                            e14.insert(10, v3.get())
	
	                        def fun2(*args):
	                            e19.insert(10, v4.get())
	
	                        def fun3(*args):
	                            e24.insert(10, v5.get())
	
	                        def fun4(*args):
	                            e10.insert(10, v6.get())
	
	                        def fun5(*args):
	                            e15.insert(10, v7.get())
	
	                        def fun6(*args):
	                            e20.insert(10, v8.get())
	
	                        def fun7(*args):
	                            e25.insert(10, v9.get())
	
	                        v2 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v2.set('Choose')
	                        v2.trace("w", fun)
	                        popupMenu1 = OptionMenu(window2, v2, *gender)
	                        popupMenu1.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu1.grid(row=1, column=3)
	
	                        v3 = StringVar(window2)
	                        gender1 = {'Male', 'Female'}
	                        v3.set('Choose')
	                        v3.trace("w", fun1)
	                        popupMenu2 = OptionMenu(window2, v3, *gender1)
	                        popupMenu2.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu2.grid(row=2, column=3)
	
	                        v4 = StringVar(window2)
	                        gender2 = {'Male', 'Female'}
	                        v4.set('Choose')
	                        v4.trace("w", fun2)
	                        popupMenu3 = OptionMenu(window2, v4, *gender2)
	                        popupMenu3.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu3.grid(row=3, column=3)
	
	                        v5 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v5.set('Choose')
	                        v5.trace("w", fun3)
	                        popupMenu4 = OptionMenu(window2, v5, *gender)
	                        popupMenu4.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu4.grid(row=4, column=3)
	
	                        v6 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v6.set('Choose')
	                        v6.trace("w", fun4)
	                        popup = OptionMenu(window2, v6, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=1, column=4)
	
	                        v7 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v7.set('Choose')
	                        v7.trace("w", fun5)
	                        popup = OptionMenu(window2, v7, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=2, column=4)
	
	                        v8 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v8.set('Choose')
	                        v8.trace("w", fun6)
	                        popup = OptionMenu(window2, v8, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=3, column=4)
	
	                        v9 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v9.set('Choose')
	                        v9.trace("w", fun7)
	                        popup = OptionMenu(window2, v9, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=4, column=4)
	
	                def Check1():
	
	                    def Show():
	                        global x1
	                        window3 = Tk()
	                        window3.title("Ticket")
	                        screen_width = window3.winfo_screenwidth()
	                        screen_height = window3.winfo_screenheight()
	                        width = 780
	                        height = 480
	                        x = (screen_width / 2) - (width / 2)
	                        y = (screen_height / 2) - (height / 2)
	                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                        window3.config(bg='gray23')
	
	                        Label(window3, text="Name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=50)
	                        Label(window3, text="Gender:",bg='dark turquoise',font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=50)
	                        Label(window3, text="Departure time:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=90)
	                        Label(window3, text="Age:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=90)
	                        Label(window3, text="Class:",bg='dark turquoise',font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=130)
	                        Label(window3, text="Train no.:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=130)
	                        Label(window3, text="Train name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=170)
	                        Label(window3, text="Source:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=210)
	                        Label(window3, text="Destination:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=250)
	                        Label(window3, text="No. of tickets:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=290)
	
	                        Label(window3, text="PNR no.:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=170)
	
	                        Name = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
	                        Gender = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
	                        DepartureTime = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=210, y=90,
	                                                                                                       height=25)
	                        Age = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=90, height=25)
	                        Class = Label(window3, justify="center",bg='white',text=variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
	                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
	                        TrainNumber.place(x=170, y=130, height=25)
	
	                        Source = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
	                        Destination = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=180, y=250,
	                                                                                                     height=25)
	                        Number = Label(window3,text=count, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=290, height=25)
	                        global conn, cursor, x1, x2
	
	                        if x1 == 12236:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12236")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5], justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2], justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1], justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3], justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12240:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12240")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12244:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12244")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12248:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12248")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170,
	                                    height=25)
	
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	
	
	                        Label(window3, text="Have a happy & safe Journey!!",bg='white',fg='orange red',font=('Comic Sans MS', 23,'bold')).place(x=200, y=340)
	
	                        mainloop()
	
	                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
	                            e15.get()) != 0) and (
	                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
	                        e25.get()) != 0) and (
	                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
	                            e10.get()) != 0) and (
	                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
	                        e20.get()) != 0) and (
	                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
	                        count=1
	                        Show()
	                    elif e12.get()!="" and e17.get()=="":
	                        count=2
	                        Show()
	                    elif e17.get()!="" and e22.get()=="":
	                        count=3
	                        Show()
	                    elif e22.get()!="":
	                        count=4
	                        Show()
	                    else:
	                        Show()
	
	                b = Button(window2, text='Proceed', bg="slategray3", font=('Britannic Bold', 16), command=Check1)
	                b.place(x=450, y=255)
	
	                mainloop()
	
	            PassengerDetails()
	
	        def PassengerDetails3():
	            global x1
	            if en22.get() == "12237":
	                x1 = 12237
	            elif en22.get() == "12241":
	                x1 = 12241
	            elif en22.get() == "12245":
	                x1 = 12245
	            else:
	                x1 = 12249
	
	            def PassengerDetails():
	                window1.destroy()
	                window2 = Toplevel(master)
	                window2.title("Passenger Details")
	                window2.config(bg="indianred2")
	                screen_width = window2.winfo_screenwidth()
	                screen_height = window2.winfo_screenheight()
	                width = 1020
	                height = 700
	                x = (screen_width / 2) - (width / 2)
	                y = (screen_height / 2) - (height / 2)
	                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                
	
	                height = 5
	                width = 5
	                for i in range(height):  # Rows
	                    for j in range(width):  # Columns
	                        e1 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn2 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn3 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn4 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e5 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e6 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn7 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn8 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn9 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e10 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e11 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e12 = Entry(window2, justify="center",font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e13 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e14 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e15 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e16 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e17 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e18 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e19 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e20 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e21 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e22 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e23 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e24 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e25 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	
	                        e1.insert(10, "S.no")
	                        enn2.insert(10, "Name")
	                        enn3.insert(10, "Age")
	                        enn4.insert(10, "Gender")
	                        e5.insert(10, "Id_Proof")
	                        e6.insert(10, "1")
	
	                        e11.insert(10, "2")
	                        e16.insert(10, "3")
	                        e21.insert(10, "4")
	
	                        e1.grid(row=0, column=0)
	                        enn2.grid(row=0, column=1)
	                        enn3.grid(row=0, column=2)
	                        enn4.grid(row=0, column=3)
	                        e5.grid(row=0, column=4)
	                        e6.grid(row=1, column=0)
	                        enn7.grid(row=1, column=1)
	                        enn8.grid(row=1, column=2)
	                        enn9.grid(row=1, column=3)
	                        e10.grid(row=1, column=4)
	
	                        e11.grid(row=2, column=0)
	                        e12.grid(row=2, column=1)
	                        e13.grid(row=2, column=2)
	                        e14.grid(row=2, column=3)
	                        e15.grid(row=2, column=4)
	
	                        e16.grid(row=3, column=0)
	                        e17.grid(row=3, column=1)
	                        e18.grid(row=3, column=2)
	                        e19.grid(row=3, column=3)
	                        e20.grid(row=3, column=4)
	
	                        e21.grid(row=4, column=0)
	                        e22.grid(row=4, column=1)
	                        e23.grid(row=4, column=2)
	                        e24.grid(row=4, column=3)
	                        e25.grid(row=4, column=4)
	
	                        def fun(*args):
	                            enn9.insert(10, v2.get())
	
	                        def fun1(*args):
	                            e14.insert(10, v3.get())
	
	                        def fun2(*args):
	                            e19.insert(10, v4.get())
	
	                        def fun3(*args):
	                            e24.insert(10, v5.get())
	
	                        def fun4(*args):
	                            e10.insert(10, v6.get())
	
	                        def fun5(*args):
	                            e15.insert(10, v7.get())
	
	                        def fun6(*args):
	                            e20.insert(10, v8.get())
	
	                        def fun7(*args):
	                            e25.insert(10, v9.get())
	
	                        v2 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v2.set('Choose')
	                        v2.trace("w", fun)
	                        popupMenu1 = OptionMenu(window2, v2, *gender)
	                        popupMenu1.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu1.grid(row=1, column=3)
	
	                        v3 = StringVar(window2)
	                        gender1 = {'Male', 'Female'}
	                        v3.set('Choose')
	                        v3.trace("w", fun1)
	                        popupMenu2 = OptionMenu(window2, v3, *gender1)
	                        popupMenu2.config(font=('Calisto MT', 9), bg="darkgoldenrod3", fg='white')
	                        popupMenu2.grid(row=2, column=3)
	
	                        v4 = StringVar(window2)
	                        gender2 = {'Male', 'Female'}
	                        v4.set('Choose')
	                        v4.trace("w", fun2)
	                        popupMenu3 = OptionMenu(window2, v4, *gender2)
	                        popupMenu3.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu3.grid(row=3, column=3)
	
	                        v5 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v5.set('Choose')
	                        v5.trace("w", fun3)
	                        popupMenu4 = OptionMenu(window2, v5, *gender)
	                        popupMenu4.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu4.grid(row=4, column=3)
	
	                        v6 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v6.set('Choose')
	                        v6.trace("w", fun4)
	                        popup = OptionMenu(window2, v6, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=1, column=4)
	
	                        v7 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v7.set('Choose')
	                        v7.trace("w", fun5)
	                        popup = OptionMenu(window2, v7, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=2, column=4)
	
	                        v8 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v8.set('Choose')
	                        v8.trace("w", fun6)
	                        popup = OptionMenu(window2, v8, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=3, column=4)
	
	                        v9 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v9.set('Choose')
	                        v9.trace("w", fun7)
	                        popup = OptionMenu(window2, v9, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=4, column=4)
	
	                def Check1():
	
	                    def Show():
	                        global x1
	                        window3 = Tk()
	                        window3.title("Ticket")
	                        screen_width = window3.winfo_screenwidth()
	                        screen_height = window3.winfo_screenheight()
	                        width = 780
	                        height = 480
	                        x = (screen_width / 2) - (width / 2)
	                        y = (screen_height / 2) - (height / 2)
	                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                        window3.config(bg='gray23')
	
	                        Label(window3, text="Name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=50)
	                        Label(window3, text="Gender:", bg='dark turquoise',font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=50)
	                        Label(window3, text="Departure time:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=90)
	                        Label(window3, text="Age:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=90)
	                        Label(window3, text="Class:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=130)
	                        Label(window3, text="Train no.:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=130)
	                        Label(window3, text="Train name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=170)
	                        Label(window3, text="Source:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=210)
	                        Label(window3, text="Destination:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=250)
	                        Label(window3, text="No. of tickets:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=290)
	
	                        Label(window3, text="PNR no.:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=170)
	
	                        Name = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
	                        Gender = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
	                        DepartureTime = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=210, y=90,
	                                                                                                       height=25)
	                        Age = Label(window3, justify="center",bg='white',font=('Slab Serif', 10)).place(x=380, y=90, height=25)
	                        Class = Label(window3, justify="center",bg='white',text=variable2.get(),font=('Slab Serif', 10)).place(x=380, y=130, height=25)
	                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
	                        TrainNumber.place(x=170, y=130, height=25)
	
	                        Source = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
	                        Destination = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=180, y=250,
	                                                                                                     height=25)
	                        Number = Label(window3,text=count, justify="center", bg='white',font=('Slab Serif', 9)).place(x=170, y=290, height=25)
	                        global conn, cursor, x1, x2
	
	                        if x1 == 12237:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12237")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12241:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12241")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12245:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12245")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2], justify="center",bg='white',
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1], justify="center",bg='white',
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	
	                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12249:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12249")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170,
	                                    height=25)
	
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1], justify="center",bg='white',
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3], justify="center",bg='white',
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	                                pnr1 = Label(window3, justify="center", text=data[0],bg='white',
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	
	
	                        Label(window3, text="Have a happy & safe Journey!!", bg='white',fg='orange red',font=('Comic Sans MS', 23,'bold')).place(x=200, y=340)
	
	                        mainloop()
	
	                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
	                            e15.get()) != 0) and (
	                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
	                        e25.get()) != 0) and (
	                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
	                            e10.get()) != 0) and (
	                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
	                        e20.get()) != 0) and (
	                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
	                        count=1
	                        Show()
	                    elif e12.get()!="" and e17.get()=="":
	                        count=2
	                        Show()
	                    elif e17.get()!="" and e22.get()=="":
	                        count=3
	                        Show()
	                    elif e22.get()!="":
	                        count=4
	                        Show()
	                    else:
	                        Show()
	
	                b = Button(window2, text='Proceed', bg="slategray3", font=('Britannic Bold', 16), command=Check1)
	                b.place(x=450, y=255)
	
	                mainloop()
	
	            PassengerDetails()
	
	        def PassengerDetails4():
	             global x1
	             if en29.get() == "12238":
	                x1 = 12238
	             elif en29.get() == "12242":
	                x1 = 12242
	             elif en29.get() == "12246":
	                x1 = 12246
	             else:
	                x1=12250
	
	             def PassengerDetails():
	                window1.destroy()
	                window2 = Tk()
	                window2.title("Passenger Details")
	                window2.config(bg="indianred2")
	                screen_width = window2.winfo_screenwidth()
	                screen_height = window2.winfo_screenheight()
	                width = 1020
	                height = 700
	                x = (screen_width / 2) - (width / 2)
	                y = (screen_height / 2) - (height / 2)
	                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                
	
	                height = 5
	                width = 5
	                for i in range(height):  # Rows
	                    for j in range(width):  # Columns
	                        e1 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn2 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn3 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        enn4 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e5 = Entry(window2, justify="center", font=('Britannic Bold', 13), bg="lightpink3",fg="blue4")
	                        e6 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn7 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn8 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        enn9 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e10 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e11 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e12 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e13 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e14 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e15 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e16 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e17 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e18 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e19 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e20 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e21 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e22 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e23 = Entry(window2, justify="center", font=('Rockwell Condensed', 11), bg="steelblue3")
	                        e24 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	                        e25 = Entry(window2, justify="center", font=('Rockwell Condensed', 5))
	
	                        e1.insert(10, "S.no")
	                        enn2.insert(10, "Name")
	                        enn3.insert(10, "Age")
	                        enn4.insert(10, "Gender")
	                        e5.insert(10, "Id_Proof")
	                        e6.insert(10, "1")
	
	                        e11.insert(10, "2")
	                        e16.insert(10, "3")
	                        e21.insert(10, "4")
	
	                        e1.grid(row=0, column=0)
	                        enn2.grid(row=0, column=1)
	                        enn3.grid(row=0, column=2)
	                        enn4.grid(row=0, column=3)
	                        e5.grid(row=0, column=4)
	                        e6.grid(row=1, column=0)
	                        enn7.grid(row=1, column=1)
	                        enn8.grid(row=1, column=2)
	                        enn9.grid(row=1, column=3)
	                        e10.grid(row=1, column=4)
	
	                        e11.grid(row=2, column=0)
	                        e12.grid(row=2, column=1)
	                        e13.grid(row=2, column=2)
	                        e14.grid(row=2, column=3)
	                        e15.grid(row=2, column=4)
	
	                        e16.grid(row=3, column=0)
	                        e17.grid(row=3, column=1)
	                        e18.grid(row=3, column=2)
	                        e19.grid(row=3, column=3)
	                        e20.grid(row=3, column=4)
	
	                        e21.grid(row=4, column=0)
	                        e22.grid(row=4, column=1)
	                        e23.grid(row=4, column=2)
	                        e24.grid(row=4, column=3)
	                        e25.grid(row=4, column=4)
	
	                        def fun(*args):
	                            enn9.insert(10, v2.get())
	
	                        def fun1(*args):
	                            e14.insert(10, v3.get())
	
	                        def fun2(*args):
	                            e19.insert(10, v4.get())
	
	                        def fun3(*args):
	                            e24.insert(10, v5.get())
	
	                        def fun4(*args):
	                            e10.insert(10, v6.get())
	
	                        def fun5(*args):
	                            e15.insert(10, v7.get())
	
	                        def fun6(*args):
	                            e20.insert(10, v8.get())
	
	                        def fun7(*args):
	                            e25.insert(10, v9.get())
	
	                        v2 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v2.set('Choose')
	                        v2.trace("w", fun)
	                        popupMenu1 = OptionMenu(window2, v2, *gender)
	                        popupMenu1.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu1.grid(row=1, column=3)
	
	                        v3 = StringVar(window2)
	                        gender1 = {'Male', 'Female'}
	                        v3.set('Choose')
	                        v3.trace("w", fun1)
	                        popupMenu2 = OptionMenu(window2, v3, *gender1)
	                        popupMenu2.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu2.grid(row=2, column=3)
	
	                        v4 = StringVar(window2)
	                        gender2 = {'Male', 'Female'}
	                        v4.set('Choose')
	                        v4.trace("w", fun2)
	                        popupMenu3 = OptionMenu(window2, v4, *gender2)
	                        popupMenu3.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu3.grid(row=3, column=3)
	
	                        v5 = StringVar(window2)
	                        gender = {'Male', 'Female'}
	                        v5.set('Choose')
	                        v5.trace("w", fun3)
	                        popupMenu4 = OptionMenu(window2, v5, *gender)
	                        popupMenu4.config(font=('Calisto MT', 10), bg="darkgoldenrod3", fg='white')
	                        popupMenu4.grid(row=4, column=3)
	
	                        v6 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v6.set('Choose')
	                        v6.trace("w", fun4)
	                        popup = OptionMenu(window2, v6, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=1, column=4)
	
	                        v7 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v7.set('Choose')
	                        v7.trace("w", fun5)
	                        popup = OptionMenu(window2, v7, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=2, column=4)
	
	                        v8 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v8.set('Choose')
	                        v8.trace("w", fun6)
	                        popup = OptionMenu(window2, v8, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=3, column=4)
	
	                        v9 = StringVar(window2)
	                        proof = {'Aadhar card', 'Pan card'}
	                        v9.set('Choose')
	                        v9.trace("w", fun7)
	                        popup = OptionMenu(window2, v9, *proof)
	                        popup.config(font=('Calisto MT', 10), bg="light green")
	                        popup.grid(row=4, column=4)
	
	                def Check1():
	
	                    def Show():
	                        global x1
	                        window3 = Toplevel(master)
	                        window3.title("Ticket")
	                        screen_width = window3.winfo_screenwidth()
	                        screen_height = window3.winfo_screenheight()
	                        width = 780
	                        height = 480
	                        x = (screen_width / 2) - (width / 2)
	                        y = (screen_height / 2) - (height / 2)
	                        window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
	                        window3.config(bg='gray23')
	                    
	
	                        Label(window3, text="Name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=50)
	                        Label(window3, text="Gender:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=50)
	                        Label(window3, text="Departure time:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=90)
	                        Label(window3, text="Age:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=90)
	                        Label(window3, text="Class:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=320, y=130)
	                        Label(window3, text="Train no.:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=130)
	                        Label(window3, text="Train name:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=170)
	                        Label(window3, text="Source:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=210)
	                        Label(window3, text="Destination:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=250)
	                        Label(window3, text="No. of tickets:",bg='dark turquoise', font=('Tempus Sans ITC', 11,'bold')).place(x=90, y=290)
	
	                        Label(window3, text="PNR no.:",bg='dark turquoise', font=('Tempus Sans ITC', 11)).place(x=320, y=170)
	
	                        Name = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
	                        Gender = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
	                        DepartureTime = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=210, y=90,
	                                                                                                       height=25)
	                        Age = Label(window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=90, height=25)
	                        Class = Label(window3, justify="center",bg='white',text=variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
	                        TrainNumber = Label(window3, justify="center",bg='white', font=('Slab Serif', 10))
	                        TrainNumber.place(x=170, y=130, height=25)
	
	                        Source = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
	                        Destination = Label(window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=180, y=250,
	                                                                                                     height=25)
	                        Number = Label(window3,text=count, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=290, height=25)
	                        global conn, cursor, x1, x2
	
	                        if x1 == 12238:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12238")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3], bg='white',justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12242:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12242")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	                                pnr1 = Label(window3,bg='white', justify="center", text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3], bg='white',justify="center", font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12246:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12246")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5], bg='white',justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170, height=25)
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	
	
	                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	                        elif x1 == 12250:
	                            cursor = conn.cursor()
	                            TrainNumber.config(text=x1)
	                            cursor.execute("Select * from Rail88 where Trainnumber=12250")
	                            fetch = cursor.fetchall()
	                            for data in fetch:
	                                Source = Label(window3, text=data[5], bg='white',justify="center", font=('Slab Serif', 10)).place(
	                                    x=170, y=170,
	                                    height=25)
	
	                                Destination = Label(window3, text=data[2],bg='white', justify="center",
	                                                    font=('Slab Serif', 10)).place(x=180, y=250, height=25)
	                                TrainName = Label(window3, text=data[1],bg='white', justify="center",
	                                                  font=('Slab Serif', 10)).place(x=180, y=210, height=25)
	                                DepartureTime = Label(window3, text=data[3],bg='white', justify="center",
	                                                      font=('Slab Serif', 10)).place(x=210, y=90, height=25)
	
	                            a = 111111
	                            b = 999999
	                            pnr = (random.randint(a, b))
	
	                            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
	                                           (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))
	
	                            conn.commit()
	
	                            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
	                            fetch1 = cursor.fetchall()
	                            for data in fetch1:
	                                pnr1 = Label(window3, justify="center",bg='white', text=data[0],
	                                             font=('Slab Serif', 9))
	                                pnr1.place(x=380, y=170, height=25)
	                                pnr1.config(text=data[0])
	                                Name = Label(window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=170, y=50, height=25)
	                                Age = Label(window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=90, height=25)
	                                Gender = Label(window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
	                                    x=380, y=50, height=25)
	
	                            cursor.close()
	                            conn.close()
	
	
	                        Label(window3, text="Have a happy & safe Journey!!", bg='white',fg='orange red',font=('Comic Sans MS', 23,'bold')).place(x=200, y=340)
	
	                        mainloop()
	
	                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
	                            e15.get()) != 0) and (
	                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
	                        e25.get()) != 0) and (
	                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
	                            e10.get()) != 0) and (
	                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
	                        e20.get()) != 0) and (
	                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
	                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
	                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
	                        count=1
	                        Show()
	                    elif e12.get()!="" and e17.get()=="":
	                        count=2
	                        Show()
	                    elif e17.get()!="" and e22.get()=="":
	                        count=3
	                        Show()
	                    elif e22.get()!="":
	                        count=4
	                        Show()
	                    else:
	                        Show()
	
	                b = Button(window2, text='Proceed', bg="slategray3", font=('Britannic Bold', 16), command=Check1)
	                b.place(x=450, y=255)
	
	                mainloop()
	
	             PassengerDetails()

	             
	        def Back1():
	            window1.destroy()
	
	        button1=Button(window1,text="Book Train 1",font=('Fixedsys',14),width=15,bg="chocolate1",command=PassengerDetails1)
	        button1.place(x=435,y=140)
	        button2 = Button(window1, text="Book Train 2",font=('Fixedsys',14),width=15, bg="chocolate1",command=PassengerDetails2)
	        button2.place(x=435,y=180)
	        button3 = Button(window1, text="Book Train 3",font=('Fixedsys',14),width=15, bg="chocolate1", command=PassengerDetails3)
	        button3.place(x=435,y=220)
	        button4 = Button(window1, text="Book Train 4",font=('Fixedsys',14),width=15,bg="chocolate1", command=PassengerDetails4)
	        button4.place(x=435,y=260)
	
	        button5 = Button(window1, text="Back",font=('Segoe UI Black',15),width=60, bg="spring green", fg="gray23", command=Back1)
	        button5.place(x=450,y=400,width=100)
	
	        mainloop()
	
	
	    def Cancellation():
	        root.destroy()
	        window4 = Toplevel(master)
	        window4.title("Ticket Cancellation")
	        window4.geometry('750x500+90+90')
	        window4.config(bg='red3')

	        cancel = Label(window4, text="Enter PNR No.", font=('System', 23), bg="chocolate2", fg="white").place(x=150, y=210)
	        e=Entry(window4,justify="center", font=('System', 20), bg="white", fg="chocolate2")
	        e.place(x=360, y=210)
	
	
	        def Delete1():
	            result = tkinter.messagebox.askquestion('Ask', 'Are you sure you want to Cancel your booked ticket?',
	                                              icon="warning")
	            if result == 'Yes':
	                cursor = conn.cursor()
	                cursor.execute("Select pnr from Rail999")
	                d = cursor.fetchall()
	
	                at=str(d)
	                d1=at.replace('(','')
	                d2 = d1.replace(')', '')
	                d3 = d2.replace(',', '')
	                d4=d3.replace('[','')
	                d5 = d4.replace(']', '')
	                d6=d5.split(' ')
	
	
	                q=0
	                for i in range(1,len(d6)):
	                    if e.get()==d6[i]:
	                        x123=e.get()
	                        q=1
	                if q==1:
	                    cursor.execute("Delete from Rail999 where pnr=?",(x123,))
	                    tkinter.messagebox.showinfo('Success', 'Ticket Cancelled Successfully')
	                    window4.destroy()
	                else:
	                    tkinter.messagebox.showinfo('Error', 'Unable to Find the Ticket')
	
	                cursor.close()
	                conn.close()
	
	
	        def Delete():
	            if (len(e.get())==""):
	                tkinter.messagebox.showinfo('Error', 'Enter required PNR No.')
	            else:
	
	                Delete1()
	        def Back():
	            window4.destroy()
	
	
	        Button(window4, text="Back", font=('Segoe UI Black', 18), bg="yellow4", fg="tomato4",command=Back).place(x=185,y=310,width=120)
	
	        Button(window4, text="Cancel", font=('Segoe UI Black', 18), bg="yellow4", fg="tomato4",command=Delete
	               ).place(x=440, y=310, width=120)
	        mainloop()
	    e1.config(font=('Segoe UI Black',18),bg="light sea green",fg="coral4")
	
	    e1.place(x=550,y=360,height=30,width=200)
	    Button(root,text="Available trains",font=('MS Serif',18), bg="plum4",fg="lawn green",command=Check).place(x=200,y=420,width=220)
	
	    Button(root, text="Train Cancellation",font=('MS Serif',18), bg="plum4",fg="lawn green",command=Cancellation).place(x=525,y=420,width=250)
	
	    mainloop()
	
	
	


#======Page 2======#

def __init__(self, masters):
        self.masters = masters
        self.frame = tk.Frame(self.master)

        self.frame.pack

def masters():
        masters= Toplevel(master)
        masters.geometry('1050x750')
        masters.title('Travel Agency 1')
        
        Label(masters,fg="firebrick4",bg="khaki2", text = "Welcome To ASRD Travel Agency", font=("impact",33)).place(x=220,y=100)
        Label(masters,fg="orange3",bg="darkblue", text = "Travel with Comfort...", font=("Comic Sans MS",28,"bold")).place(x=320,y=200)

        Button(masters,text="Railways", font=('Calibri',12),width=20,command=road).grid(row=3,sticky=N)
        
def tavelQuit():
    masters.destroy()

def login_function():
        with open("pass.txt","r") as o:
                with open("username.txt","r") as f:
                        data=f.read()
                        global masters
                        pasw=o.read()
                        passw=pasw.split()
                        if master.txt_user.get()=="" :
                                notif.config(fg="red", text="ERROR !!!  Please Fill The Details")
                        elif master.txt_pass.get()not in passw:
                                notif.config(fg="red", text="ERROR!!  Invalid Username/Password")
                                
                        else:
                                masters= Toplevel(master)
                                
                                masters.title('Travel Agency 1')
                                Label(masters,fg="white", text = "   ", font=('Calibri',12)).grid(row=0,sticky=N)
                                Label(masters,fg="firebrick4",bg="khaki2", text = "Welcome To ASRD Travel Agency", font=("impact",33)).place(x=220,y=100)
                                Label(masters,fg="white", text = "   ", font=('Calibri',12)).grid(row=0,sticky=N)
                                Label(masters,fg="orange3",bg="darkblue", text = "Travel with Comfort...", font=("Comic Sans MS",28,"bold")).place(x=320,y=200)

                                Button(masters,text="RAILWAYS",bg="gray55", font=("Fixedsys",18,"italic"),width=20,command=createWindow).place(x=366,y=300)
                                Button(masters,text="AIRWAYS",bg="gray55", font=("Fixedsys",18,"italic"),width=20,command=air).place(x=366,y=400)
                                Button(masters,text="QUIT",fg="gold",bg="red", font=('Calibri',12),width=20,command=tavelQuit).place(x=450,y=600)
                               
                                Label(masters,fg="white", text = "   ", font=('Calibri',12)).grid(row=6,sticky=N)



#======Login Frame======#
Frame_login=Frame(master, bg="white")
Frame_login.place(x=150,y=150,height=340,width=500)

title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
desc=title=Label(Frame_login,text="Enter Your Login Details",font=("Goudy old style",13,"bold"),fg="#d23d17",bg="white").place(x=90,y=100)


lbl_user=title=Label(Frame_login,text="USERNAME:-",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
master.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgreen")
master.txt_user.place(x=90,y=170,width=350,height=35)


lbl_pass=title=Label(Frame_login,text="PASSWORD:-",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=210)
master.txt_pass=Entry(Frame_login,show="*",font=("times new roman",15),bg="lightgreen")
master.txt_pass.place(x=90,y=240,width=350,height=35)

forget_btn=Button(Frame_login,text="Forgot Password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)

Login_btn=Button(master,text="Login",fg="white",bg="#d77337",font=("times new roman",21),command=login_function).place(x=300,y=470,width=180,height=40)


master.mainloop()
	
