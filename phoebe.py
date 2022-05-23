import mysql.connector as m
db = m.connect(host="localhost", user="root", passwd="Anshshah2003")
c = db.cursor(buffered=True)
c.execute("create database if not exists friends")
c.execute("use friends")
c.execute("Create table if not exists phoebe(song_name varchar(30) primary key,Duration_mins int, Genre varchar(20),Inspiration varchar(50), lyrics_Threelines varchar(100))")
print("Table Created")
def insert_song():
    n = int(input("Enter number of songs to be registered: "))
    for i in range(0, n):
        sn = input("Enter song name: ")
        sd = input("Enter Duration(mins): ")
        sg = input("Enter Genre of the song: ")
        insp = input("Enter inspiration for the song: ")
        lyr = input("Enter first three lines of the lyrics: ")
        c.execute("insert into phoebe values('"+sn+"','"+sd+"','"+sg+"','"+insp+"','"+lyr+"')")
        print("Data inserted")
        db.commit()
def display():
    print("--------REGISTERED SONGS--------")
    c.execute("Select * from phoebe")
    k = 1
    for i in c:
        print("song", k, ":", i)
        k += 1
while True:
    cho=int(input("------MENU------- \npress 1 to register a song \npress 2 to display all songs \npress 3 to exit \nenteryour choice: "))
    if cho==1:
        insert_song()
    elif cho==2:
        display()
    elif cho==3:
        if db.is_connected():
        db.close()
        c.close()
        print("MySQL connection Terminated")
        break
    else:
        print("Please enter valid choice")