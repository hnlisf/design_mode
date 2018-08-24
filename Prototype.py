# coding:utf-8
"""
原型：prototype
意图：
用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
适用性：
当要实例化的类是在运行时刻指定时，例如，通过动态装载；或者为了避免创建一个与产品类层次平行的工厂类层次时；或者当一个类的实例只能有几个不同状态组合中的一种时。建立相应数目的原型并克隆它们可能比每次用合适的状态手工实例化该类更方便一些。
"""
import copy

class Prototyper:
    def __init__(self):
        self._objects = {}

    def register_object(self,name,obj):
        self._objects[name]=obj

    def unregister_object(self,name):
        del self._objects[name]

    def clone(self,name,**attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

def main():
    class A :
        def __str__(self):
            return "I am A"

    a = A()
    prototype = Prototyper()
    prototype.register_object('a',a)
    b = prototype.clone('a',a=1,b=2,c=3)

    print(a)
    print(b.a,b.b,b.c)

if __name__ == '__main__':
    main()
