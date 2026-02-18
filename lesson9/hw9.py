

#%%

class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExceededException(Exception):
    pass
class Book:
    def __init__(self, title, author,is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Member:
    def __init__(self, name, borrowed_books:int):
        self.name = name
        self.borrowed_books = borrowed_books

class Library:
    def __init__(self, books: dict, members: dict):
        self.books = books
        self.members = members

    def add_book(self, book: Book):
        self.books[book.title] = book

    def add_member(self, member: Member):
        self.members[member.name] = member

    def borrow_book(self, book_name,member_name):
        if book_name not in self.books.keys():
            raise BookNotFoundException('Book is not found')
        if self.books[book_name].is_borrowed==True:
            raise BookAlreadyBorrowedException('Book is already borrowed')
        self.books[book_name].is_borrowed = True
        if self.members[member_name].borrowed_books>=3:
            raise MemberLimitExceededException('Member limit exceeded')
        self.members[member_name].borrowed_books+=1

    def return_book(self, book_name,member_name):
        self.books[book_name].is_borrowed = False
        self.members[member_name].borrowed_books-=1


#%%
import csv

with open('grades.csv', mode='w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['Name','Subject','Grade'])
    writer.writerow(['Alice','Math',85])
    writer.writerow(['Bob','Science',78])
    writer.writerow(['Carol','Math',92])
    writer.writerow(['Dave','History',74])

def readcsv():
    context=[]
    with open('grades.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            context.append({'Name':row['Name'],'Subject':row['Subject'],'Grade':row['Grade']})
    return context

def averagegrade(context:list):
    total={}
    count={}
    for row in context:
        if row['Subject'] not in total:
            total[row['Subject']]=int(row['Grade'])
            count[row['Subject']]=1
        else:
            total[row['Subject']]+=int(row['Grade'])
            count[row['Subject']]+=1
    average={subject: total[subject]/count[subject] for subject in total.keys()}
    with open('average_grade.csv','w',newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['Subject','Average Grade'])
        for key in average.keys():
            writer.writerow([key,average[key]])

averagegrade(readcsv())


#%%
import json
data=   [
       {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
       {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
       {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
   ]
with open('tasks.json','w',newline='') as jsonfile:
    json.dump(data,jsonfile,indent=4)

def loadjson():
    with open('tasks.json','r') as jsonfile:
        data=json.load(jsonfile)
        return data
def display():
    with open('tasks.json','r') as jsonfile:
        jsondata=json.load(jsonfile)
        print('ID','Task Name', 'Completed Status','Priority')
        for task in jsondata:
            print(task['id'],task['task'],task['completed'],task['priority'])
def rewrite(data:list):
    with open('tasks.json','w') as jsonfile:
        json.dumps(data,jsonfile,indent=4)

def totaltasks(data:list):
    return len(data)

def completedtasks(data:list):
    count=0
    for task in data:
        if task['completed']:
            count+=1

    return count

def pendingtasks(data:list):
    count=0
    for task in data:
        if task['completed']==False:
            count+=1

    return count
def avgpriority(data:list):
    priority=[]
    for task in data:
        priority.append(task['priority'])
    return sum(priority)/len(priority)

def json_to_csv(data:list):
     with open('tasks.csv','w',newline='') as csvfile:
         writer=csv.DictWriter(csvfile,fieldnames=['id','task','completed','priority'])
         writer.writerow({'id':'ID','task':'Task Name', 'completed':'Completed Status', 'priority':'Priority'})
         writer.writerows(data)


with open('tasks.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#%%
