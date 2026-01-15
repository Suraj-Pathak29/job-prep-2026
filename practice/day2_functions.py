# Check if a number is even or odd

def check(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"
#FUNCTION CALL
#check(4)



# Find factorial of a number

def factorial_check(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial

a = int(input("Enter the number: "))
print(f"Factorial of {a} is {factorial_check(a)}")



# Return maximum of two numbers

def max_of_two(x,y):
    if x>y:
        return x
    else:
        return y
result = max_of_two(10,20)
print(result)



# Count vowels in a string

def count_vowel(ch):
    count = 0
    for i in ch:
        if i in ('a','e','i','o','u','A','E','I','O','U'):
            count += 1
    return count
a = "Education"
print(f"Total vowels in {a} = {count_vowel(a)}")



# Simple calculator function (+, -, *, /)

def add(x,y):
    return x + y

def subtract(x,y):
    if x>y:
        return x - y
    else:
        return y-x
    
def multiply(x,y):
    return x * y

def division(x,y):
    return x / y

print(add(5,10))
print(subtract(3,5))
print(multiply(8,10))
print(division(11,5))