from new import Student

class Person(Student):
    pass

ans = Person()
print(ans.name)
print(ans.age)
print(ans.gender)


'''class MyClass:
    x = 5
    y = 6

p1 = MyClass()
print(p1.x)

p2 = MyClass()
print(p2.y)'''

'''
class Person:
 def __init__(self,name,age):
  self.name = name
  self.age =  age

p1 = Person('John',23)
print(p1.name)
print(p1.age)'''
