# Function

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a * b
def division(a,b):
    return a//b
    
a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))
add_result = add(a,b)
sub_result = sub(a,b)
multiply_result = multiply(a,b)
division_result = division(a,b)
print("Addition : ",add_result)
print("Subtraction : ",sub_result)
print("Multiplication : ",multiply_result)
print("Division : ",division_result)