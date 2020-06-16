class Employee:                                            #creating an Employee class
    emp_count = 0                                          #creating a variable
    emp_salaries = []                                      #creating a list

    def __init__(self, name, family, salary, department):  #creating a __init__ method which always be called when an obj is created
        self.emp_name = name                               #assining arguments values 
        self.emp_family = family
        self.emp_salary = salary
        self.emp_department_name = department
        Employee.emp_count +=1                             # increasing emp count
        Employee.emp_salaries.append(salary)               # appending salaries to emp_salaries list

    def displayEmp(self):                                  # creating a method to display employee details      
        print("Name : ", self.emp_name, ", Family Name : ", self.emp_family, ", Salary: ", self.emp_salary, ", department: ", self.emp_department_name)

    def get_salary(self):                                  # creating a method to calculate avg of employees salaries
        total_salaries = 0
        for i in Employee.emp_salaries:                    # looping through employee salaries
            total_salaries = total_salaries + i            # Adding all employee salaries
        return total_salaries / len(Employee.emp_salaries) # returing avg of all emp salaries

class FullTimeEmployee(Employee):                          # creating a fulltimeemployee class which inherits Employee class
    def __init__(self, name, family, salary, department):   #creating a __init__ method for fulltimeemployee class which always be called when an obj is created
        Employee.__init__(self, name, family, salary, department) #calling __init__ method of Employee class

E1 = Employee("harika", "gurram", 1000000, "CS")            # passing employee details to Employee class
E2 = Employee("arun", "anthati", 1200000, "CSE")
E3 = FullTimeEmployee("monica", "thati", 600000, "CS")      # passing employee details to FullTimeEmployee class
E4 = FullTimeEmployee("Lalitha", "Devasnh", 600000, "CS")
print("Total Employees %d" % Employee.emp_count)            # printing out total number of employees
avg_salary = E1.get_salary()                                # calling get_salary method of Employee class
print("All the employees together has an average salary of", avg_salary)    # printing out avg of all employees
print("The Employees details are :")
print(E1.displayEmp(),E2.displayEmp(),E3.displayEmp(),E4.displayEmp())      # printing out details of each employee
