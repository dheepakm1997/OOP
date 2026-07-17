class Person():
    ...


john = Person()

john.name = "John"
john.age = 30

print(john.name,john.age)
john.name ="John!"

print(john.name)

class House:
    bedrooms = 4
    doors = 16

my_house = House()
my_house_v2 = House()
my_house.doors += 1
my_house.bedrooms -= 1


print(dir(my_house))
print(my_house.doors,my_house_v2.doors)
print(my_house,my_house_v2)
print(my_house.bedrooms,my_house_v2.bedrooms)
