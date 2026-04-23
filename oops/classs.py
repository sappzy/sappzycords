# class Vehicle:
#     def vehicle_info(self):
#         print("inside vehicle class")

# #child class
# class Car(Vehicle):
#     def car_info(self):
#         print('inside car class')

# #create object of car
# my_car=Car()
# my_car.vehicle_info()
# my_car.car_info()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hi, I'm {self.name} and I'm {self.age} years old."
#     def __repr__(self):
#          return f"Person(name={self.name!r}, age={self.age!r})"  
        
# p1 = Person("alice", 35)
# p2 = Person("bob", 30)

# print(p1)
# print(p1.greet())
# print(p2.name, p2.age)

# from abc import ABC,abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass
# class defender(Car):
#     def mileage(self):
#         print("The mileage of defender is 7 km/1")
# class fortuner(Car):
#     def mileage(self):
#         print("The mileage is 13 km/1")
# d=defender()
# d.mileage()
# i=fortuner()
# i.mileage()

# x="hello world"
# y=['12','hi',-1,9.999]
# z=('99.99','hell')
# print(len(x))
# print(len(y))
# print(len(z))
# g={'yak':3,'sparrow':4}
# print(len(g))

# x=5
# y='hi'
# print(x*3)
# print(y*2)

# encapsulation
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
# p1=Person("bob",30)
# print(p1.name)
# print(p1._Person__age)

class Shape:
    def area(self):
        print("area not defined")
class Rectangle(Shape):
    def __init__(self,l,w):
        self.w=w
    def area(self):
        print(self.l*self.w)
class Circle(Shape):
    def __init__(self,r):
       
        self.r=r
    def area(self):
        print(3.14*self.r*self.r)
class Square(Shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)

r=Rectangle(10,6)
c=Circle(5)
r=area()
c=area()

      