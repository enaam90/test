# Badic Data Types

library_name = 'Iqraa'
#fname, sname = 'Asha', 'Ali' 
#count1= count2= count3 = 0
#print('>>>>>>>>>>>', fname, sname, count1, count2)

print('Name-----------------', library_name)

# slicing
'''
print('slicing --------', library_name[1:3])
print('slicing --------', library_name[2:])
print('slicing --------', library_name[:4])
print('--------------', library_name[0] ,library_name[-1])
print('slicing --------', library_name[-3:-1])
print('len----------', len(library_name))
'''
# formating
# ‘%s’ is used to inject strings ‘%d’ for integers, ‘%f’ for floating-point values, ‘%b for binary
"""
print('Welcome to %s' %library_name)
year = 2022
print('Welcome to %s! its %s' %(year, library_name))

print('{2} {1} {0}'.format('directions', 'the', 'Read'))
age = 7.225
print('The age of the library is: %5.2f' %age)
"""

# comparision

"""library_name2 = 'Iqraa'
library_name3 = 'iqraa'
print('IS library_name is same as library_name2 ?', library_name == library_name2)
print('IS library_name is same as library_name2 ?', library_name == library_name3)
print('IS library_name is not library_name2 **** ?', library_name != library_name3)
print('IS library_name is not library_name2 ?', library_name is library_name2)
""" 

# conversion
"""
year = 2022
print('Year data type', type(year))

year2= 2022
print('>>>>>>>>>>>>>>>>>>', year == year2)
year =  str(year)
print('>>>>>>>>>>>>>>>>>>', year == year2)
print('Year as string', type(year) )
year = int(year)
print('Year as int again', type(year))
next_year = '2023'
#print('sub---------------', next_year - year)
print('sub---------------', int(next_year) - year)
""" 

# print('Dir------------', dir(library_name))

# Lists

book_types = ['children', 'sci', 'fiction', 'general']
"""book_types[0] = 'poitry'
print('>>>>>>>>>>>', book_types)
print('# if list elements', len(book_types))
print('Book Types: ---------', book_types)
print('Book befor last one: ---------',book_types[-2] )
print('Slicing: ---------', book_types[1:4])
bl2 = book_types
print(': ---------', bl2, book_types)
bl3 = book_types[:]
print(': ---------', bl3, book_types)
bl2.append('religon')
print('bl3, book_types, bl2: ---------', bl3, book_types, bl2)
puplishing_year = [2001, 2000, 2002]
print('-------------',puplishing_year , book_types)
zipped_list = zip(book_types, puplishing_year)
print('--------------', zipped_list)
print(' ----------------  ' , list(zipped_list))
"""

# Tuples

lang = ('Arabic', 'English')

"""
print('----------------', lang)

new_lang = lang + ('Frenish',)
print('lang, new_lang----------------', lang, new_lang)

lang = (*lang, 'Chinese')
print('Unpack -----------', lang)
print('Unpack -----------', lang[1:2])
print('Unpack -----------', lang)
lang = list(lang)
lang.append('Japanese')
print('>>>>>>>>>>>>>>>',lang, type(lang))
print('New Lang Tuple:', tuple(lang))
"""

# Dictionaries

"""
book = {
	'name': 'Gone with wind',
	'auther': 'XXX',
	'publishing_year': 1960,
	'is_translated': True,
	'langs': ['Arabic', 'English']
}
print('Book Dict-----------',book )
print('Book Dict-----------',book.keys() )
print('Book Dict-----------',book.values() )
print('Book Dict-----------',book.items() )
print('Book Dict-----------',book.get('name', False) )
book['puplisher'] = 'Dar Azza'
print('Book Dict-----------',dir(book) )
book.update({'type': 'general', 'country': 'Sudan' })
print('Book Dict-----------',book )
"""

#Comparision
age = 13
bgender = 'male'
bname = 'Ali'
gname = 'Kawther'
ggender = 'female'

"""
if age <= 10:
	print('Ali is a chiled')
elif age <= 20:
	print('Ali is a teneger')
else:
	print('Ali is not a chiled')



if gname == 'Kawther' and ggender == 'female':
	is_girl = 'She is a Girl'
else:
	is_girl = 'She is not a Girl'
	
print('------------------------', is_girl)


is_girl = gname == 'Kawther' and ggender == 'female' and '***** She is a Girl ******' or 'She is not a girl'
print('is_girls --------------- ', is_girl )


"""

girl2 = 'Mariam'

if girl2 == 'Mariwwam' or gname == 'Kawwwwwher':
	print('girlsssssssssssssssssssssssssssssssssssssssssssss')
	
















