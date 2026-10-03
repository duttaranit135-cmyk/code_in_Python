def avg():
    a=int(input("enter number1: "))
    b=int(input("enter number2: "))
    c=int(input("enter number3: "))

    average=(a+b+c)/3
    print(average)

avg()
avg()
avg()

#use parameter

def goodday(name,ending):
    print("good day,"+name)
    print(ending)

goodday("ranit","thank you")

#recursion
def factorial(n):
     if(n==1):
      return 1
     else:
      return n*factorial(n-1)

n=int(input("enter a number: "))
print("factorial in given number:",factorial(n))

    
