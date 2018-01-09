def drawstars(x):
    y=('*')
    for i in x:
        if type (i) == int:
            print i*y
        else:
            if type(i)== str:
                for val in i:
                    print val[0]*len(i)
                    break
drawstars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
