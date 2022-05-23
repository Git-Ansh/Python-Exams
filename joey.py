import mysql.connector as m
db = m.connect(host="localhost", user="root", passwd="Anshshah2003")
c = db.cursor(buffered=True)
c.execute("create database if not exists friends")
c.execute("use friends")
c.execute("Create table if not exists joey(s_no int primary key,skill varchar(30), name varchar(20),number int, hours_to_learn int)")
print("Table Created")
def insert_song():
    n = int(input("Enter number of people to be registered: "))
    for i in range(0, n):
        sn = input("Enter serial number: ")
        sd = input("Enter skill: ")
        sg = input("Enter name: ")
        insp = input("Enter number: ")
        lyr = input("Enter hours to learn: ")
        c.execute("insert into joey values('"+sn+"','"+sd+"','"+sg+"','"+insp+"','"+lyr+"')")
        print("Data inserted")
        db.commit()
def display():
    print("--------REGISTERED SONGS--------")
    c.execute("Select * from joey")
    k = 1
    for i in c:
        print("data", k, ":", i)
        k += 1
def search():
    try:
        lt=input("Enter a skill: ")
        c.execute("select * from joey where skill like '"'%' + lt + '%'"' ")
    k = 1
    for i in c:
        print("data", k, ":", i)
    k += 1
except:
    print("It's a moo point.")
def queries():
    print("people who know french")
    c.execute("select name from joey where skill like 'learning french'")
    k = 1
    for i in c:
        print("data", k, ":", i)
        k += 1
    print("people who know singing")
    c.execute("select name from joey where skill like 'singing'")
    k = 1
    for i in c:
        print("data", k, ":", i)
        k += 1
    print("Rachel's skills:")
    c.execute("select * from joey where name like 'rachel green'")
    k = 1
    for i in c:

        print("data", k, ":", i)
        k += 1
    print("Singing and dancing")
    c.execute("select name from joey where skill like 'singing'")
    print("Singing")
    k = 1
    for i in c:
        print("data", k, ":", i)
        k += 1
    c.execute("select name from joey where skill like 'dancing'")
    print("dancing")
    for i in c:
        print(i)
        k += 1
    c.execute("select sum(hours_to_learn) from joey where skill='singing' or skill='dancing' ")
    for i in c:
        print(i)
    print("Grouped by names")
    c.execute("select count(skill), sum(hours_to_learn),name from joey group by name")
    for i in c:
        print(i)
    c.execute("select max(hours_to_learn), min(hours_to_learn),skill from joey group by skill ")
    for i in c:
        print(i)
while True:
    cho=int(input("------MENU------- \npress 1 to register a person \npress 2 to display all data \npress 3 to search fora skill \npress 4 to run all specified queries \npress 5 to exit \nenter your choice: "))
    if cho==1:
        insert_song()
    elif cho==2:
        display()
    elif cho==3:
        search()
    elif cho==4:
        queries()
    elif cho==5:
        if db.is_connected():
            db.close()
            c.close()
            print("MySQL connection Terminated")
            break
        else:
            print("Please enter valid choice")