class Animal:
    def __init__(self, wild):
        self.wild = wild

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, wild, name):
        super().__init__(wild)
        self.name = name

    def make_sound(self):
        print(f"Hi I am {self.name}. I am not {'not wild' if not self.wild else 'wild'}")
        print("I bark")


class Cat(Animal):
    def __init__(self, wild, name):
        super().__init__(wild)
        self.name = name

    def make_sound(self):
        print(f"Hi I am {self.name}. I am not {'not wild' if not self.wild else 'wild'}")
        print("I meow")


dog = Dog(False, 'Bruno')
cat = Cat(True, 'Wild Cat')

dog.make_sound()
cat.make_sound()
