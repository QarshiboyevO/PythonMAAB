import math

class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Operand must be a Vector")
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")


    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])


    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])


    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Invalid operand")


    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*[round(a / mag, 3) for a in self.components])


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_file(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        open(self.FILE_NAME, "a").close()

    def _read_all(self):
        with open(self.FILE_NAME, "r") as f:
            return f.readlines()

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        if self.search_employee(emp_id, silent=True):
            print("Employee ID already exists!")
            return

        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        emp = Employee(emp_id, name, position, salary)
        with open(self.FILE_NAME, "a") as f:
            f.write(emp.to_file())

        print("Employee added successfully!")

    def view_all_employees(self):
        records = self._read_all()
        if not records:
            print("No records found.")
            return
        print("\nEmployee Records:")
        for r in records:
            print(r.strip())

    def search_employee(self, emp_id, silent=False):
        for line in self._read_all():
            if line.startswith(emp_id + ","):
                if not silent:
                    print("Employee Found:")
                    print(line.strip())
                return line
        if not silent:
            print("Employee not found.")
        return None

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        records = self._read_all()
        updated = False

        with open(self.FILE_NAME, "w") as f:
            for line in records:
                if line.startswith(emp_id + ","):
                    name = input("New Name: ")
                    position = input("New Position: ")
                    salary = input("New Salary: ")
                    emp = Employee(emp_id, name, position, salary)
                    f.write(emp.to_file())
                    updated = True
                else:
                    f.write(line)

        print("Employee updated!" if updated else "Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        records = self._read_all()
        found = False

        with open(self.FILE_NAME, "w") as f:
            for line in records:
                if not line.startswith(emp_id + ","):
                    f.write(line)
                else:
                    found = True

        print("Employee deleted!" if found else "Employee not found.")

    def menu(self):
        while True:
            print("""
Welcome to the Employee Records Manager!
1. Add new employee
2. View all employees
3. Search employee
4. Update employee
5. Delete employee
6. Exit
""")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee(input("Enter Employee ID: "))
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

from abc import ABC, abstractmethod
import csv
class Storage(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

class CSVStorage(Storage):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["id", "title", "description", "due_date", "status"]
            )
            writer.writeheader()
            writer.writerows(tasks)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []

class TodoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self):
        task = {
            "id": input("Task ID: "),
            "title": input("Title: "),
            "description": input("Description: "),
            "due_date": input("Due Date (YYYY-MM-DD): "),
            "status": input("Status: ")
        }
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        for t in self.tasks:
            print(", ".join(t.values()))

    def update_task(self):
        task_id = input("Enter Task ID: ")
        for t in self.tasks:
            if t["id"] == task_id:
                t["title"] = input("New Title: ")
                t["description"] = input("New Description: ")
                t["due_date"] = input("New Due Date: ")
                t["status"] = input("New Status: ")
                print("Task updated!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID: ")
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        print("Task deleted!")

    def filter_tasks(self):
        status = input("Enter status to filter: ")
        for t in self.tasks:
            if t["status"].lower() == status.lower():
                print(", ".join(t.values()))

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved.")

    def menu(self):
        while True:
            print("""
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Filter Tasks
6. Save Tasks
7. Exit
""")
            choice = input("Choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                break