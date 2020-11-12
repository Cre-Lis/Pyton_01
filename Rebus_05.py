L = 1000 # глубина поиска
for x in range (-L,L+1):
    print(x)
    for y in range (-L,L+1):
        for z in range (0,L+1):

            #if( x**3 + y**3 + z**3 == 10 ):
            if( x*x*x + y*y*y + z*z*z ==  10 ):
                print(x,y,z)
        
