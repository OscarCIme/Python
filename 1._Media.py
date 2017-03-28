List = [1, 12, 1, 15, 10, 3]
def Promedio(plist):
    if len(plist)>0:
        return reduce(lambda x,y:x+y,plist)/len(plist)
    return 0
 
print 'Promedio:',Promedio(List)
