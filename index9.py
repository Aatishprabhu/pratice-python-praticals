def fun():
    print('fun() started execution')
    
    try:
       num=int(input('Enter the  numerator:'))
       den=int(input('Enter the denominator'))
       res=num/den
       print(res)
    except ZeroDivisionError as e:
        print('Exception handled in fun()')
        raise e
    finally:
        print('fun() finished execution normally')
def main():
    print('main() started execution')
    try:
        fun()
    except ZeroDivisionError:
        print('Exception handled in main()')
        
    print('main() finished execution normally')
    
main()
        