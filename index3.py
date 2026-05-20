print('secure connection has been established to the bank server')

try:
    p=int(input('Enter your principal amount'))
    t=int(input('Enter the duration '))
    r=10
except:
    print('please provide the numerical values')
else:
    si=(p*t*r)/100
    print('simple interest =',si)
    
print('Secure connection has been closed to the bank server')
          
            