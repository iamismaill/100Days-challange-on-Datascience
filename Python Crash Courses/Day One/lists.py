## Python lists 

algorithms = ['Kmeans','K-Medoids','distributed Algorithm']
print("If you want to cluster numerical values use :" + algorithms[0].title())
friends = ['Java','Farhad','Ali','Mouna','Said']
##Greating from java
print("Salamat malam :" + friends[0].title())
print("Asaalamu calaykm :" + friends[1].title()) 

##changing , adding and removing list elements

friends[0] ='Zaid'
print("We have changed the value of java to :"+ friends[0].title())

##Adding elements to th elist 
friends.append("Maryam")
friends.append("Aisha")
print(friends)

##insert function 
 
del friends[3]
print(friends)

guest_list = ['Java','Farhad','Ali','Mouna','Said']
for each_one in guest_list :
    print ("I invited you Mr." + each_one.title())
 
algorithms = ['Kmeans','K-Medoids','distributed Algorithm']
for clustering in algorithms :
    print ("This " + clustering.title() +" Algorithm we can you use clustering categorical data")

 

row_data = []
for values in range(1,5):
 row_data.append(guest_list)
 print(values)

 ## slicing the list 

 print(guest_list[0:4])

 ## Loop for the slicing 
 print ("slicing the loop :")
 for i in guest_list[0:3]:
   print(i.title())
   break    
   ## copying the list 

 my_food = ['Pizza','Chicken Maayo','Fish','Doktaritang']
 friends_food =my_food [0:3]
 print("My favourite foods are :")
 print(my_food)
 print("My friends's favourite food are:")
 print(friends_food)

 ## Exercise for slicses 
 ## question one 
 print(my_food[0:3])
 ##question two 
 print(my_food[1:3])

