def h1():
    c=0
    op=[]
    asc=[]
    asci=[]
    ps=input("Enter Password: ")
    ls=ps.split(ps[9])
    po=[int(i) for i in str(ls[0])]
    for x in po:
        m=x*x
        k=m%10
        op.append(k)
    stri=[str(lol) for lol in op]
    strin="".join(stri)
    h=int(strin)
    for j in ls[1]:
        asc.append(ord(j))
    for ki in asc:
        kio=ki-1
        asci.append(kio)
    kr="".join([chr(il) for il in asci])
    q=str(h)+ps[9]+kr
    print("calculating...")
    print("Decrypted password: ",q)
h1()