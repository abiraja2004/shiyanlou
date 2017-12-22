class ModelMetaclass(type):
    mappings = dict()
    start = -1

    def __new__(cls, name, bases, attrs):
        if name == 'Base':
            return type.__new__(cls, name, bases, attrs)
        ModelMetaclass.mappings[name] = type.__new__(cls, name, bases, attrs)
        return ModelMetaclass.mappings[name]

    def __iter__(self):
        return self

    def __next__(self):
        ModelMetaclass.start += 1
        if ModelMetaclass.start >= len(ModelMetaclass.mappings):
            ModelMetaclass.start = -1
            raise StopIteration()
        values = list(ModelMetaclass.mappings.values())
        return values[ModelMetaclass.start]

    def __str__(self):
        values = list(ModelMetaclass.mappings.values())
        return values[ModelMetaclass.start].__name__


class Base(object, metaclass=ModelMetaclass):
    pass
