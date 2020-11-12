
def diff():
    m = int(input('Введите первое число: '))
    n = int(input('Введите второе число: '))
    if m > n:
        print(m-n)
    else:
        print(n-m)
        
    return m,n

a,b = diff()
c,d = diff()
e,f = diff()


print(a,b,c,d,e,f)
