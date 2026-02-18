class Vector:
    def __init__(self,*components):
        self.components = tuple(components)
    def __len__(self):
        return len(self.components)
    def __add__(self,other):
        if len(self) != len(other):
            print("Vector addition failed")
        else:
            return Vector(*(x+y for x,y in zip(self.components, other.components)))
    def __sub__(self,other):
        if len(self) != len(other):
            print("Vector subtraction failed")
        else:
            return Vector(*(x-y for x,y in zip(self.components, other.components)))
    def __call__(self):
        return self.components

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                print("Vector multiplication failed")
            else:
                dot_product=sum((x*y for x,y in zip(self.components, other.components)))
                return dot_product
        elif isinstance(other, int):
            return Vector(*(x*other for x in self.components))
        else:
            print("Vector multiplication failed")

    def __str__(self):
        return str(self.components)
    def magnitude(self):
        magnitude=0
        for component in self.components:
            magnitude=magnitude+(component**2)
        return magnitude**0.5
    def normalize(self):

        return Vector(*((x/self.magnitude()) for x in self.components))


class EmployeeManager:
    def __init__(self,employee_id,name,salary, position):
        self.name=name
        self.salary=salary
        self.position=position
        self.employee_id=employee_id



    def addemployee(self,employee_id,name,salary,position):
        with open("employee.txt","a") as file:
            file.write(str(employee_id)+','+str(name)+','+str(salary)+','+str(position)+"\n")

    def viewall(self):
        with open("employee.txt","r") as file:

            context=file.read()
            print(context)

    def search(self,employee_id):
        with open("employee.txt","r") as file:
            for line in file:
                if str(employee_id) in line:
                    print(line)
    def update(self,employee_id):
        with open("employee.txt","r") as file:
            lines=file.readlines()
        update=False
        with open("employee.txt","w") as file:

            if lines.employee_id==employee_id:
                print("enter the new employee information")
                nameemployee=input("enter the new employee name")
                salaryemployee=input("enter the new employee salary")
                positionemployee=input("enter the new employee position")

                information=EmployeeManager(employee_id,nameemployee,salaryemployee,positionemployee)
                file.write(str(information))
                update=True
            else:
                file.writelines(lines)
            if update:
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
    def delete(self,employee_id):
        with open("employee.txt","r") as file:
            lines=file.readlines()
        with open("employee.txt","a") as file:
            if lines.employee_id==employee_id:
                pass
            else:
                file.writelines(lines)







class Employees(EmployeeManager):
    pass
emplyees=Employees("","","","")
print(f"Welcome to the Employee Records Manager!\n 1. Add new employee record \n 2. View all employee records\n 3. Search for an employee by Employee ID \n 4. Update an employee's information \n 5. Delete an employee record \n 6. Exit")
response=0
while response!=6:

    response=int(input("Enter your choice: "))

    if response==1:
        employee_id=int(input("Enter employee ID: "))
        name=input("Enter employee name: ")
        salary=float(input("Enter employee salary: "))
        position=(input("Enter employee position: "))
        emplyees.addemployee(employee_id,name,salary,position)

    elif response==2:
        print("Employee Records: ")
        emplyees.viewall()
    elif response==3:
        print("Enter Employee ID to search: ")
        id=int(input())
        emplyees.search(id)
    elif response==4:
        print("Enter Employee ID to update: ")
        id=int(input())
        emplyees.update(id)
    elif response==5:
        print("Enter Employee ID to delete: ")
        id=int(input())
        emplyees.delete(id)
    elif response==6:
        print("Goodbye")
    else:
        print("Enter a valid choice")




class ToDo:
    def __init__(self,taskid,name,description,duedate=None ,status="In progress"):
        self.taskid=taskid
        self.name=name
        self.description=description
        self.duedate=duedate
        self.status=status

    def addtask(self,taskid,name,description,duedate,status):
        with open("tasks.txt","a") as file:
            file.write(str(taskid)+','+str(name)+','+str(description)+',' + str(duedate) +','+str(status)+'\n')
    def view(self):
        with open("tasks.txt","r") as file:
            context=file.read()
            print(context)
    def updatetask(self,taskid):
        with open("tasks.txt","r") as file:
            lines=file.readlines()
            update=False
        with open("tasks.txt","w") as file:
            if lines.taskid==taskid:
                print("enter the new task information")
                nametask=input("enter the new task name: ")
                descriptiontask=input("enter the new task description: ")
                duedatetask=input("enter the new task due date(YYYY-MM-DD): ")
                status=input("enter the new task status(in progress/ complete): ")
                newtask=ToDo(taskid,nametask,descriptiontask,duedatetask,status)
                file.write(str(newtask))
                update=True
            else:
                file.writelines(lines)
            if update:
                print("Task updated successfully.")
            else:
                print("Task not found.")
    def deletetask(self,taskid):
        with open("tasks.txt","r") as file:
            lines=file.readlines()
        with open("tasks.txt","w") as file:
            if lines.taskid==taskid:
                pass
            else:
                file.writelines(lines)
    def filtertask(self,status):
        tasks=[]
        with open("tasks.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                if line[4]==status:
                    line.strip.split(',')
                    task={
                        "taskid":lines[0],
                        "name":lines[1],
                        "description":lines[2],
                        "duedate":lines[3],
                        "status":lines[4]
                    }
                    tasks.append(task)
response=0
print("Welcome to TO DO application!")
print("1. Add new task")
print("2. View all tasks")
print("3. Update an task")
print("4. Delete task")

print("5. filter the task by status")
print("6. Exit!")
task=ToDo('','','','','')

while response!=6:
    response=int(input("Enter your choice: "))
    if response==1:
        taskid=int(input("Enter task ID: "))
        taskname=input("enter the task name: ")
        taskdescription=input("enter the task description: ")
        duedate=input("enter the task due date(YYYY-MM-DD): ")
        status=input("enter the task status(in progress/ complete): ")
        task.addtask(taskid,taskname,taskdescription,duedate,status)
        print("Task added successfully.")
    elif response==2:
        print("Tasks:")
        task.view()
    elif response==3:
        id=int(input("Enter Employee ID to search: "))
        task.updatetask(id)
    elif response==4:
        id=int(input("Enter Employee ID to delete: "))
        task.deletetask(id)
    elif response==5:
        response=input("Enter the status you want to see: ")
        task.filtertask(response)
    elif response==6:
        print("Goodbye")
    else:
        print("Enter a valid choice")