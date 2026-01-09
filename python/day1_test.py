# REVERSE A STRING

a = input("enter the string: ")
rev = "".join(reversed(a))
print("original string: ",a)
print("reversed string: ",rev)



# COUNT FREQUENCY OF CHARACTERS

a = input("enter the string: ")
char = input("Enter the character to count its frequency: ")
count = 0
for i in a:
    if i==char:
        count += 1
    else:
        pass
print(f"Total frequency of {char} is {count}")



# CHECK FOR PRIME

a = int(input("Enter the number: "))
count = 0
for i in range(2,a):
    if a%i == 0:
        count += 1
if a == 1 or a ==0:
    print(f"{a} is not a prime number")
elif count > 0:
    print(f"{a} is not prime")
else:
    print(f"{a} is a prime number")



# CHECK FOR PRIME IN RANGE

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
for i in range(lower , upper+1):
    if i>1:
        is_prime = True
        for num in range(2,i):
            if i%num == 0:
                is_prime = False
                break
        if is_prime:
            print(i , end=" ")



# FIND SECOND LARGEST NUMBER IN A LIST

a = list(map(int,input("Enter the list: ").split(',')))
unique = list(set(a))
if len(a) < 2:
    print("There is no second number")
else:
    unique.sort(reverse = True)
    print("second largest number is ", unique[1])



# SIMPLE CLASS WITH CONSTRUCTOR AND METHOD

class Student():
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def details(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")

#Creating Object
student1 = Student("Suraj" , 101)
#Calling Method
student1.details()



# CORE QUESTIONS
# 1 - WHAT IS CLASS
# ANS- A class is a blueprint or template used to create objects 

# 2 - WHAT __init__ does?
# ANS- It initializes the object data when the object is created

# 3 - WHAT self means?
# ANS- self refers to the current object
