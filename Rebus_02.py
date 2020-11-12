for a in range (10):
 for b in range (10):
  for c in range (10):
   for d in range (10):
    for e in range (10):
     for f in range (10):
         if( (a+b+c+d+e+f == 8) and
             (   (a*100000 + b*10000 + c*1000 + d*100 + e*10 + f*1 + 1) % 8  == 0    )   ):
             print(a,b,c,d,e,f)

# Пароль на сообщество 1234        
