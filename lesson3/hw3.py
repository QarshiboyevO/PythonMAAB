#%% md
List tasks
#%%
# task1
a=['a','b','c','d','e','f','a','b']
a.count('a')
#%%
# task2
a=[1,3,5,5,2,3,4,54,12]
sum(a)
#%%
# task3
a=[1,3,5,5,2,3,4,54,12]
max(a)
#%%
# task4
a=[1,3,5,5,2,3,4,54,12]
min(a)
#%%
# task5
a=[1,3,5,5,2,3,4,54,12]
b=1
b in a
#%%
# task6
a=[]
try:
    print(a[0])
except:
    print("empty list")
#%%
# task7
a=[1,3,5,5,2,3,4,54,12]
try:
    print( a[len(a)-1])
except:
    print("empty list")
#%%
# task8
a=[1,3,5,5,2,3,4,54,12]
b=[a[0],a[1],a[2]]
print(b)
#%%
# task9
list1=[1,3,5,5,2,3,4,54,12]
list1.reverse()
list2=list1
print(list2)
#%%
# task10
a=['a','b','c','d','e','f','a','b']
a.sort()
b=a
print(b)
#%% md

#%%
# task11
a=['a','b','c','d','e','f','a','b']
b=list(set(a))
print(b)
#%%
# task12
a=['a','b','c','d','e','f','a','b']
element='e'
a.insert(3,element)
print(a)
#%%
# task13
a=['a','b','c','d','e','f','a','b']
a.index('e')
#%%
# task14
a=[1,34,2]
a==[]
#%%
# task15
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1.count(2)+list1.count(4)+list1.count(6)+list1.count(8)
#%%
# task16
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1.count(1)+list1.count(3)+list1.count(5)+list1.count(7)+list1.count(9)
#%%
# task17
a=['a','b','c','d','e','f','a','b']
b=['f','e','g','h','i','j','k','l','m','n']
a.extend(b)
print(a)
#%%
# task18
a=['a','b','c','d','e','f','a','b']
b=['a','b','c']
set(b).issubset(set(a))
#%%
# task19
a=['a','b','c','d','e','f','a','b']
element='e'
a[2]=element
print(a)
#%%
# task20
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1.sort(reverse=True)
list1[1]

#%%
# task21
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1.sort()
list1[1]
#%%
# task24
list1=[1,3,5,5,2,3,4,5,6,8,2]
len(list1)
#%%
# task25
list1=[1,3,5,5,2,3,4,5,6,8,2]
list2=list1.copy()
print(list2)
#%%
# task26
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1[(len(list1))//2]
#%%
# task27
list1=[1,3,5,5,2,3,4,5,6,8,2]
list2=list1[0:5]
max(list2)

#%%
# task28
list1=[1,3,5,5,2,3,4,5,6,8,2]
list2=list1[3:7]
min(list2)
#%%
# task29
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1.pop(5)
list1
#%%
# task30
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1==list1.sort()
#%%
# task31
list1=[1,3,5,5,2,3,4,5,6,8,2]
number=3
list1=list1*number
print(list1)
#%%
# task32
list1=[1,3,5,5,2,3,4,5,6,8,2]
list2=[1,4,2,5,6,2,4,6,1,0,23]
list1.extend(list2)
list1.sort()
list1
#%%
# task33
list1=[1,3,5,5,2,3,4,5,6,8,2]
element=2
a=list1.index(element)
print(list1.index(element),list1.index(element,a+1))
#%%
# task34
list1=[1,3,5,5,2,3,4,5,6,8,2]
list1.reverse()
print(list1)

#%%
# task35
numbers=list[range(1,20,1)]
print(numbers)
#%%
# task38
from copy import deepcopy
list1=[3,1,3]
list2=deepcopy(list1)
list1.reverse()
list1==list2



#%%
# task39
list1=[1,3,5,5,2,3,4,5,6,8,2,4]
list2=[[1,2,4,5],[5,5,6,3],[4,3,8,2]]
list2
#%%
# task40
list1=[1,3,5,5,2,3,4,5,6,8,2,4]
list2=list(set(list1))
list2
#%%

#%% md
Tuples
#%%
# task1
tuple1=(1,2,4,5,6,4,3,6,1,7)
element=1
tuple1.count(element)
#%%
# task2
tuple1=(1,2,4,5,6,4,3,6,1,7)
max(tuple1)
#%%
# task3
tuple1=(1,2,4,5,6,4,3,6,1,7)
min(tuple1)
#%%
# task4
tuple1=(1,2,4,5,6,4,3,6,1,7)
element=1
element in tuple1
#%%
# task5
tuple1=(1,2,4,5,6,4,3,6,1,7)
try:
    print(tuple1[0])
except:
    print("empty tuple")
#%%
# task6
tuple1=(1,2,4,5,6,4,3,6,1,7)
try:
    print(tuple1[len(tuple1)-1])
except:
    print("empty tuple")
#%%
# task7
tuple1=(1,2,4,5,6,4,3,6,1,7)
len(tuple1)
#%%
# task8
tuple1=(1,2,4,5,6,4,3,6,1,7)
newtuple=(tuple1[0],tuple1[1],tuple1[2])
newtuple
#%%
# task9
tuple1=(1,2,4,5,6,4,3,6,1,7)
tuple2=(1,2,2,7,4,3)
finaltuple=(tuple1+tuple2)
finaltuple
#%%
# task10
tuple1==()
#%%
# task11
tuple1=(1,2,4,5,6,4,3,6,1,7)
element=1
a=tuple1.index(element)
print(tuple1.index(element),tuple1.index(element,a+1))
#%%
# task12
tuple1=(1,2,4,5,6,4,3,6,1,7)
tupletemp=sorted(tuple(set(tuple1)))
tupletemp[len(tupletemp)-2]
#%%
# task13
tuple1=(1,2,4,5,6,4,3,6,1,7)
tupletemp=sorted(tuple(set(tuple1)))
tupletemp[1]
#%%
# task14
singletuple=(1)
singletuple

#%%
# task15
list1=[1,3,5,5,2,3,4,5,6,8,2]
listtotuple=tuple(list1)
listtotuple
#%%
# task16
tuple1=(1,2,4,5,6,4,3,6,1,7)
tuple1==sorted(tuple1)
#%%
# task17
tuple1=(1,2,4,5,6,4,3,6,1,7)
subtuple=tuple1[1:7]

max(subtuple)
#%%
# task18
tuple1=(1,2,4,5,6,4,3,6,1,7)
subtuple=tuple1[3:8]

min(subtuple)
#%%
# task19
tuple1=(1,2,4,5,6,4,3,6,1,7)
element=2
newlist=list(tuple1)
newlist.remove(element)
newtuple=tuple(newlist)
newtuple

#%%
# task20
tuple1=(1,2,4,5,6,4,3,6,1,7)
nettuple=((1,2,4),(5,6,4),(3,6,1,7))
nettuple
#%%
# task21
tuple1=(1,2,4,5,6,4,3,6,1,7)
element=2
newtuple=tuple1*element
newtuple
#%%
rango_tuple=tuple(range(1,10))
rango_tuple
#%%
tuple1=(1,2,4,5,6,4,3,6,1,7)
tuple2=tuple(reversed(tuple1))
tuple2
#%%
tuple1=(1,2,4,5,6,4,3,6,1,7)
tuple2=tuple(reversed(tuple1))
tuple2==tuple1
#%%
tuple1=(1,2,4,5,6,4,3,6,1,7)
tuple2=tuple(set(tuple1))
tuple2

#%%

#%% md
Sets

#%%
# task1
set1={1,2,3,4,5,6,4,3,6,1,7}
set2={2,5,3,7,4,2,6,1,8}
set3=set1.union(set2)
set3
#%%
# task2
set1={1,2,3,4,5,6,4,3,6,1,7}
set2={2,5,3,7,4,2,6,1,8}
set3=set1.intersection(set2)
set3
#%%
# task3
set1={1,2,3,4,5,6,4,3,6,1,7}
set2={2,5,3,4,2,6,1,8}
set3=set1.difference(set2)
set3
#%%
# task4
set1={1,2,3,4,5,6,4,3,2,1,7}
set2={2,5,3,4,2,6,1}
set2.issubset(set1)
#%%
# task5
set1={1,2,3,4,5,6,4,3,2,1,7}
element=3
element in set1
#%%
# task6
set1={1,2,3,4,5,6,4,3,2,1,7}
len(set1)
#%%
# task7
list1=[1,2,3,4,5,6,4,3,2,1,7]
set2=set(list1)
set2
#%%
# task8
set1={1,2,3,4,5,6,4,3,2,1,7}
element=3
set1.remove(element)
set1
#%%
# task9
set1={1,2,3,4,5,6,4,3,2,1,7}
set1.clear()
set1
#%%
# task9
set1={}
set1==set([])
#%%
# task11
set1 = {1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 7}
set2 = {2, 5, 3, 4, 2, 6, 1}
set2.symmetric_difference(set1)
#%%
# task12
set1={1,2,3,4,5,6,4,3,2,1,7}
element=11
set1.add(element)
set1
#%%
# task13
set1={1,2,3,4,5,6,4,3,2,1,7}
set1.pop()
set1
#%%
# task14
set1={1,2,3,4,5,6,4,3,2,1,7}
max(set1)
#%%
# task15
set1={1,2,3,4,5,6,4,3,2,1,7}
min(set1)
#%%
# task18
set1=set(range(1,10))
set1
#%%
# task19
list1=[1,2,3,4,5,6,4,3,2,1,7]
list2=[4,7,9,11,2,34]
merged=set(list1+list2)
merged
#%%
set1={1,2,3,4,5,6,4,3,2,1,7}
set2={41,72,9,11,24,34}
set1.isdisjoint(set2)
#%%
# task21
list1=[1,2,3,4,5,6,4,3,2,1,7]
tempset=set(list1)
newlist=list(tempset)
newlist
#%%
# task21
list1=[1,2,3,4,5,6,4,3,2,1,7]
tempset=set(list1)
newlist=list(tempset)
len(newlist)
#%%

#%%

#%% md
Dictionary
#%%
# task1
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
try:
    print(dictionary['d'])
except KeyError:
    print("no such key")
#%%
# task2
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
key='a'
key in dictionary
#%%
# task3
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
len(dictionary)
#%%
# task4
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
dictionary.keys()
#%%
# task5
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
dictionary.values()
#%%
# task6
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
dictionary2={'e':"age",'d':'phone number'}
dictionary.update(dictionary2)
dictionary
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
try:
    dictionary.pop('a')
except KeyError:
    print("no such key")
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
dictionary.clear()
dictionary
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
dictionary=={}
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
key='a'
dictionary.get(key)
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
key='a'
dictionary['a']='Salom'
dictionary
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
list1=list(dictionary.values())
list1.count('name')
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname'}
keys=list(dictionary.keys())
values=list(dictionary.values())
dictionary1=dict(zip(values,keys))
dictionary1
#%%
dictionary={'a':'Orifjon','b':'surname', 'c':'name'}
value='name'
keys=list(dictionary.keys())
values=list(dictionary.values())
dictionary1=dict(zip(values,keys))
dictionary1[value]
#%%
list1=[1,2,3]
list2=["salom",'hayr','bopti']
dictionry=dict(zip(list1,list2))
dictionry
#%%
dictionary={'a':'Orifjon','b':'surname', 'c':'name'}

any(isinstance(value,list) for value in dictionary.values())
#%%
dictionry={'a':{'e':"qo'y",'f':"age"},'b':'surname', 'c':'name'}
dictionry['a']['f']
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'surname','d':[]}
dictionary
#%%
dictionary={'a':'Orifjon','b':'name', 'c':'name'}
set1=set(dictionary.values())
len(set1)
#%%
dictionary={'a':'Orifjon','c':'name', 'b':'surname'}
sorted_dictionary=sorted(dictionary.items())
sorted_dictionary
#%%
dictionary={'a':'orifjon','c':'name', 'b':'surname'}
sorted_dictionary=dict(sorted(dictionary.items(), key=lambda item:item[1]))
sorted_dictionary
#%%
dictionary={'a':'Orifjon','b':'surname', 'c':'name'}
dict1={'a':'salom','d':'phone number'}
set(dict1.keys())==set(dictionary.keys())
#%%
tuple1=([1,12,2,32],[3,45,4,45])
dictionray=dict(zip(tuple1[0],tuple1[1]))
dictionray
#%%
dictionary={'a':'Orifjon','b':'surname', 'c':'name'}
list1=list(dictionary.keys())
list2=list(dictionary.values())
print(f"{list1[0]} : {list2[0]}")
#%%
