
class Rodzhers(object):
    def __init__(self, x_min, y_min, x_max, y_max, x1, y1, x2, y2):
        self.INSIDE = 0  # 0000
        self.LEFT = 1    # 0001
        self.RIGHT = 2   # 0010
        self.BOTTOM = 4  # 0100
        self.TOP = 8     # 1000
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2



    def compute_outcode(self, x, y):
            code =self. INSIDE
            if x <self. x_min:
                code |= self.LEFT
            elif x > self.x_max:
                code |= self.RIGHT
            if y < self.y_min:
                code |= self.BOTTOM
            elif y > self.y_max:
                code |= self.TOP
            return code


    def cohen_sutherland_clipping(self):

        self.outcode1 = self.compute_outcode(self.x1, self.y1)
        self.outcode2 = self.compute_outcode(self.x2, self.y2)
        accept = False
        while True:
            if not (self.outcode1 | self.outcode2):
                accept = True
                break
            elif self.outcode1 & self.outcode2:
                break
            else:
                x = 0
                y = 0
                outcode_out = self.outcode1 if self.outcode1 > self.outcode2 else self.outcode2

                if outcode_out & self.TOP:
                    x = self.x1 + (self.x2 - self.x1) * (self.y_max - self.y1) / (self.y2 - self.y1)
                    y = self.y_max
                elif outcode_out & self.BOTTOM:
                    x = self.x1 + (self.x2 - self.x1) * (self.y_min - self.y1) / (self.y2 - self.y1)
                    y = self.y_min
                elif outcode_out & self.RIGHT:
                    y = self.y1 + (self.y2 - self.y1) * (self.x_max - self.x1) / (self.x2 - self.x1)
                    x = self.x_max
                elif outcode_out & self.LEFT:
                    y = self.y1 + (self.y2 - self.y1) * (self.x_min - self.x1) / (self.x2 - self.x1)
                    x = self.x_min

                if outcode_out == self.outcode1:
                    self.x1, self.y1 = x, y
                    self.outcode1 = self.compute_outcode(self.x1, self.y1)
                else:
                    self.x2, self.y2 = x, y
                    self.outcode2 = self.compute_outcode(self.x2, self.y2)

        if accept:
            print("Линия от ({}, {}) до ({}, {}) отсечена и видима.".format(self.x1, self.y1, self.x2, self.y2))
        else:
            print("Линия от ({}, {}) до ({}, {}) полностью невидима.".format(self.x1, self.y1, self.x2, self.y2))


test = Rodzhers(50, 50, 100, 100, 25, 30, 120, 80)
test.cohen_sutherland_clipping()