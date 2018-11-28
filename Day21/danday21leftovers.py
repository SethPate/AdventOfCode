#dan21 leftovers

#def r180(a):
    #a = a.replace('/','')
    #matchlist = []
    #charlength = len(a)
    #boxsize = int(math.sqrt(charlength))
    #match 3 - rotate 180
    #match = ''
    #reducer = charlength
    #while reducer >= 0:
        #print reducer
        #print boxsize
        #match = match + str(a[reducer - boxsize:reducer][::-1])
        #reducer -= boxsize
    #return match

#def r270(a):
    #match 4 - rotate 270
    #a = a.replace('/','')
    #match = ''
    #charlength = len(a)
    #boxsize = int(math.sqrt(charlength))
    #decreaser = boxsize - 1
    #while decreaser >= 0:
        #for i in range(0,charlength):
            #if i % boxsize == decreaser:
                #match = match + a[i]
        #decreaser -= 1
    #return match
