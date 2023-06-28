from domain.models import Person

def get_person_by_name(name):
    return Person(name, 20)

def get_person_by_age(age):
    if age <= 0:
        return Person("I'm not born yet", 0)

    return Person("John", age)