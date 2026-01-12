
#%%
from fontTools.svgLib.path.parser import UPPERCASE
# task1
x=[1,1,2,3,8,7]
y=[1,2,3,4,5]
list1=[i for i in x if i not in y]+[j for j in y if j not in x]
print(list1)


#%%
# task2
n=int(input("enter the value of n"))
i=1
while i<n:
    print(i**2)
    i+=1
#%%
# task4
import random
play='yes'
randomint=random.randint(1,100)
i=0
while play.lower()=='yes' or play.lower()=='y':
    con=True
    while con and i<10:
        userinput=int(input("Enter your guess:"))
        if userinput==randomint:
            print('you guessed correctly')
            con=False
        elif userinput<randomint:
            print('Too low')
        elif userinput>randomint:
            print('Too high')
        i+=1
    play=input("Do you want to play?")
#%%
# task5
password=input('Enter your password:')

UPPERCASE=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
con=False
if len(password)<8:
    print('password is too short')
elif len(password)>8:
    for i in range(len(password)):
        if password[i] in UPPERCASE:
            con=True
    if con!=True:
       print('password must contain an Uppercase letter')
if con==True and len(password)>=8:
    print('password is Strong')



#%%
# task6
for i in range(2,100):
    con=True
    for j in range(2,i):
        if i!=j :
            if i%j==0:
                con=False

        j+=1
    if con==True:
        print(i)
    i+=1

#%%
# Bonus question
scorecomp=0
scoreuser=0
while scoreuser<5 and scorecomp<5:
    choice = random.choice(['rock','paper','scissor'])
    userinput=input('input your choice')
    if userinput.lower()=='rock' and choice=='scissor':
        scoreuser+=1
    elif userinput.lower()=='rock' and choice =='paper':
        scorecomp+=1
    elif userinput.lower()=='paper' and choice=='rock':
        scoreuser+=1
    elif userinput.lower()=='paper' and choice =='scissor':
        scorecomp+=1
    elif userinput.lower()=='scissor' and choice =='rock':
        scorecomp+=1
    elif userinput.lower()=='scissor' and choice=='paper':
        scoreuser+=1
    print('your score is ',scoreuser)
    print('Computer score is ',scorecomp)
if scoreuser>scorecomp:
    print('you win')
else:
    print('you lose')

#%%
# task3
tex=input("enter your text:")
vowel="aiuoeAIEOU"
result=[]
i=0
while i<len(tex)-1:
    result.append(tex[i])
    if (i+1)%3==0 and i<len(tex)-1:
        if tex[i] in vowel or (i>0 and result[i-2]=='_'):
            result.append(tex[i+1])
            if i+2<len(tex):
                result.append('_')
            i+=1
        else:
            result.append('_')
    i+=1


print ("".join(result))