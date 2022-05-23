import mysql.connector as m
db = m.connect(host="localhost", user="root", passwd="Anshshah2003")
c = db.cursor(buffered=True)
c.execute("create database if not exists RTO_Ahmedabad")
c.execute("use RTO_Ahmedabad")
c.execute("create table if not exists Users(UserID int primary key,UserName varchar(30), VehicleNumber varchar(20), address varchar(100), age int)")
print("Table one created")
c.execute("create table if not exists Two_wheelers(VehicleNumber varchar(20) primary key, foreign key(VehicleNumber) references users(VehicleNumber), VehicleModel varchar(30),Company varchar(20), YearOfManufacture int)")
print("Table 2 created")
def user():
    try:
        for i in range(1,6):
        uid = input("Enter userid Code : ")
        unm = input("Enter username name : ")
        vn = input("Enter vehicle number : ")
        add = input("Enter address : ")
        age = input("Enter age: ")
        q = "Insert into Users values('" + uid + "','" + unm + "','" + vn + "','" + add + "','" + age + "')"
        c.execute(q)
        print("Data inserted successfully")
        db.commit()
    except:
        print("Error")
def whlr():
    try:
        for i in range(1,6):
        vn = input("Enter vehicle number : ")
        vm = input("Enter vehicle model : ")
        cp = input("Enter company : ")
        add = input("Enter Year of manufacture : ")
        q = "Insert into Two_wheelers values('" + vn + "','" + vm + "','" + cp + "','" + add + "')"
        c.execute(q)
        print("Data inserted successfully")
        db.commit()
    except:
        print("Error")
def queries():
    print("1")
    c.execute("select users.UserName from users, two_wheelers where two_wheelers.Company='Yamaha'")
    for i in c:
        print(i)
    print("2")
    c.execute("select users.UserName, two_wheelers.VehicleNumber from users, two_wheelers where two_wheelers.YearOfManufacture=2020")
    for i in c:
        print(i)
    print("3")
    try:
        c.execute("select UserName from users where age=23")
        for i in c:
            print(i)
    except:
        print("no users found")
        print("4")
        c.execute("select users.UserName, two_wheelers.VehicleNumber from users, two_wheelers where two_wheelers.YearOfManufacture=2020")
        for i in c:
            print(i)
        print("5")
        c.execute("alter table users add NoOfMembers int")
        for i in c:
            print(i)
        print("6")
        c.execute("update users set UserName = user where VehicleNumber = GJ01DF7322")
        print("7")
        c.execute("select * from users where VehicleNumber = 'GJ05%'")
        for i in c:
            print(i)
        print("8")
        c.execute("update users set VehicleNumber = 'GJ01EJ1193' where UserID = 4")
        for i in c:
            print(i)
        print("9")
        c.execute("select * from users order by Age ASC")
        for i in c:
            print(i)
        print("10")
        c.execute("delete from two_wheelers where YearOfManufacture>1960")
queries()