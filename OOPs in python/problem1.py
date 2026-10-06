#Create a class “Programmer” for storing information of few programmers working at
#Microsoft.


class programmer:
    company="microsoft"

    def __init__(self, name, dept, salary):
        self.name=name
        self.dept=dept
        self.salary=salary
           
p=programmer("name=ranit\n","dept=project manager\n","salary=450000\n")
print(p.name,p.dept,p.salary)
p=programmer("sohon","data analysis",120000)
print(p.name,p.dept,p.salary)
p=programmer("sudip","product verification",45000)
print(p.name,p.dept,p.salary)
