
#%%
def decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Denominator can't be zero"


    return wrapper
@decorator
def div(a,b):
    return a/b
print(div(2,0))
#%%
FILE_NAME = "employees.txt"


# 1. Add new employee record
def add_employee():
    empid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{empid},{name},{position},{salary}\n")

    print("Employee record added successfully.\n")


# 2. View all employee records
def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nEmployee Records:")
            for line in file:
                empid, name, position, salary = line.strip().split(",")
                print(f"ID: {empid}, Name: {name}, Position: {position}, Salary: {salary}")
            print()
    except FileNotFoundError:
        print("No records found.\n")


# 3. Search employee by ID
def search_employee():
    search_id = input("Enter Employee ID to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == search_id:
                print(f"\nEmployee Found:")
                print(f"ID: {data[0]}, Name: {data[1]}, Position: {data[2]}, Salary: {data[3]}\n")
                found = True
                break

    if not found:
        print("Employee not found.\n")


# 4. Update employee record
def update_employee():
    update_id = input("Enter Employee ID to update: ")
    updated = False
    records = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == update_id:
                name = input("Enter new name: ")
                position = input("Enter new position: ")
                salary = input("Enter new salary: ")
                records.append(f"{update_id},{name},{position},{salary}\n")
                updated = True
            else:
                records.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if updated:
        print("Employee record updated successfully.\n")
    else:
        print("Employee not found.\n")


# 5. Delete employee record
def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")
    deleted = False
    records = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] != delete_id:
                records.append(line)
            else:
                deleted = True

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if deleted:
        print("Employee record deleted successfully.\n")
    else:
        print("Employee not found.\n")


# Main menu
def menu():
    while True:
        print("=== Employee Records Manager ===")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search employee by ID")
        print("4. Update employee information")
        print("5. Delete employee record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run the program
menu()

#%%
from collections import Counter
try:
    file = open("sample.txt","r")
    content = file.read().lower()
    words = content.split()
    wordcount = len(words)

    word_count=Counter(words)
    most_com=word_count.most_common(5)

    print(f"Total words: {wordcount}""\n" "Top 5 most common words:")
    for word, count in most_com:
        print(f"{word}: {count}")


except FileNotFoundError:
    file = open("sample.txt","w")
    file.write(input("enter your paragraph: "))
    file.close()
    with open("sample.txt","r") as file:
        content = file.read().lower()
    words = content.split()
    wordcount = len(words)

    word_count=Counter(words)
    most_com=word_count.most_common(5)

    print(f"Total words: {wordcount}""\n" "Top 5 most common words:")
    for word, count in most_com:
        print(f"{word}: {count}")
#%%

