import sqlite3
book=sqlite3.connect("book.db")
curbook=book.cursor()
cs=0
def book():
    nm=input("Name of Book :")

    sql="SELECT * from book WHERE Title='"+nm+"';"
    curbook.execute(sql)

    record=curbook.fetchall()
    for i in record:
        print(i)

    cp=int(input("No. of Copies :"))

    sql="Select Price from book WHERE Title='"+nm+"';"
    curbook.execute(sql)
    record=curbook.fetchall()
    for i in record:
        for j in i:
          price=j*cp
    global cs
    cs+=price
    ch=input("Add more books ? Y/N :")

    if(ch=="Y" or ch=="y"):
        book()
    elif(ch=="N" or ch=="n"):
        print("Total cost=",cs)
    else:
        print("Enter right choice")
        
book()

