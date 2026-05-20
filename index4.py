print("Execution Started Normally")
lst = [10, 20, 30, 40, 50]
d = {1:'c', 2:'c++', 3:'java', 4:'python'}

try:
    r = int(input("Enter the rank of the language \n"))
    print(d[r])
    num = int(input("Enter the index of numerator"))
    den = int(input("Enter the index of denominator"))
    print(lst[num]/lst[den])
except:
    print('Hey there is an issue!!')
print("Execution Completed Normally")    