def name(number):
    if number == 0:# base case
        return
    else: # recursive case
        print("name")
        name(number-1)


name(10)


def num(number): 
    if number == 0:
        return
    else:
        num(number-1)
        print(number)

num(20)



def sum(number):
    if number == 0:
        return 0

    else:
        return number + sum(number-1) 

        

total = sum(10)
print(total)


def product(number):
    if number == 1:
        return 1

    else:
        return number*product(number-1)


total_2 = product(5)
print(total_2)