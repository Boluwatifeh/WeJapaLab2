# Use this playground to experiment with list methods, using Test Run
numbers = [43, 6, 7 , 12, 34, 23, 70, 59]

cities = ['Ikorodu', 'Yaba', 'Oshodi', 'Mushin']

# sorted() takes in the list and sorts the items from the largest to the lowest
print('The sorted array in ascending order: {}'.format(sorted(numbers)))

# len() returns the number of elements available in the string
print('The length of the list is: {}'.format(len(numbers)))

# max() returns the highest value present in the List
print('The highest number is: {}'.format(max(numbers)))

# min() returns the highest value present in the List
print('The lowest number is: {}'.format(min(numbers)))

# append() adds an element to the end of a List
cities.append('Ikoyi')
print('List of some places in Lagos: {}'.format(cities))

# join() takes in a list and returns a new list with a seperator string
print("\n".join(cities)) 
