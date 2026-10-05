class Employee:
    salary=120000
    company = "Google"
     # Specific to Each Class

Ranit = Employee() # Object Instantiation

#Ranit.company
Employee.company = "YouTube" # Changing Class Attribut

print(Ranit.company,Ranit.salary)