

# problem1
a=float(input("enter a number: "))
print(round(a,2))
#%%
# problem2
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
print('Maximum of numbers is ',max(a,b,c))
print('Minimum of numbers is ',min(a,b,c))
#%%
# problem3
km=float(input("enter km: "))
meters=km*1000.0
cantimeters=km*100000.0
print('meters = ',meters)
print('cantimeters = ',cantimeters)
#%%
# problem4
a=int(input("enter a number: "))
b=int(input("enter a number: "))
print('answer: ' ,a//b,' remainder: ' ,a%b)
#%%
# problem5
celcius=float(input("enter celcius: "))
fahrenheit=celcius*1.8+32
print('fahrenheit = ',fahrenheit)
#%%
# problem6
a=int(input("enter a number: "))
print(a%10)
#%%
# problem7
a=int(input("enter a number: "))
if a%2==0:
    print('even')
else:
    print('odd')
#%%
# problem1
name=input("enter your name: ")
birthyear=int(input("enter your birth year: "))
print('you are ',2026-birthyear,'years old')
#%%
# problem2
txt = 'LMaasleitbtui'
print(txt[0]+txt[3:5]+txt[6]+txt[8]+txt[-3]+txt[-1:])
print(txt[1:3]+txt[5]+txt[7]+txt[9]+txt[11])
#%%
# problem3
text=input("enter a text: ")
print(len(text))
print(text.upper())
print(text.lower())
#%%
# problem4
text='12321'
text2=text[::-1]
if text==text2:
    print('palindrome')
else:
    print('not palindrome')

#%%
# problem5
text='aasasdkan'
vovels=['a', 'e', 'i', 'o', 'u']
count=0
for i in range(len(text)):
    if text[i] in vovels:
        count+=1
print(count)
#%%
# problem6
string1='asdacdfcafsdcf'
string2='asd'
if string2 in string1:
    print(True)
#%%
# problem7
text=input("enter a text: ")
replace=input("enter replace word: ")
value=input("enter your word: ")
text=text.replace(replace,value)
print(text)
#%%
# problem8
string=input("enter a text: ")
print(string[0],string[-1])
#%%
# problem9
text=input("enter a text: ")
print(text[::-1])
#%%
# problem10
sentence=input("enter a sentence: ")
print(len(sentence.split()))
#%%
# problem11
digits=['0','1','2','3','4','5','6','7','8','9']
word='1ncwjkasdfbck2qn34jn4'
condition=False
for i in range(len(word)):
    if word[i] in digits:
        condition=True
if condition:
    print('String contains at least a digit')


#%%
# problem12
words=['hello','world','hi','this']
word=''
for x in words:
    word=word+x+', '
print(word)

#%%
# problem13
string=input("enter a text: ")
print(string.replace(' ',''))
#%%
# problem14
string1=input("enter a text: ")
string2=input("enter a text: ")
if string1==string2:
    print('The strings are equal')
else:
    print('The strings are not equal')

#%%
# problem15
text=input("enter a text: ")
list1=text.split()
word=''
for x in list1:
    word+=(x[0])
print(word)
#%%
# problem16
string=input("enter a text: ")
char=input("enter a character: ")
print(string.replace(char,''))
#%%
# problem17
text=input("enter a text: ")
vowels=['a','e','i','o','u']
for i in vowels:
    text=text.replace(i,'*')
print(text)
#%%
# problem18
sentence=input("enter a sentence: ")
a=sentence.split()
print('sentence starts with: ',a[0])
print('sentence ends with:',a[-1])
#%%
# problem1
username=input("enter your name: ")
password=input("enter your password: ")
if username=='':
    print('username is empty')
elif password=='':
    print('password is empty')
else:
    print('username and password are not empty')
#%%
# problem2
num1=3
num2=5
if num1==num2:
    print('numbers are equal')
else:
    print('numbers are not equal')

#%%
# problem3
num=124
if num>0 and num%2==0:
    print('number is even and positive')
#%%
# problem4
num1=2
num2=3
num3=4
if num1!=num2 and num1!=num3 and num2!=num3:
    print('numbers are different')
#%%
# problem5
string1='asddsada'
string2='asdasdasda'
if len(string1)==len(string2):
    print('Strings have the same length')
else:
    print('Strings have different length')
#%%
# problem6
num=30
if num%3==0 and num%5==0:
    print('number is divisible by 3 and 5')
#%%
# problem7
num1=123
num2=12
if num1+num2>50.8:
    print(True)
#%%
num2=15
if num2>=10 and num2<=20:
    print(True)
#%%
