class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2*(self.height + self.width)

    def get_diagonal(self):
        return (self.width ** 2 + self.height**2) ** .5

    def get_picture(self):
        # todo test if too large
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        # todo height print width
        pic = ''
        for n in range(0, self.height):
            for r in range(0, self.width):
                pic += '*'
            pic += '\n'
        return pic

    def get_amount_inside(self, shape):
        area_guest = shape.get_area()
        area_home = self.get_area()
        i = 0
        while area_home >= area_guest:
            area_home = area_home - area_guest
            i = i + 1
        return i

    def __str__(self):
        return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'


