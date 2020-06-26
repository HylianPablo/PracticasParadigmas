size=9

matriz=[]
for i in range(size):
    matriz.append([])
    for j in range(size):
        matriz[i].append('*')
for i in range(2):
    print u'\u250C'+u'\u2500'+u'\u2500'+u'\u252C'+u'\u2500'+(size-2)*(u'\u2500'+u'\u252C'+u'\u2500')+u'\u2500'+u'\u2510'
    print size*(u'\u2502'+"  ")+u'\u2502'
    print u'\u2514'+u'\u2500'+u'\u2500'+u'\u2534'+u'\u2500'+(size-2)*(u'\u2500'+u'\u2534'+u'\u2500')+u'\u2500'+u'\u2518'
    


