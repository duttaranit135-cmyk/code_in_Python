def greet(fx):
    def mfx():
        print("hello good morning")
        fx()
        print("thanks good bey")
        return mfx
        
@greet
def speech():
    print("today i am talk about gen ai version 2.03.........")

def add(a,b):
    print(a+b)


speech()

   
