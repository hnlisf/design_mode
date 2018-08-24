#coding:utf-8
"""
Bridge  桥接

意图：
 将抽象部分与它的实现部分分离，使它们都可以独立地变化。
 适用性：
 你不希望在抽象和它的实现部分之间有一个固定的绑定关系。例如这种情况可能是因为，在程序运行时刻实现部分应可以被选择或者切换。
 类的抽象以及它的实现都应该可以通过生成子类的方法加以扩充。这时Bridge 模式使你可以对不同的抽象接口和实现部分进行组合，并分别对它们进行扩充。
 对一个抽象的实现部分的修改应对客户不产生影响，即客户的代码不必重新编译。
 （C++）你想对客户完全隐藏抽象的实现部分。在C++中，类的表示在类接口中是可见的。
 有许多类要生成。这样一种类层次结构说明你必须将一个对象分解成两个部分。Rumbaugh 称这种类层次结构为“嵌套的普化”（nested generalizations ）。
 你想在多个对象间共享实现（可能使用引用计数），但同时要求客户并不知道这一点。一个简单的例子便是Coplien 的String 类[ Cop92 ]，在这个类中多个对象可以共享同一个字符串表示（StringRep）。
"""

class DrawingAPI1:
    def draw_circle(self,x,y,radius):
        print("API1.circle at {}:{},radius {}".format(x,y,radius))

class DrawingAPI2:
    def draw_circle(self,x,y,radius):
        print("API2.circle at {}:{},radius {}".format(x,y,radius))

class CircleShape:
    def __init__(self,x,y,radius,drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x,self._y,self._radius)

    def scale(self,pct):
        self._radius *= pct

def main():
    shapes = (
        CircleShape(1,2,3,DrawingAPI1()),
        CircleShape(5,7,11,DrawingAPI2())
    )
    for shape in shapes:
        shape.scale(2.5)
        shape.draw()

if __name__ == '__main__':
    main()