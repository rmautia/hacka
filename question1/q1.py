def rmdupandsort(mylist):
    cleanlist = set(mylist)
    newlist = list(cleanlist)
    newlist.reverse()
    return newlist


mylist = [11,6,11,7,8,9,6,2,7,1,3]
print(rmdupandsort(mylist))