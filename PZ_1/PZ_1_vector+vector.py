class Dot :
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Vector:
    def __init__(self,dot1,dot2):
        if isinstance(dot1,Dot) and isinstance(dot2,Dot):
            self.dot1 = dot1
            self.dot2 = dot2
            self.x = dot2.x-dot1.x
            self.y = dot2.y-dot1.y
        else:
            print('-vaib')
    def  summ(self,vec):
        if isinstance(vec,Vector):
            print ('Координаты вектора №1 (', vec.x, vec.y,').', 'Координаты вектора №2 (', self.x, self.y,')')
            new_x = self.x + vec.x
            new_y = self.y + vec.y
            return Vector (Dot(0, 0), Dot(new_x, new_y))
a = Vector(Dot(0,0), Dot(5,5))
b = Vector(Dot(5,5), Dot(10,10))
c = a.summ(b)
print('Координаты вектора №3 (', c.x, c.y, ')')