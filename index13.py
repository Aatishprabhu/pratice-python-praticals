lst=[10,20,30]
def sum_list(items):
    sum_numbers=0
    for x in items:
        sum_numbers += x
    return sum_numbers
print("sum of the list;",sum_list(lst))