def convert_cel_to_far(celcie):
    return 9/5*celcie+32
def convert_far_to_cel(fares):
    return (fares-32)*5/9

faren=int(input('Enter the temperature in F: '))
cel=int(input('Enter the temperature in C: '))
print(faren, ' degrees F = ',f"{convert_far_to_cel(faren):.2f}", 'degrees C')
print(cel, 'degrees C = ',convert_cel_to_far(cel))
#%%
def invest(initialdeposit, annualrate, year):
    finaldeposit=initialdeposit
    for i in range(1,year+1):
        finaldeposit=initialdeposit+finaldeposit*annualrate
        print('year',i,'=',f'{finaldeposit:.2f}')
        initialdeposit=finaldeposit
invest(100,0.05,4)
#%%
def factor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i, 'is a factor of ', num)
factor(12)
#%%
pythonuniversities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stat(list):
    value=[]
    tution=[]
    for i in list:
        value.append(i[1])
        tution.append(i[2])
    return value, tution
def median(list):
    return sorted(list)[len(list)//2]
def mean(list):
    return sum(list)/len(list)
print('Total students: ',sum(enrollment_stat(pythonuniversities)[0]), 'Total tuition $ ', sum(enrollment_stat(pythonuniversities)[1]))
print('Students mean ', f"{mean(enrollment_stat(pythonuniversities)[0]):.2f}", ' Students median ', mean(enrollment_stat(pythonuniversities)[0]))
print ('Tuition mean', f"{mean(enrollment_stat(pythonuniversities)[1]):.2f}", ' Tuition median ', median(enrollment_stat(pythonuniversities)[1]))


#%%
def is_prime(num):
    con=False
    for i in range(2,num):
        if num%i==0:
            con=True
            break
    if con==False:
        return True
    else:
        return False
is_prime()
#%%
