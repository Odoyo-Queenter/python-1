#Declare an empty list



fruit = ['']
print(fruit)

#Declare a list with more than 5 items
fruits = ['mango','banana','apple','grapes','ovacado','pineapple']
print(fruits)

#Find the length of your list
print(len(fruits))

#Get the first item, the middle item and the last item of the list
print(fruits[0])
print(fruits[3])
print(fruits[5])

#Declare a list called mixed_data_types, put your
# (name, age, height, marital status, address)
mixed_data_types = ['Queenter Achieng','24','156','not married','616 korongo road']
print(mixed_data_types)

#Declare a list variable named it_companies and 
# assign initial values Facebook, 
# Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Add an IT company to it_companies
it_companies.append('AkiraChix')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
# it_companies.uppercase([0])
# print(it_companies)

#Check if a certain company exists in the it_companies list.
print(it_companies[0])
print(it_companies[1])
print(it_companies[2])
print(it_companies[3])
print(it_companies[4])
print(it_companies[5])

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
print(it_companies[0:3])

#Slice out the last 3 companies from the list
print(it_companies[3:6])

#Slice out the middle IT company or companies from the list
print(it_companies[4:5])

#Remove the last IT company from the list
del(it_companies[0])
print(it_companies)

del(it_companies[4])
print(it_companies)

del(it_companies[3])
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#join the lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
sum = front_end + back_end
print(sum)

