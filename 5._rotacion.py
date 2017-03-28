def rotar():
    a = [1, 5, 2, 4, 3]
    b = [1, 5, 2, 4, 3]
    c = [1, 5, 2, 4, 3]
    a.reverse()
    b.sort()
    c.sort(reverse=True)
    print (a)
    print (b)
    print (c) 
rotar()
