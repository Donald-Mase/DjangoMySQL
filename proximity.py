import mysql.connector
# graph visualization using matplotlib library
import matplotlib.pyplot as plt
import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pandas as pd
from sqlalchemy import create_engine, types
place =[]
proximity =[]


def graph_data(place,proximity):
    con = pymysql.connect(host='localhost', user='root', password='Kipruto14.', database='userdata')
    mycursor = con.cursor()
    query = 'select place, proximity from data2'
    mycursor.execute(query)
    df = pd.read_sql(query,con)
    place = df['place']
    proximity =df['proximity']
    # plotting the points
    plt.bar(place, proximity)
    # naming the x-axis
    plt.xlabel('Place')
    # naming the y-axis
    plt.ylabel('Proximity')
    # plt.plot()
    plt.show()
def connect_database():
    if placeEntry.get()=='' or proximityEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con = pymysql.connect(host= 'localhost', user='root', password='Kipruto14.')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data2(place varchar(100), proximity int(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from data2 where place=%s' #prevent double entry
        mycursor.execute(query,(placeEntry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'place ALready Exists')
        else:
            query = 'insert into data2(place, proximity) values(%s, %s)'
            mycursor.execute(query,(placeEntry.get(),proximityEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Successful update','Registration Success')
            prox.destroy()


prox = Tk()
prox.geometry('2000x2000')
prox.title('Proximity and Place Entry')
prox.resizable(True, True)
bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(prox, image=bgImage)
bgLabel.place(x=0, y=0)

frame = Frame(prox, bg= 'white')
frame.place(x=554, y=100)

heading = Label(frame, text='Distance', font=('Microsoft Yahei UI Light',18,'bold'),bg= 'white', fg='firebrick1')
heading.grid(row =0, column=0, padx=10, pady=10)


placeLabel = Label(frame, text='place', font=('Microsoft Yahei UI Light',18,'bold'),bg= 'white', fg='firebrick1')
placeLabel.grid(row =3, column=0, sticky='w', padx=10, pady=10)
placeEntry = Entry(frame, width= 30,font=('Microsoft Yahei UI Light',18,'bold'),bg= 'white', fg='firebrick1')
placeEntry.grid(row=4, column=0, sticky='w', padx= 25)

proximityLabel = Label(frame, text='proximity', font=('Microsoft Yahei UI Light',18,'bold'),bg= 'white', fg='firebrick1')
proximityLabel.grid(row =5, column=0, sticky='w', padx=10, pady=10)
proximityEntry = Entry(frame, width= 30,font=('Microsoft Yahei UI Light',18,'bold'),bg= 'white', fg='firebrick1')
proximityEntry.grid(row=6, column=0, sticky='w', padx= 25)

submitButton = Button(frame, text='submit', font=('Open Sans',16,'bold'),bd=0,bg= 'firebrick1', fg='white',width=17, command =connect_database)
submitButton.grid(row=10, column=0, pady=10)



graph_data(place, proximity)