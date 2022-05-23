import sys
def movie():
    while True:
        print("******Welcome to five star movie theatre******")
        print("1. Get all movies")
        print("2. Get details about a particular movie")
        print("3. Exit")
        ch=int(input("Enter Your Choice: "))
        movRat=[9.2,9.1,9.0,9.0,8.9,8.9,8.9,8.9,8.7,8.7,8.8]
        movPrice=[10.5,9.4,13.6,14.0,6.5,7.0,9.3,10.0,11.9,8.4]
        movName=['The Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'The Dark Knight','12 Angry Men','Schindlers List','The Lord of the Rings: The Return of the King','Inception','The matrix','Pulp Fiction']
        n=len(movRat)
        if ch==1:
            try:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSr., Movie Name , Rating, Price")
                for i in range(0,n):
                    print(i,movName[i],",",movRat[i],",",movPrice[i])
            except:
                continue
        elif ch==2:
            while True:
                print("1. search by name")
                print("2. search by rating")
                print("3. main menu")
                ch1=int(input("Enter Choice: "))
                if ch1==1:
                    ent=input('Enter Movie Name: ')
                    for i in movName:
                        try:
                            if ent==i:
                                p = movName.index(i)
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMovie Name , Rating, Price")

                                print(movName[p],',',movRat[p],",",movPrice[p])
                                continue
                            else:
                                print("this movies does not exist")
                                continue
                        except:
                            print("this movies does not exist")
                            continue
                elif ch1==2:
                    try:
                        ent=float(input('Enter Rating: '))
                        for i in movRat:
                            if ent==i:
                                p = movRat.index(i)
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMovie Name , Rating, Price")

                                print(movName[p],',',movRat[p],",",movPrice[p])

                                continue
                    except:
                        print("this movies does not exist")
                        continue
                elif ch1==3:
                    movie()
                else:
                    print("enter valid input")
                    continue
        elif ch==3:
            sys.exit()
        else:
            print("enter valid input")
            continue
movie()