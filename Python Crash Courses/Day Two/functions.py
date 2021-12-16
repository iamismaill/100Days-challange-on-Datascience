from typing import Counter

import module
def get_user(username):
    data = input(" username")
    data =username
    print(data)
get_user('data')

## two paramaters 

def get_userinfo(name,age):
    print(f"My name is :{name.title()}")
    print(f"My age is :{age.title()}")
get_userinfo('Ismai','23')
get_userinfo('farah','24')

##Input the arguments
data1 = input("What is your name")
data2 = input("Whats your age ?")
def get_userinfo(name,age):
    print(f"My name is {name.title()}")
    print(f"My age is {age.title()}")
get_userinfo(name=data1 ,age=data2)

city = input("Input the city name")
country = input("Input the country name")
def describe_city(city_name,country_name):
    print(f"This {city_name.title()} city belongs to {country_name.title()} Country")
describe_city(city_name= city , country_name=country)

## return function 
def get_username(username):
     print(f"My username is {username}")
     return  
get_username('ismail')

## if the user inputs full name return full name , if user not input the median name return first name and last name
f_name =input("enter your first name")
m_name = input("enter your middle name")
last_name = input("enter your last name")

def get_formatted_name (first_name,midle_name,last_name):
    if m_name:
        print(f"My full name is {f_name.title()} {m_name.title()} {last_name.title()}")
    else:
        print(f" My name is {first_name.title ()} {last_name.title()}")

        ## Function with dictinary
get_formatted_name(f_name,m_name,last_name)
 

## function with while loop
name =input("Name !")
age = input("Age ~")
active = True
def get_formatted_name(f_name,age):

    while active:
        print(f"My name is {name.title()} and age is {age.title()}")
        break
get_formatted_name(f_name =name,age=age)


def get_person_info(f_name,uni_name):
    while True:
        print(f"name{f_name.title()} uni_name{uni_name.title()}")
        break
get_person_info('ismai','Kookmin uni')


## Function with list 
lista =['ismail','Ali','Mohamed','Farah']
def list_names(names) :
 
   print(lista)
list_names(names=lista)

## Function with list and for loop 
lista =['ismail','Ali','Mohamed','Farah']
def list_names(names):
    for name in names :
        print("Hello " +name)
list_names(names =lista)

## empty list with function 
user_info = []
age =[]
university_name = []

def get_info(username,age ,uni_name) :
    m_user_name = input("Enter your username")
    m_age = input("Enter your age")
    m_uni = input("Enter your univesity")
    user_info.append(m_user_name)
    user_info.append(m_age)
    user_info.append(m_uni)
    for magaca in user_info :
        print(magaca)
        
         
     
get_info(username=user_info ,age = user_info,uni_name=user_info)