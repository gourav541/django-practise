# countries = list(('India',True,'America','South Korea'))
# countries[2]= 'Bangladesh'

# print(countries)
# print(type(countries)) #tell the type of data type
# print(type(countries[1])) #tell the type of data type
# print(countries[-1]) #reads from last element
# print(countries[2][0]) #first index gives the name of element in the list and next index will tell the indexing for particular element.
# print(countries[1:3])
# print(len(countries))

'''list1 = [34,54,23,12]
list2 = ['banana','oranges','apple','grapes']
list3 = list1.copy()
list1.append(45)
list1.extend(list2)  #extend keyword helps in adding the another list in the existing list.
print(list1)
print(list3)
list1.pop()
print(list1)
list1.remove('banana')
print(list1)'''

list1 = [34,54,23,12]
list2 = ['banana','oranges','apple','grapes']
del list1[2]
print(list1)

