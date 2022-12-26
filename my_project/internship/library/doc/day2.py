import functools

# Looping


num_list = [1, 2, 3, 4, 5, 6]
"""
print('num_list>>>>>>>>>>>>>>>',num_list )
for r in num_list:
	print('>>>>>>>>>>>>>>>', r)
	

num_list = [r for r in range(1, 7)]
for r in range(1, 7):
	num_list.append(r)
print('>>>>>>>>>>>>', num_list)

"""
num_list = [r for r in range(1, 7)]
# print('>>>>>>>>>>>>>>> sum', num_list)

book_publishing_years = [
	(2000, ['1Q84', 'Gone with wind', 'To kill a mockingbird']), 
	
	(2002, ['Anna Karneen', 'Ware and peace']), 
	
	(2001, ['wuthering heights', 'Harry Poter'])
	]
#print('>>>>>>>>>>>>>>>>>>>>>', book_publishing_years)
	
"""
	for year in book_publishing_years:
	
	#if isinstance(year[1], list):
	#for book in year[1]:
	print('List >>>>>>>>>>>>', year)
	#else:
		#for book in year[1].keys():
			#print('Dict >>>>>>>>>>>>', book)
	
	#print('>>>>>>>>', year[1:][1])	

for year in book_publishing_years:
	#print('Year ---', year)
	for book in year[1]:
		#if book == 'Gone with wind':
			#break
		if book == 'Gone with wind':
			continue
		
		print('Book --- ', book)

for year in book_publishing_years:
	pass
"""

# Functions

"""
sums = 77
print('sums ----- first', sums)
def sum_numbers(num1, num2):
	''' 
		Calculate sumation of two numbers.
	
	'''
	total = 3
	sums = num1 + num2
	print('sums inside function >>>>>>>>>>>>>>>', sums, total)
	return sums 
	
res = sum_numbers(6, 8)

#y = 5

for num in num_list:
	#print('num ---- ',  num )
	if num > 7:
		y = num * 2
	 
print('--------------',y)

"""
"""
res , res2 = sum_numbers(1 , 2)
print('calling func >>>>>>>>>>>>>>>>>', res)
"""

# Anonymous Functions

#cube = lambda num: num * num * num
#print('lambda with var >>>>>>>>>>>>', cube(3))
#print('lambda without var >>>>>>>>>>>>>>>>>', (lambda num, num2 : num * num2)(2, 5))
"""
cube_list = [] 
for num in num_list:
	cube_list.append(cube(num))
print('cube_list', cube_list)
# map
num_list_cube = list(map(lambda num: num * num * num, num_list))
print('>>>>>>>>>>>>>', num_list_cube)
"""
# filter
even_nums = filter(lambda num: num % 2 == 0, num_list)
print('>>>>>>>>>>>>>', list(even_nums))

# reduce
min_num = functools.reduce(lambda a, b: a if a < b else b, num_list)
print('>>>>>>>>>>>>>>>>>>', min_num)
""" """

