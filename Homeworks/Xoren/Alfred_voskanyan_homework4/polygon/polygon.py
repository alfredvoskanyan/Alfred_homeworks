class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = list()

    def input_sides(self):
        while True:
            self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
            if max(self.sides) < sum(self.sides)/2:
                break
            print("It's impossible to create a polygon, try again")


    def disp_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def find_area(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


class Right_Triangle(Triangle):
    def __init__(self):
        Triangle.__init__(self)


    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n-1)]
        self.sides.append((self.sides[0] ** 2 + self.sides[1] ** 2) ** 0.5)

#p = Polygon(3)
#p.input_sides()
#p.disp_sides()

#t = Triangle()
#t.input_sides()
#t.disp_sides()

r = Right_Triangle()
r.input_sides()
r.disp_sides()
r.find_area()