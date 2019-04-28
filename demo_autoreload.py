class MyClass:

    def __init__(self, a=10):
        self.a = a

    def square(self):
        print('compute square')
        return self.a*2

    # def cube(self):
    #     print('compute cube')
    #     return self.a*self.a*self.a
