print('Execution Started normally')
lst = [10, 20, 30, 40, 50]
d = {1:'c', 2:'java', 3:'python', 4:'c++'}

try:
    r=int(input('Enter the rank of the language:\n'))
    print(d[r])
    num=int(input('Enter the index of numerator:'))
    den=int(input('Enter the index of denominator'))
    print(lst[num]/lst[den])
except KeyError:  #specific handlers
    print(' key does not exist')
except IndexError:
    print('Index out of bounds')
except ZeroDivisionError:
    print('Division by zero')
except : #generic handler
    print('Hey some issue occurred') 
      
print('Execution terminated normally')
