def power(num):
    i=1
    c=0
    k=1
    while i<=num:
        k=2**i
        if k==num:
            c=c+1
            print("true")
        i=i+1
    if c==0:
        print("false")
n=int(input("enter a any number"))
power(n)