import matplotlib.pyplot as plt
class Shape():
    def __init__(self, points, id=None, t=None):
        self.points = points
        self.id = id
        self.type = t
    def __repr__(self):
        return str(self.points)
class Polyline(Shape):
    def __init__(self, points, id, name=None):
        Shape.__init__(self, points, id, "polyline")
        self.name = name
        self.color = 'gray'
    def draw(self):
        l = plt.Polygon(self.points, closed=False, fill=False, edgecolor=self.color)
        plt.gca().add_line(l)


l1 = Polyline([[1,2], [5,3], [7,2]], 'l1')
l1.draw()

plt.axis('scaled')
plt.xticks([])
plt.yticks([])
plt.show()

#s = Shape([[1,1], [2,3], [3,7], [2,8]])
#print(s)
