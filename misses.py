from math import log, exp, ceil, floor

# find almost right answers\
def upper_limit_for_k(k):
    if (k > 10) or (k <= 70):
        print("That's a good value is below the upper limit of k")
        return True
    else:
        print("The value you entered is greater than 70 which is the upper limit")
        print("Try again another value of k")

def search(n, k):
    m = n
    j = k

    return m, j
    return upper_limit_for_k(k)

#print(search(2, 3))
def analyzer(x,y):
    n = int(input("Enter the value of n : "))
    k = int(input("Enterthe value of k : "))
    n, k = search(n,k)
    print(x, y)

    return x, y, n

#analyzer(10, 12)
def finder(x, y):
    x, y, n = analyzer(x, y)

    x = x ** n
    y = y ** n
    z = x + y
    z = exp(log(x)/n)
    z = ceil(z)
    #check whether z^n < x ^n + y^n or less , calculate the distance between

    diff1 = (x + y) - z**n
    diff2 = (z+1)**n - (x + y)
    if (diff1 > diff2):
        print("Z^n is less than (x^n + y^n) by : ", diff1)
        print("The value of Z is : ", z)
    else:
        print("(z+1)^n is greater than (x^n + y^n) by : ", diff2)
        print("The value of Z is : ", z+ 1)

   #parent(x, y)
def almost_right(x, y):
    print("almost right")
    return finder(x, y)

def parent(x, y):
    print("you have done  all")
    return almost_right(x, y)

def value_of_z():
    for z in range(20):
        return z
    return z+1
value_of_z()
#finder(12, 10)
parent(10, 12)