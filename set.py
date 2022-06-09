st = {"volvo","audi","toyota","isuzu"}
len(st)

print('volvo' in st)

st.add("wish")
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)

listx =('banana', 'orange', 'mango', 'lemon')
new_list = set(listx)
print(new_list)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

print(st3)

#If two sets do not have a common item or items
#  we call them disjoint sets. We can check if
#  two sets are joint or disjoint using isdisjoint() method.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)
print

#Insert multiple IT companies at once to the set it_companies
multiple_it= {"Qhala","Twiga","Turing","Upwork","Tiba"}
multiple_its= it_companies.union(multiple_it)

print(multiple_its)

#Remove one of the companies from the set it_companies
it_companies.pop()

print(it_companies)

