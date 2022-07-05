import functools as ft

# <join> function 
names: tuple = ('Rocky', 'Docky', 'Pocky')

namestr = '/'.join(names) # join strings from iterable ...
# print(namestr)

# <zip> function
professors: tuple = ('Dr. Jerome', 'Dr. Arron', 'Dr. Calt')
subjects: tuple = ('Math', 'Physics', 'English')

prof_subs: tuple = tuple(zip(professors, subjects, names)) 
# combines value pairs as 0-0-0, 1-1-1, 2-2-2 from multiple iterables ...

# print(prof_subs)

# <reduce> function (functools)
numbers: list = [10, 20, 30, 40, 50]
total_of_iter: int = ft.reduce(lambda x, y: x + y, numbers) 
# takes x, y sequentially as all numbers of iterable and through lambda make the desired operation with them ...
# print(total_of_iter)

# <map> function
taxed: tuple = tuple(map(lambda x: x * 1.25, numbers)) 
# applies certain operation to each element of iterable ...
# print(taxed) 

# <filter> function

filtered: tuple = tuple(filter(lambda x: x > 25, numbers)) 
# applies a certain filter to each element of iterable and returns only filtered iterables ...
print(filtered)