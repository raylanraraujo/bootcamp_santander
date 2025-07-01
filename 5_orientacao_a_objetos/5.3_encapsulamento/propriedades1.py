class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property # para retornar valor preciso ter o property anotado
    def x(self):
        return self._x or 0

    @x.setter # para que seja possivel alterar o valor e fazer uma atribuicao para a propriedade é preciso fazer um setter.
    def x(self, value):
        self._x += value
    #O SETTER recebe dois valores. O primeiro valor que recebe é o objeto (ou a instância) - que nesse caso é o foo. O segundo valor é o que se passa depois do igual. que no exemplo seria o 10 pois temos foo.x = 10

    @x.deleter
    def x(self):
        self._x = -1    

foo =Foo(10)
print(foo.x) #com property eu acesso o m;etodo com uma sintaxe de atributo e nao de método.
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)