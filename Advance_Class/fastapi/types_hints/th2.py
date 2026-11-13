def say_hi(name: str | None = None) -> str:
    if name is None:
        return "Hi!"
    return f"Hi {name}!"

print(say_hi())  # Output: "Hi!"
print(say_hi("Tony"))  # Output: "Hi Tony!"


print()
# Class as Types
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
# person is the instance of the class Person
def greet_person(person: Person) -> str:
    return f"Hello, {person.name}!"

person = Person("Tony", 45)
print(greet_person(person))  # Output: "Hello, Tony!"