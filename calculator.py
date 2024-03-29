def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def devide(x,y):
    return(x/y)

n1= eval(input("Enter the first value --> "))
n2= eval(input("Enter the second value --> "))

print("Select the Options")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multipliation")
print("4. Devision")
print("5. Exit")

while(True):
    choice = int(input("Enter the choice from(1/2/3/4/5) --->"))
    if choice in (1,2,3,4,5):
           if choice==1:
               print("Addition of two numbers ", n1, "and ",n2, "is -->", add(n1,n2))
           elif choice==2:
               print("Subtraction of two numbers ", n1, "and ", n2 , "is -->", subtract(n1,n2))
           elif choice==3:
               print("Multiplication  of two numbers ", n1, "and ", n2 , "is -->", multiply(n1,n2))
           elif choice==4:
               print("Devision of two numbers ", n1, "and ", n2 , "is -->", devide(n1,n2))
           elif choice==5:
               print("Thank you :)"
                     )
               exit()
    else:
        print("Invalid Choice Try Again")
