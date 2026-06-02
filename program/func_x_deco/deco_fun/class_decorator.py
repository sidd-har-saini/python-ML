def func(cls):
    cls.class_name = cls.__name__
    return cls

@func
class person:
    pass
print(person.class_name)
print(person.__class__)
print(person.__annotations__)
print(person.__base__)
print(person.__basicsize__)
print(person.__call__)
print(person.__delattr__)
print(person.__dict__)
print(person.__dictoffset__)
print(person.__dir__)
print(person.__doc__)
print(person.__eq__)