#Project on STUDENT DATA management system

#first create connection 

import mysql.connector as mysql
conn=mysql.connect(user='root',password='',host='localhost')
cursor=conn.cursor()

#selecting database 
cursor.execute('use project')
print('done')


#insert new data into database (table)
def add():
    a=input("Enter your Fullname:")
    b=input("Enter your Address:")
    c=input("Enter your course name:")
    d=int(input("Enter your marks:"))
    q1="insert into studentdata(name,address,course,marks) values('"+a+"','"+b+"','"+c+"','"+str(d)+"')"
    cursor.execute(q1)
    conn.commit()
    print("Successfully saved")
    main()


#To retrive data from database
def Showdata():
    q2="Select*from studentdata"
    cursor.execute(q2)
    res=cursor.fetchall()
    for i in res:
        print(i)
    main()


#To udate the existing data in databse
def updatedata():
    x=int(input("Enter RollNo to update marks:"))
    y=int(input("Update marks:"))
    q3="update studentdata set marks='"+str(y)+"' where id='"+str(x)+"'"
    cursor.execute(q3)
    conn.commit()
    print("Update sucessfully")
    main()


#To delete records from database
def del_data():
    rollno=int(input("Enter students rollno you want to delete:"))
    q4="delete from studentdata where id='"+str(rollno)+"'"
    cursor.execute(q4)
    conn.commit()
    print("Deleted sucessfully") 
    main() 


#To search records from database
def search_data():
    rollno=int(input("Enter students rollno you want to search:"))
    q5="select*from studentdata where id='"+str(rollno)+"'"
    cursor.execute(q5)
    res=cursor.fetchall()
    print(res)
    main()


#To get the records of students who score maximum marks
def topper():
    q6="select*from studentdata order by marks desc limit 2"
    cursor.execute(q6)
    res=cursor.fetchall()
    for i in res:
        print(i) 
    main()


#To get the records of students who score less marks marks
def Average():
    q7="select*from studentdata order by marks limit 3"
    cursor.execute(q7)
    res=cursor.fetchall()
    for i in res:
        print(i)
    main()



def main():
    choice=int(input("enter your choice:\n1:add\n2:Showdata\n3:updatedata\n4:del_data\n5:search_data\n6:topper\n7:Average\n"))
    if choice==1:
        add()
    elif choice==2:
        Showdata()
    elif choice==3:
        updatedata()
    elif choice==4:
        del_data()
    elif choice==5:
        search_data()
    elif choice==6:
        topper()
    elif choice==7:
        Average()
    else:
        exit


main()