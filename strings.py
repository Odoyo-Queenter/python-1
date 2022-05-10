#creating a string
greeting = 'Hello World'
print(greeting)
print(len(greeting))

sentence = 'I always enjoy coding and I love python'
print(sentence)
print(len(sentence))

#multiline string
multiline_string = ''' I am a student at Akirachix and I enjoy coding.
I'm diploma in software engineering and looking foward to thrive in the
industry.'''
print(multiline_string)

multiline_string = """ I am a student at Akirachix and I enjoy coding.
I'm diploma in software engineering and looking foward to thrive in the
industry."""
print(multiline_string)

#String concatination
first_name = 'Queenter'
last_name = 'Achieng'
space = ' '
full_name = first_name + space+ last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(full_name))

#Escape sequence in strings
print('I hope everyone is enjoying the Python Challenge.\nAre you ?')
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')





#string interpolation
fruit = 'mango'
drinks = 'milk'
study = 'books'
print(f"I love {fruit} {drinks} {study} and love's  Faith")

a=4
b=6
print(f'{a} + {b}')
print(f'{a} - {b}')
print(f'{a} * {b}')
print(f'{a} / {b}')
print(f'{a} **{b}')
print(f'{a} //{b}')

school = 'AkiraChix'
languages = 'python, kotlin,javascript'
labs = 'AnitaB, HopperLab, EidderLab'
print(f'I love our school {school} because we are being taught {languages} in defferent labs like {labs}')

#String formating
a=4
b=6
print('{} + {}'.format(a,b))
print('{} - {}'.format(a,b))
print('{} * {}'.format(a,b))
print('{} / {}'.format(a,b))
print('{} **{}'.format(a,b))
print('{} //{}'.format(a,b))

school = 'AkiraChix'
languages = 'python, kotlin,javascript'
labs = 'AnitaB, HopperLab, EidderLab'
print('I love our school {} because we are being taught {} in defferent labs like {}'.format(school,languages,labs))


#Accessing Characters in Strings by Index
#positive indexing
language ='python'
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
print(len(language))

#negative indexing
language ='python'
print(language[-1])
print(language[-2])
print(language[-3])
print(language[-4])
print(language[-5])
print(language[-6])
print(len(language))

#string slicing
name = 'Daniel'
first_three = name [0:3]
print(first_three)
print(name[0:4])
print(name[0:6])
print(name[5:6])
print(name[1:3:4])

#negative indexing
name = 'Daniel'
first_three = name [0:3]
print(first_three)
print(name[-4:-6])
print(name[-2:-6])
print(name[-5:-6])
print(name[-3:-6])

#String methods
laptop = 'thinkpad'
print(laptop.title())
print(laptop.capitalize())
print(laptop.isalnum())
print(laptop.endswith('pad'))
print(laptop.startswith('ink'))
print(laptop.replace('t','T'))
print(laptop.find('y'))
print(laptop.find('k'))

challenge = 'Thirty'
print(challenge.isdigit()) 
challenge = '30'
print(challenge.isdigit())   
challenge = '\u00B2'
print(challenge.isdigit())   
















