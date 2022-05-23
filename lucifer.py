import mysql.connector as m
db = m.connect(host="localhost", user="root", passwd="Anshshah2003")
c = db.cursor(buffered=True)
if db.is_connected():
    print("Connection Established")
    c.execute("Create database if not exists Yourname_TodaysDate")
    c.execute("Use Yourname_TodaysDate")
    c.execute("Create table if not exists User_Sentiment(user_id int primary key,user_name varchar(20),rating int,hoursspent int,showname varchar(20),Genreofshow varchar(20),Seasons int)")
    print("Table Created")
    print()
    k = int(input("Enter number of records to be registered : "))
    print()
    try:
        for i in range(0, k):
            uid = input("Enter user_id(use numbers only) : ")
            uname = input("Enter user Name(use characters only) : ")
            rate = input("Enter Rating(out of 5)(use numbers only) : ")
            hrs = input("Enter Hours client spent watching(use numbers only) : ")
            nameshow = input("Enter Name of the show(use characters only) : ")
            genreshow = input("Enter Genre of the show(use characters only) : ")
            seasons = input("Enter Seasons(use numbers only) : ")
            q1 = "Insert into User_Sentiment values('" + uid + "','" + uname + "','" + rate + "','" + hrs + "','" + nameshow+ "','" + genreshow + "','" + seasons + "')"
            c.execute(q1)
            db.commit()
            print("Data insertion Successful")
        c.execute("select * from User_Sentiment")
        n = 1
        for i in c:
            print("Data", n, ":", i)
            n += 1
        print("USERID AND NAMES OF USERS WHO HAVE WATCHED LUCIFER:")
        c.execute("select user_id, user_name from user_sentiment where showname like '%Lucifer%'")
        k = 1
        for j in c:
            print("Data", k, ":", j)
            k += 1
        print("NAME AND HOURS SPENT WATCHING FOR SHOWS WITH MORE THAN 4 SEASONS:")
         c.execute("select showname, hoursspent from user_sentiment where seasons>4")
        p = 1
        for u in c:
            print("Data", p, ":", u)
            p += 1
    except:

        print("Error! Please check your entries")

    finally:
        if db.is_connected():
            db.close()
            c.close()
            print("MySQL connection is closed")

else:
    print("Sorry Connection Failed")