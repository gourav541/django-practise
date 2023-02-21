cou_file = open("C:/Users/ARYA CARD/Desktop/django practise/'reading3'",'w')

'''
print(cou_file.readlines()[2]) #return the element that is stored in the other file.
'''
'''
for lines in cou_file.readlines():
    print(lines)
'''
cou_file.write("this is the another new file")
#cou_file.write("This is the new file")

cou_file.close()