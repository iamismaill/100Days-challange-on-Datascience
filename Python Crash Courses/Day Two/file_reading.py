


file_name ='C:/Users/Ismail/Pictures/a.txt'
with open(file_name,'w') as data:
    data.write("I am studying python \n")


## Appending text on exist file 

with open(file_name,'a') as data:
    data.write("I love Korea")

## Files 
#checking the file if there is 164

file_data = "C:/Users/Ismail/Pictures/a.txt"
with open(file_data) as data :
    info = data.readlines()

    if info =='210.123.42.76' :
        print(" we detect this ip")
    else:
        print("we don't have")

## writing on fiel 


file_data = "C:/Users/Ismail/Pictures/a.txt"

with open(file_data,'w') as data :
    data.write("I am ismail")
    print(data)


file_name ='C:/Users/Ismail/Pictures/a.txt'
with open(file_name,'w') as data:
    data.write("I am studying python \n")


## Appending text on exist file 

with open(file_name,'a') as data:
    data.write("I love Korea")