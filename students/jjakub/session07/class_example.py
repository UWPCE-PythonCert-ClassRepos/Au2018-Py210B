

class Point:
    x = 1
    y = 2

Point
Point.x

p = Point()

p
p.x


class Point: # Class or type

    def __init__(self, x ,y): # Method
        self.x = x
        self.y = y

p = Point(3,4) # p = Instance 
               # (3,4) = Attributes


class Point(object):
    size = 4 #Class attribute, shared by every instance
    color= "red"
    def __init__(self, x, y): #Method
        self.x = x
        self.y = y
# The instance of the class is passed as the first parameter for every method;
# Anything assigned to a self attribute is kept in the instance name space, self is the instance

class Point3:
    size = 4
    color = "red"

    def get_color(self): # Methods defined by def are class attributes, Class attributes are accessed with self
        return self.color

p3 = Point3()
p3.get_color()

# class attributes are shared by ALL the instances of the class.
# each instance has its own copy of each instance attribute.

class C:
    x = [1,2,3] # class attribute
    def __init__(self):
        self.y = [4,5,6] # instance attribute

c1 = C()
c2 = C()

c1.x is c2.x # Each instance sees the same x
c1.y is c2.y # Each instance does not sees the same y


c1.x.append(100)

c1.x
c2.x
# Adding an item to x1.x also changed c2.x because they are the same list - 
# .x is a class attribute, c1 and c2 share the same class

c1.y.append(200)

c1.y
c2.y
# Adding an item to y1.x did not change c2.x because they are instance 
# attributes - each instance has its own versionIn [11]: C.x.append(2222)

C.x.append(2222) #Possible to access a class attribute from the class 
# namespace, will affect all instances
c1.x
c2.x


import math

class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def expand(self, factor=2):
        self.diameter = self.diameter * factor
        return None  # note that if you leave that off, it will still return None

    def area(self):
        area = (self.diameter / 2)**2 * math.pi
        return area

    def grow(self, factor=2):
        self.diameter = self.diameter * factor


# Classes are about encapsulating the data and the functions that act on that data
# – the methods are the functions that act on the data.

C = Circle(5)
C.grow(2,3) # Will return error because only two arguments were given, takes 3 since
# self is also required

c = Circle(2)
c.area()
c.diameter = 4
c.area()

# Note that after I changed the diameter attribute, when I called the area() method 
# –it used the new diameter. Simple attribute access changed the state of the object.


# Define a class
# Give the class shared (class) attributes
# Add an initializer to set up it’s initial state
# Add methods to manipulate that state.
# Add methods that return the results of calculations of the current state


# Python is not a true object oriented programming language,
# as it does nto allow full encapsulation and does not require classes


class Circle:
    color = "red"

class NewCircle(Circle): # NewCircle is the subclass, has all the same attributes as the super class
    color = "blue" # In this case the attribute of the subclass is overwritten, the self instance has a new attribute

nc = NewCircle
print(nc.color)


# A method is an attribute


class Circle:
    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = self.diameter * math.sqrt(2)


# All instances will have a new method
c = NewCircle()
c.diameter = 4
c.grow()