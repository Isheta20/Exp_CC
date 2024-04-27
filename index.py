print('Isheta Aggarwal')
def maximum(a, b, c): 
    if (a >= b) and (a >= c): 
        largest = a 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
    return largest 

# User input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

print("The largest number is:", maximum(a, b, c))
