f = open("spiderman.txt", "a+")

def q1():
    l = f.readlines()
    num=0

    print("Case no., client name, phone no, product id, quantity, price per element.\n")
    for i in range(0, len(l)):
        num = int(l[i].split(',')[0])
    for v in range(2, int(num / 2) + 1):
        if (num % v) == 0:
            break
        else:
            print(l[i])
def q2():
    li = ['2', 'S', '3', 'E', '1', 'S', '2', 'E', '1', 'S', '1', 'E']
    b = 0
    for index, element in enumerate(li):
        if index % 2 == 0:
            x = int(element)
        for c in range(0, x):
            if index % 2 != 0:
                if element == 'S':
                    print("|")
        for c in range(0, b):
            print(" ", end="")
        for c in range(0, x):
            if element == 'E':
                print("-", end="")

                b += 1

q1()
q2()