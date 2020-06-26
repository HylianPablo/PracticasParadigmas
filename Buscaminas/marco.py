COE  = u'\u2500' 
CNS  = u'\u2502' 
CES  = u'\u250C' 
CSO  = u'\u2510' 
CNE  = u'\u2514'  
CON  = u'\u2518'  
COES = u'\u252C' 
CNES = u'\u251C'  
CONS = u'\u2524'  
CONE = u'\u2534'  
CSOM = u'\u2593'

filas=9
columnas=9


print '\n',
print '  ' + CES + (3 * COE) + COES + ((columnas-2)*((3 * COE) + COES)) + (3 * COE) + CSO,
print '\n',
for i in range(filas):
    for j in range(columnas):
        print ' '+ ((3 if (i%2==1) else (1)) * (" "))+ CNS + ' ' + '0' if(j==0) else(CNS+' '+'0'),
    print CNS,
    print '\n',
    if i==filas-1:
        print ('  ' + CNE + (columnas-1)*(3*COE + CONE) + 3*(COE) + CON)
    elif (i%2==0):
        print (('  ' + CNE + (columnas)*(COE + COES + COE + CONE) + COE + CSO))
    else:
        print (('  ' + CES + (columnas)*(COE + CONE + COE + COES) + COE + CON)) 
