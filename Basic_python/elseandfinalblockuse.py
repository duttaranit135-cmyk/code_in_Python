try:
    a=10
    b=2
    print(a/b)
except ZeroDivisionError:
    print("error")

else:
    print("division successful")

finally:
    print("program finished")
