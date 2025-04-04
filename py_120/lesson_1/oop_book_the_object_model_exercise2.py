class Foo:

    def __init__(self, name):
        self.name = name
        # type_name = type(self).__name__
        type_name = self.__class__.__name__
        print(f'I am a {type_name} object')

foo = Foo('test')
