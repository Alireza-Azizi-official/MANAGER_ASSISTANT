import mysql.connector
import time

# connect to the database
con=mysql.connector.connect(host='localhost', 
						database='company_project', 
						user='root', 
						password='Alirezaz48861378!') 
 
 
# check if the entered id is in the data base or not
def check_employee(employee_id):
    sql= 'select * from employee_record where id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id , )
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else: 
        return False

# add employee if the id already exists raise an error otherwise add
def add_employee():
    id = input("enter employee id:")
    if (check_employee(id) == True):
        print("employee already exists \n enter another id.")
        time.sleep(2)
        print("_____________________________________")
        menu()
        
    else:
        name = input("enter the employee name:")
        post = input("enter the employee post:")
        salary = input("enter the employee salary:")
        data = (id, name, post, salary)
        sql = 'insert into employee_record (id, name, post, salary) values (%s, %s, %s, %s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("<< THE EMPLOYEE ADDED SUCCESSFULLY >>")
        time.sleep(2)
        print("_____________________________________")
        menu()
        
# remove employee if the id doesn't exist raise an error otherwise remove
def remove_employee():
    id = input("enter the employee id:")
    
    if (check_employee(id)==False):
        print("the one you want remove is not even in the list.\n enter another id.")
        print("_____________________________________")
        time.sleep(2)
        menu()
        
    else:
        sql = 'delete from employee_record where id = %s'
        data = (id,)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("<< THE EMPLOYEE REMOVED SUCCESSFULY >>")
        time.sleep(2)
        print("______________________________________")
        menu()
       
# check if the entered id exists if not raise an error otherwise count the salary and increase it 
def promot_employee():
    id = input('enter the employee id:')
    
    if (check_employee(id)==False):
        print("there is no such employee with this id. try another one.")
        time.sleep(2)
        print("_____________________________________")
        menu() 
        
    else:
        amount = int(input("how much do you want to add to the salary:"))
        
        sql='select salary from employee_record where id=%s'
        data = (id, )
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        t = int(r[0]) + amount
        sql = "update employee_record set salary=%s where id=%s"
        d = (t, id)
        c.execute(sql, d)
        con.commit()
        print("<< EMPLOYEE PROMOTEED SUCCESSFULY >>")
        time.sleep(2)
        print("______________________________________")
        menu()


# check if the entered id exists if not raise an error otherwise count the salary and decrease it
def demotion_employee():
    id = input('enter the employee id:')
    
    if (check_employee(id)==False):
        print("there is no such employee with this id. try another one.")
        time.sleep(2)
        print("_____________________________________")
        menu() 
        
    else:
        amount = int(input("how much do you want to decrease the salary:"))
        
        sql='select salary from employee_record where id=%s'
        data = (id, )
        c = con.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        t = int(r[0]) - amount
        sql = "update employee_record set salary=%s where id=%s"
        d = (t, id)
        c.execute(sql, d)
        con.commit()
        print("<< SALARAY DECREASED SUCCESSFULY >>")
        time.sleep(2)
        print("______________________________________")
        menu()
        

# show all the details about each employee in the database
def display_employee():
    sql = 'select * from employee_record'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print("ENPLOYEE ID :", i[0])
        print("ENPLOYEE NAME :", i[1])
        print("ENPLOYEE POST :", i[2])
        print("ENPLOYEE SALARY :", i[3])
        print("______________________________________")
    time.sleep(2)
    print("______________________________________")
    menu()

# show the menu to the user to choose what to do based on numbers and call the chosen function  
def menu():
    print("** HELLO DEAR BOSS. I AM YOUR ASSISTANT AND I'M HERE TO HELP YOU.")
    print("PRESS:")
    print("1 to ADD employee.")
    print("2 to REMOVE employee.")
    print("3 to PROMOTE employee.")
    print("4 to DEMOTION employee. ")
    print("5 to DISPLAY employee.")
    print("6 to EXIT")
    
    ch = int(input("what do you want to do:"))
    print("_______________________________________")
    
    if ch == 1:
        add_employee()
    elif ch == 2:
        remove_employee()
    elif ch == 3:
        promot_employee()
    elif ch==4:
        demotion_employee()
    elif ch == 5:
        display_employee()
    elif ch == 6:
        print("TAKE CARE.")
        exit(0)
    else:
        print("!! INVALID NUMBER ENTERED !!")
        time.sleep(2)
        print("______________________________________")
        menu()       
menu()
