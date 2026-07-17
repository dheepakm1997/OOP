class Person:
    name = "John"
    age = 25

    def print_age(self):
        print("Called!!" ,self.age)

    def set_new_age(self,new_age):
        self.age =new_age
        print("Age Reset to:",self.age)

john = Person()
john_b = Person()



john.set_new_age(64)

