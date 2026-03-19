import sys #system functions (exit, arguments, etc.)

def sum_numbers(numbers): #function that sum list numbers
    tot = 0
    for i in numbers:
        tot += i
    return tot


#main code starts here
numbers = [] #list numbers
try:
    total_numbers_list = int(input("Insert Total Numbers List: "))
except ValueError:
    print("Invalid Inpud. Code Terminated!")
    sys.exit() #Code Terminated 


for i in range(total_numbers_list): #for from 0 to total_number_list
    while True:
        user_input = input("Insert Number " + str(i) + ": ")
        try:
            num = float(user_input)
            numbers.append(num)
            break #exit the while loop if input is valid
        except ValueError:
            print ("Invalid Number Input!")


print("Numbers Entered: " + str(numbers)) #print every num of the list - vedere se inserted numbers va bene
print("Result: " + str(sum_numbers(numbers))) #print sum of numbers
