size=9

matriz=[]
for i in range(size):
    matriz.append([])
    for j in range(size):
        matriz[i].append('*')

for i in range(size*2):
    for j in range(size):
        if i%2==0:
            if i==0:
                if j==0:
                    print u'\u250C'+u'\u2500'+u'\u252C',

                elif j==(size-1):
                    print u'\u2500'+u'\u2510',

                else:
                    print u'\u2500'+u'\u252C'+u'\u2500',

            elif i==(size-1):
                if j==0:
                    print u'\u2514'+u'\u2500'+u'\u2534',

                elif j==(size-1):
                    print u'\u2500'+u'\u2518',

                else:
                    print u'\u2500'+u'\u2534',

            else:
                if i%4==0:
                    if j==0:
                        print u'\u250C'+u'\u2534'+u'\u252C',
                    elif j==(size-1):
                        print u'\u2534'+u'\u252C',
                    else:
                        print u'\u2534'+u'\u252C'+u'\u2518',

                else: #Saltos
                    if j==0:
                        print 2*" "+ u'\u2514'+u'\u252C'+u'\u2534',
                    elif j==(size-1):
                        print u'\u252C'+u'\u2534'+u'\u2510',
                    else:
                        print u'\u252C'+u'\u2534',
        else:
            if j==0:
                print u'\u2502'+" "+u'\u2502',
            else:
                print u'\u2502',
    print (" ")


