#Create an empty tuple
empty_tuple = ()
print(empty_tuple)

#Create a tuple containing names of your sisters and your brothers 
#Join brothers and sisters tuples and assign it to siblings
#How many siblings do you have
#Modify the siblings tuple and add the name of your father and
#mother and assign it to family_members

sisters = ('Myrah','Angelah','Shiloh')
brothers = ('Athan','Junior','Gedion')
siblings = sisters + brothers
print(siblings)
print(len(siblings))

parents = ('Angeline Atieno','Bob Aloo')
family_members= siblings + parents
print(family_members)

#Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp
fruits_tuple =('mango','apple','banana')
vegetables_tuple = ('carrot','cabbage','sukumawiki')
animal_product_tuple = ('milk','meat','manure')
food_stuff_tp = fruits_tuple + vegetables_tuple + animal_product_tuple
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = fruits_tuple + vegetables_tuple + animal_product_tuple
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from 
#the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[4:5])
print(food_stuff_tp[4:5])

#Slice out the first three items and 
#the last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[6:9])





