a = 100
b = 20
c = 30

if a>=b:
    if b>=c:
        print(int(a),"<",int(b),"<",int(c))
    else:
        print(int(a),"<",int(c),"<",int(b))
else:
    print("'a' is not the biggest value.")