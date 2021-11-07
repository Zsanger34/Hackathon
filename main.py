from tkinter import *
import mysql.connector
from tkinter import messagebox
import sys
from PIL import ImageTk,Image
from tkinter import ttk
from Animal import Animal
from Customer import customer
from ZooKeeper import ZooKeeper
from Customer import moneyMade
import random

mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="zoo_mangment_system")
mycursor=mydb.cursor()
#Adds rows to the Mysql Table
def addRow(day,cOL,cOW,cP,sH,zH) :
    profit = cP -(cOL + cOW)
    sql = "Insert into Zoo Values (" + str(day) +"," + str(cOL) + "," + str(cOW) + "," + str(cP) +  "," + str(sH) + ","+ str(zH) + "," + str(profit) +";"
    mycursor.execute(sql)
    mydb.commit()
AnimalList =[]
ZooList = ["Alligators", "Hawks", "Crocodiles", "Giraffes","Bears" ,"Owl", "Snakes" , "Ocelot", "Lion",
 "Cougars", "Penguins", "Chimpanzees", "Gorilla","Peacock","Elephants"]
def ListOfLiving():
    sizeVal=int(random.random()*15+1)
    nutriVal=int(random.random()*3+1)
    for n in range(25):
        AnimalList.append(Animal(random.choice(ZooList), nutriVal, sizeVal))


weath=[.27,.96,.27,.96,.57,.96,.27,.27,.66,.96,.13,.96,.076,.96]
ListOfLiving()
#need to include total of all the money the customer payed
def CustomerList():
    listOfCust=[]
    Max=int(random.choice(weath)*1000)
    for n in range(1, Max):
        listOfCust.append(customer(n))
    return listOfCust



Habitat = ["Reptiles","Birds","Big Cats","Large Animals","Monkeys"]

def ListofWorkers():
    WorkerList ={}
    workVal=int(random.random()*5+1)
    for n in range(5):
        WorkerList[(ZooKeeper(16.5, n))]=Habitat[n]
    return WorkerList



def CusFav(lst):
    anml={}
    for n in range(len(lst)):
        anml[lst[n].favorite]=anml.get(lst[n].favorite,0)+1
    ret=''
    hold=0
    print(anml)
    for key in anml:
        if anml[key]>hold:
            hold=anml[key]
            ret=key
    return ret+" "+str(hold)



def COL():
    num=0
    for n in AnimalList:
        num = num + (n.nutrition *n.size)
    return num

def CP(cus):
    income=moneyMade(cus)
    return income


#for n in range(1)
#   lst=customerList()
#   CPS = CP(lst)
#   COLS = COL()
#   FavRow = CusFav(lst)
    ##addRow("Day" + str(n+2),cOL,16.5,cP,,zH)
#income=moneyMade(lst)
#print(income)



#---------------------------------------------------------------------------------------------------
#                                             GUI FUNCTIONS
#____________________________________________________________________________________________________
def show():
    Cost_of_Living_entry.delete(0, END)
    Salery_entry.delete(0, END)
    Income_entry.delete(0, END)
    Profit_entry.delete(0, END)
    BH_entry.delete(0, END)
    Zk_entry.delete(0,END)
    if timeperiod_Entry.get() == "Today":
        mysql = 'Select Cost_Of_Living from Zoo where Day_Number=(SELECT max(Day_Number) FROM Zoo);'
        mycursor.execute(mysql)
        for x in mycursor:
            Cost_of_Living_entry.insert(0, x)
        mysql = 'Select Zookeeper_Salery from Zoo where Day_Number=(SELECT max(Day_Number) FROM Zoo);'
        mycursor.execute(mysql)
        for x in mycursor:
            Salery_entry.insert(0, x)
        mysql = 'Select Customer_Income from Zoo where Day_Number=(SELECT max(Day_Number) FROM Zoo);'
        mycursor.execute(mysql)
        for x in mycursor:
            Income_entry.insert(0, x)
        mysql = 'Select Favorite_Animal from Zoo where Day_Number=(SELECT max(Day_Number) FROM Zoo);'
        mycursor.execute(mysql)
        for x in mycursor:
            BH_entry.insert(0, x)
        mysql = 'Select Zookeeper_of_Animal from Zoo where Day_Number=(SELECT max(Day_Number) FROM Zoo);'
        mycursor.execute(mysql)
        for x in mycursor:
            Zk_entry.insert(0, x)
        mysql = 'Select Profit from Zoo where Day_Number=(SELECT max(Day_Number) FROM Zoo);'
        mycursor.execute(mysql)
        for x in mycursor:
            Profit_entry.insert(0, x)
    elif timeperiod_Entry.get() == "Yesterday":
        mysql = 'Select Cost_Of_Living from Zoo order by Day_Number DESC LIMIT 1,1;'
        mycursor.execute(mysql)
        for x in mycursor:
            Cost_of_Living_entry.insert(0, x)
        mysql = 'Select Zookeeper_Salery from Zoo order by Day_Number DESC LIMIT 1,1;'
        mycursor.execute(mysql)
        for x in mycursor:
            Salery_entry.insert(0, x)
        mysql = 'Select Customer_Income from Zoo order by Day_Number DESC LIMIT 1,1;'
        mycursor.execute(mysql)
        for x in mycursor:
            Income_entry.insert(0, x)
        mysql = 'Select Favorite_Animal from Zoo order by Day_Number DESC LIMIT 1,1;'
        mycursor.execute(mysql)
        for x in mycursor:
            BH_entry.insert(0, x)
        mysql = 'Select Zookeeper_of_Animal from Zoo order by Day_Number DESC LIMIT 1,1;'
        mycursor.execute(mysql)
        for x in mycursor:
            Zk_entry.insert(0, x)
        mysql = 'Select Profit from Zoo order by Day_Number DESC LIMIT 1,1;'
        mycursor.execute(mysql)
        for x in mycursor:
            Profit_entry.insert(0, x)
    elif timeperiod_Entry.get() == "This Week":
        mysql = 'Select sum(Cost_Of_Living) from zoo ORDER BY Day_Number DESC LIMIT 7;'
        mycursor.execute(mysql)
        for x in mycursor:
            Cost_of_Living_entry.insert(0, x)
        mysql = 'Select sum(Zookeeper_Salery) from zoo ORDER BY Day_Number DESC LIMIT 7;'
        mycursor.execute(mysql)
        for x in mycursor:
            Salery_entry.insert(0, x)
        mysql = 'Select sum(Customer_Income) from zoo ORDER BY Day_Number DESC LIMIT 7;'
        mycursor.execute(mysql)
        for x in mycursor:
            Income_entry.insert(0, x)
        mysql = 'Select sum(Profit) from zoo ORDER BY Day_Number DESC LIMIT 7;'
        mycursor.execute(mysql)
        for x in mycursor:
            Profit_entry.insert(0, x)
        BH_entry.insert(0, "NA")
        Zk_entry.insert(0, "NA")
    elif timeperiod_Entry.get() == "This Month":
        mysql = 'Select sum(Cost_Of_Living) from zoo ORDER BY Day_Number DESC LIMIT 30;'
        mycursor.execute(mysql)
        for x in mycursor:
            Cost_of_Living_entry.insert(0, x)
        mysql = 'Select sum(Zookeeper_Salery) from zoo ORDER BY Day_Number DESC LIMIT 30;'
        mycursor.execute(mysql)
        for x in mycursor:
            Salery_entry.insert(0, x)
        mysql = 'Select sum(Customer_Income) from zoo ORDER BY Day_Number DESC LIMIT 30;'
        mycursor.execute(mysql)
        for x in mycursor:
            Income_entry.insert(0, x)
        mysql = 'Select sum(Profit) from zoo ORDER BY Day_Number DESC LIMIT 30;'
        mycursor.execute(mysql)
        for x in mycursor:
            Profit_entry.insert(0, x)
        BH_entry.insert(0, "NA")
        Zk_entry.insert(0, "NA")
    elif timeperiod_Entry.get() == "This Year":
        mysql = 'Select sum(Cost_Of_Living) from zoo ORDER BY Day_Number DESC LIMIT 365;'
        mycursor.execute(mysql)
        for x in mycursor:
            Cost_of_Living_entry.insert(0, x)
        mysql = 'Select sum(Zookeeper_Salery) from zoo ORDER BY Day_Number DESC LIMIT 365;'
        mycursor.execute(mysql)
        for x in mycursor:
            Salery_entry.insert(0, x)
        mysql = 'Select sum(Customer_Income) from zoo ORDER BY Day_Number DESC LIMIT 365;'
        mycursor.execute(mysql)
        for x in mycursor:
            Income_entry.insert(0, x)
        mysql = 'Select sum(Profit) from zoo ORDER BY Day_Number DESC LIMIT 365;'
        mycursor.execute(mysql)
        for x in mycursor:
            Profit_entry.insert(0, x)
        BH_entry.insert(0, "NA")
        Zk_entry.insert(0, "NA")

#------------------------------------------------------------------------------------------------------------------------------------
#                                              GUI
#________________________________________________________________________________________________________________________

mainpage = Tk()
mainpage.geometry("1800x1800")
mainpage.title("Main Page")
mainpage.configure(bg='white')

OutputFrame = Frame(mainpage, bg="blue")
OutputFrame.place(relx=0.05, rely=0, relheight=1 , relwidth=0.9)
timeperiod_Label = Label(OutputFrame, text ="Time Period")
timeperiod_Label.place(relx=0.05, rely=0.05, relheight=0.05 , relwidth=0.3)
timeperiod_Entry=ttk.Combobox(OutputFrame, values =["Today",
                                                    "Yesterday",
                                                    "This Week",
                                                    "This Month",
                                                    "This Year"])
timeperiod_Entry.place(relx=0.375, rely=0.05, relheight=0.05 , relwidth=0.35)
timeperiod_button=Button(OutputFrame ,text="Search" , command=show)
timeperiod_button.place(relx=0.75, rely=0.05, relheight=0.05 , relwidth=0.2)

Cost_of_Living_Label = Label(OutputFrame, text ="Cost of Living")
Cost_of_Living_Label.place(relx=0.05, rely=0.15, relheight=0.05 , relwidth=0.3)
Cost_of_Living_entry=Entry(OutputFrame)
Cost_of_Living_entry.place(relx=0.4, rely=0.15, relheight=0.05 , relwidth=0.55)

Salery_Label = Label(OutputFrame, text ="Salery of Workers")
Salery_Label.place(relx=0.05, rely=0.25, relheight=0.05 , relwidth=0.3)
Salery_entry=Entry(OutputFrame)
Salery_entry.place(relx=0.4, rely=0.25, relheight=0.05 , relwidth=0.55)

Income_Label = Label(OutputFrame, text ="Income from Customer")
Income_Label.place(relx=0.05, rely=0.35, relheight=0.05 , relwidth=0.3)
Income_entry=Entry(OutputFrame)
Income_entry.place(relx=0.4, rely=0.35, relheight=0.05 , relwidth=0.55)

Profit_Label = Label(OutputFrame, text ="Net Income")
Profit_Label.place(relx=0.05, rely=0.45, relheight=0.05 , relwidth=0.3)
Profit_entry=Entry(OutputFrame)
Profit_entry.place(relx=0.4, rely=0.45, relheight=0.05 , relwidth=0.55)

BH_Label = Label(OutputFrame, text ="Best Habitat")
BH_Label.place(relx=0.05, rely=0.55, relheight=0.05 , relwidth=0.3)
BH_entry=Entry(OutputFrame)
BH_entry.place(relx=0.4, rely=0.55, relheight=0.05 , relwidth=0.55)

Zk_Label = Label(OutputFrame, text ="Zookeeper of that Habitat")
Zk_Label.place(relx=0.05, rely=0.65, relheight=0.05 , relwidth=0.3)
Zk_entry=Entry(OutputFrame)
Zk_entry.place(relx=0.4, rely=0.65, relheight=0.05 , relwidth=0.55)

mainpage.mainloop()



