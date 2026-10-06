#Add a static method in problem 2, to greet the user with hello.


class calculator:
       def __init__(self,n):
              self.n=n
        
       def square(self):
              print(f"The square is{self.n*self.n}")

       def cube(self):
              print(self.n*self.n*self.n)  
       def squareroot(self):
             print({self.n**1/2})
    
       @staticmethod
       def hello():
         print("hello there")

a=calculator(4)
a.hello()
#a.square()
#a=calculator(2)
#a.cube()
#a=calculator(16)
#a.squareroot()
