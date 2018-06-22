# Create a class Animal as a base class and define method animal_attribute 
#Create another class Tiger which is inheriting Animal and access the base class method.

class animal:
  def animal_attribute(self):
    print("animal class call")
 
class tiger(animal):
  pass
t=tiger()
t.animal_attribute()


#output of code

class A:
  def f(self):
    return self.g()
  def g(self):
    return 'A'
class B(A):
  def g(self):
    return 'B'


a=A()
b=B()
print (a.f(), b.f())
print (a.g(), b.g())



#Create a class Cop. Initialize its name, age , work experience and designation.
class cop:
  def add(self,name,age,work,designation):
    self.name=name
    self.age=age
    self.work=work
    self.designation=designation
  def display(self):
    print("name:",self.name)
    print("age:",self.age)
    print("work exp:",self.work)
    print("designation:",self.designation)

  def update(self,name,age,work,designation):
    self.name=name
    self.age=age
    self.work=work
    self.designation=designation
class mission(cop):
  def add_mission_details(self,mission):
    self.mission=mission
    print(self.mission)

m1=mission()
m1.add_mission_details("abc")
m1.add("himanshu",20,2,"ssm")
m1.display()
m1.update("gurry",23,5,"safaiwala")
m1.display()

#Create a class Shape.Initialize it with length and breadth Create the method Area

class shape:
  def __init__(self,l,b):
    self.length=l
    self.breadth=b
  def area(self):
    self.area=self.length*self.breadth
    print(self.area)

class rectangle(shape):
  pass
class square(shape):
  pass
s=square(4,6)
r=rectangle(6,8)
s.area()
r.area()