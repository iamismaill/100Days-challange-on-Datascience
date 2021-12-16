from random import randint, random
class Dog :
    name = 'J'
    age = '20'
    def __init__(self,name,age) -> None:
        print("Hello")


print(Dog.name)
print(Dog.age)
    

class Studentinf :
    name = input("Your name")
    age = input("Your age")

    m = int(age)
    uni = input("Your uni name")
    
    def __init__(self,name,m,uni) -> None:
        pass

print(Studentinf.name)
print(Studentinf.uni)
print(Studentinf.m)


## A car class - this class contains model , color ,year of the car  (My own way)
class Car :
    
    def __init__(self,model,color,year) -> None:
        self.model = model 
        self.color = color
        self.year = year 
    def descriptive_info(self) :
        car_info =print(f"{self.model},{self.color},{self.year}")
         
my_new_car = Car('TB20','Red',2021)
print(my_new_car.descriptive_info())


## user input for user's car wish 
class User_car :
    modela = input("your model")
    color = input("your color")
    year = input("your year")

    def __init__(self,model,color,year) -> None:
    
       self.model = model 
       self.year = year
       self.color = color

    def desc_info(self) :
        
        car_info =print(f"You car's model is {self.model}, Your cars's color is {self.color} and Your car's year is {self.year}")
    
data = User_car(model =User_car.modela,color =User_car.color,year =User_car.year)
print(data.desc_info())

from random import randint

a =randint(1,10)
print(a)

from random import choice
favourtie =['I','M','D','K','L']
d = choice(favourtie)
for i in d:
    print(i)

 ##Lottery game (Print randomly 5 persons that win this lotery )
 
guest_list = ['Java','Farhad','Ali','Mouna','Said','Mohamed','Aisha']
 

for i in  range(0,4):
    i = choice(guest_list)
    print(f"These are the four persons win the lottery {i.title()}")

    
    #file soo akhrisasho 

with open('hello.txt') as myfile :
    a = myfile.read()
    print(a)

    ## file in other location 
 

## put the file data into list
file ="C:/Users/Ismail/Pictures/a.txt"
list = []
with open(file) as file_info:
    data = file_info.readlines()
    list.append(data) 
    for i in list :
       print(i)

#checking the file if there is 164
file_data = "C:/Users/Ismail/Pictures/a.txt"
with open(file_data) as data :
    info = data.read()
    print(info)
    finding_IP='210.123.42.76'
    for line in info:
        finding_IP += line.strip()
    ##finding_IP ='2210.123.42.76\n210,123,42.0\t\n210.123.32.13\n164.124.101.2'
    if info in finding_IP:
        print(" we detect this ip")
    else:
        print("we don't have")

        