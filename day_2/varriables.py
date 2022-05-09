# python varriables



from tokenize import String
from xxlimited import Str


first_name = 'Faith'    #String
last_name = 'Kimberly'  #String
country = 'Kenyan'      #String
age = 4                 #int
year = 2018             #int
is_a_child = True       #boolean
skills = ['dancing','jumping','running','intelligent'] #list

print(first_name)
print(last_name )
print(country )
print(age)
print(year)
print(is_a_child)
print(skills)

#Declaring Multiple Variable in a Line
first_name,last_name,country,age,year,is_a_child,skills = 'Faith','Kimberly','Kenyan',4,2018,True,['dancing','jumping','running','intelligent']
print(first_name,last_name,country,age,year,is_a_child,skills)

#Checking Data types and Casting

first_name = 'Faith'    #String
last_name = 'Kimberly'  #String
country = 'Kenyan'      #String
age = 4                 #int
year = 2018             #int
weight = 13.50          #float   
is_a_child = True       #boolean
skills = ['dancing','jumping','running','intelligent'] #list
hobbies = {'foodious':'eats','determined':'focus'} #dictionary


print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_a_child))
print(type(skills))
print(type(weight))
print(type(hobbies))

#int to float

num_int = 10
numb_float = float(num_int)
print(numb_float)

#float to int
numb_float = 10.50
num_int = int(numb_float)
print(num_int)

#int to string
num_int =20
numb_str = Str(num_int)
print(numb_str)

#String to float
numb_str = '20'
numb_float = float(numb_str)
print(numb_float)

#String to list
first_name = 'Faith'
name_list = list(first_name)
print(name_list)

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('Age: ', age)
print('Skills: ', skills)

print(len(first_name))
print(len(last_name))
print(len(country))
print(len(skills))
print(len(hobbies))


  
