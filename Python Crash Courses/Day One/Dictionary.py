## Dictionary

allien_0 = {'color':'green','points':5}
print(allien_0['color'])

## Product dictionaris 
products = {'Hp' :400,'lenova':900,'Samsung':800,'Toshiba':800}
for product in products:
  print(product)

  ## Condition in dictinaries
  products = {'Hp' :400,'lenova':900,'Samsung':800,'Toshiba':800}
for product in products:
    if product == 'lenova':
        print(product.upper())
    else:
        print(product.title())
 
favrt_lang ={
    'Ismail':'Python',
    'Ali':'Java',
    'Java': 'Java',
    'Ashwin':'C++'
}
for name , fvrt in favrt_lang.items():
    print (name +"'s favourite language is :" + fvrt)
 

##using getting function 

print(favrt_lang.get('Ashwin','There is no value'))
print(favrt_lang.get('Revin','There is no value'))

## Exercise 

friends_info ={'first_name':'Mohamud','last_name':'Ali','Age':20}
print(friends_info)

user_info = {
    'first_name':'Ismail',
    'last_name':'Ali',
    'user_name': 'Ahmed'
}

for keys,values in user_info.items():
    print(keys)
    print(values)

## looping only the key 
## two ways 
for key in user_info:
    print (key)
for key in user_info.keys():
    print(key)

## nesting dictinaries to list 
Data_subjects ={'Subject':'Pandas','Subject':'Text analyze'}
C_subjects = {'subject':'Algorithms','Subject':'Independent study'}

whole_subjects= [Data_subjects.values(),C_subjects.values()]
for values in whole_subjects:
    print(values)


## making list in 30 
data = []

for values in range(100):
    favrt_lang
    data.append(favrt_lang)

for values in data :
    print(values)


laptop_features = {
    'name':'HP',
     'features':['Black','Monitor 15 inch','500 GB','Ram 4gb'],
     
}

print(f" you have order a {laptop_features['name']} - "
"with the following feautres:")
for feature in laptop_features['features']:
    print(feature)


    favrt_lang ={
    'Ismail':['Python','Java','C++','Koltin','C#'],
    'Ali':['Java'],
    'Java': ['Java'],
    'Ashwin':['C++']
}

###imsails fravboute languages are :

for name,lanuages in favrt_lang.items():
    print(f"\n{name.title()}'s favourite languages are :")
  
for language in lanuages:
    print(f"\t{language.title()}")

## user inputs 
##message = input("Write something")
 
favourti = input(" What is your favourtie p_language")
print("\nmy favourite is " + favourti)

height = input(" how tall are u ?")
mesasge = int(height)

if mesasge > 20 :
    print("you're tall enough to ride !")
else :
    print ("you're not enough to ride ") 


#if number is odd or even 

number = input ("Enter a number , I will tell you if it's odd or even")
message = int(number)

if message % 2 == 0:
    print (" This is even number ")
else :
    print(" This is odd number " )

## Practical Excercise
## Rntal car 

rental_car = input(" What's your favourite rental car ?")
print(rental_car)

## Order_seating 
numberof_pple = input("How many people are in your dinner group ?")
message = int(numberof_pple)

if message > 8 :
    print (" you have to wait another table please ~~~")
else:
    print(" Your table is ready  ")