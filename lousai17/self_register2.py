class Meta(type):
    _children = []

    def __new__(cls, name, bases, attrs):
        class_temp = type.__new__(cls, name, bases, attrs)
        if name != 'Base':
            cls._children.append(class_temp)
        return class_temp

    def __iter__(cls):
        return iter(cls._children)
    def __repr__(cls):
        return cls.__name__


class Base(metaclass=Meta):
    def __init__(self):
        super(self).__init__()

class Course(Base):
    pass
class Lab(Base):
    pass

if __name__ == '__main__':
    for cls in Base:
        print(cls)

    print(Course in list(Base))
    print(Lab in list(Base))