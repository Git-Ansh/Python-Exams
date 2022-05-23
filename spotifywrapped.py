import datetime
class spotify():
    def __init__(self):
        self.totaltime=0
        self.mostfrequent=""
        self.favouriteartist=""
        self.favgenre=""
        self.mostplayed=0
    def get(self):
        l=0
        f = open('srk.supremacy@gmail.txt', "r+")
        p = [tuple(map(str, i.split(','))) for i in f]
        po=[x[2] for x in p]
        di=[x[3] for x in p]
        dy=[x[4] for x in p]
        for i in po:
            l+=int(i)
        self.totaltime=l
        nums = [int(u) for u in po]
        du=(nums.index(max(nums)))
        self.mostfrequent=p[du][0]
        self.mostplayed=max(nums)
        self.favouriteartist=max(set(di), key=di.count)
        self.favgenre=max(set(dy), key=dy.count)
    def display(self):
        print("------Welcome to your wrapped-------")
        now=datetime.datetime.now()
        ct=now.hour
        if ct<12:
            print("Good Morning,")
        elif ct>12:
            print("Good Afternoon,")
        elif ct>14:
            print("Good Evening,")
            print("This Year you listened to music for",self.totaltime,"minutes \nThere is a particular song that is very closeto your heart \nYou have listened to this song",self.mostplayed,"times! \n...And the song is ...drumroll please... \n",self.mostfrequent,"\nYour Favourite aritst was",self.favouriteartist,"\nAnd finally your favourite Genre was",self.favgenre)
s=spotify()
s.get()
s.display()