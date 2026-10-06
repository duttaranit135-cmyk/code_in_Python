#Write a class “Calculator” capasquare, cuble of finding be and square root of a number

class calculator:
       def __init__(self,n):
              self.n=n

       def square(self):
              print(f"The square is{self.n*self.n}")

       def cube(self):
              print(self.n*self.n*self.n)  
       def squareroot(self):
             print({self.n**1/2})


a=calculator(4)
a.square()
a=calculator(2)
a.cube()
a=calculator(16)
a.squareroot()
