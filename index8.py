def fun2():
    print('fun2() started execution')
    num=int(input('Enter the  numerator:'))
    den=int(input('Enter the denominator'))
    res=num/den
    print(res)
    print('fun2()finished execution normally')
    
def fun1():
    print('fun1() started execution')
    
    print('fun1() finished execution normally')
    
def main():
    print('main() started execution')
    try:
        fun2()
    except ZeroDivisionError:
        print('Exception handled in main()')
        
    print('main() finished execution normally')
    
main()
        
    