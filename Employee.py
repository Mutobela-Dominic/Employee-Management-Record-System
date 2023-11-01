#importing mysql.connector 
import mysql.connector
#make connection.
con = mysql.connector.connect(
    host="localhost",user="root",password="@mr.domi.",database="Employee")

    
    # function to add emlpoyee.
def Add_Employee():
    id = input("Enter employee id :")
    
    #check if the given id exixts.
    if(check_employee(id) == True):
        print("Employee already exists\nTry Again\n")
        menu()
        
    else:
        Name = input("Enter Employee Name :")
        Post = input("Enter Employee Post :")
        salary = input("Eter Employee salary :")
        data = (id, Name, Post, salary)
        
    #insert employee details into employees table.
    sql = 'insert into employees values(%s,%s,%s,%s)'
    c = con.cursor()
    #execute the query
    c.execute(sql,data)    
    #commit() to make changes in table.
    con.commit()
    print("Employee Added Successfully")
    menu()
       
    #function to promote employee.
def Promote_Employee():
        id = int(input("Enter Employee id"))
    #check if the id given exists.
        if(check_employee(id) ==False):
            print("Employee does not exists\nTry again\n")
            menu()
        else:
            Amount = int(input("Enter increase in salary"))
    #query to fetch salary of the id entered.
        sql = 'select salary from employees where id=%s'
        data = (id,)
        c.con.cursor()
    #execute the query.
        c.execute(sql, data)
    #fetch salary of the given id.
        r= c.fetchone()
        t = r[0]+Amount
    #query to update salary.
        sql = 'update employees set salary=%s where id=%s'
        d = (t, id)
    #execute the query.
        c.execute(sql,d)
    #commit() method to save changes.
        con.commit()
        print("Employee Promoted")
        menu()
    
    #function to remove employee.
def Remove_Employee()    :
    id = input("Enter Employee id :")
    #check if the id exist.
    if(check_employee(id)==False):
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
    #query to delete employee.
        sql = 'delete from employees where id=%s'
        data = (id,)
        c = con.cursor()
    #execute the query.
    c.execute(sql, data)
    #commit() to make changes in the table.
    con.commit()
    print("Employee Removed")
    menu()
    
    
def check_employee(Employee_id):
    #query to select arr rows of employees table
    sql = 'select * from employees where id=%s'
    #make cursor buffered to make raw method work correctly.
    c = con.cursor(buffered=True)
    data = (Employee_id,)
    #rowcount method to find number of raws with the given values.
    r = c.rowcount
     
    if r == 1:
        return True
    else:
        return False
 
    #function to display employees.
def Display_Employees():
    #query to select rows from employees.
    sql = 'select * from employees'
    c = con.cursor()
    #execute the query.
    c.execute(sql)
    #fetch all details of all employees.
    r = c.fetchall()
    print(f"This the value of r:{r} ")
    #print(f"length of r r:{len(r)} ")
    for i in r:
        print("Employee id :", i[0])
        print("Employee Name :",i[1])
        print("Employee Post :", i[2])
        print("Employee salary :",i[3])
        print("                                                                ")
    menu()
    #menu function.
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee" )
    print("2 to Remove Employee ")
    print("3 to Promote Employee ")
    print("4 to Display Employees ")
    print("5 to Exit")
        
    #Take choice from user.
    ch = int(input("Enter your Choice "))
    if ch ==1:
        Add_Employee()
    elif ch == 2:
        Remove_Employee()
    elif ch ==3:
        Promote_Employee()
    elif ch ==4:
        Display_Employees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()
    #calling the functions.    
menu()
check_employee(Employee_id)
Add_Employee()
Promote_Employee()
Display_Employees()
Remove_Employee()
