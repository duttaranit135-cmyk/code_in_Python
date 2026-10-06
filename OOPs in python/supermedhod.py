class Employee:

  def __init__(self):
    print("it is constractor 1")
    
class Programmer(Employee):
  
  def __init__(self):
        #super().__init__()
        print("it is constractor 2")
  

class Manager(Programmer):

      def __init__(self):
        super().__init__()
        print("it is constractor 3")
        

m=Manager()

#this method apply for parent constractor showing.process -first it run parent constractor then run child constractor.

   
