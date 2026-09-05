class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def get_a(self):
        return self.a   
    def get_b(self):
        return self.b  
    def get_c(self):
        return self.c   
    def get_d(self):
        return self.d   
    def get_e(self):
        return self.e  
    def get_f(self):
        return self.f

    def isSolvable(self):
        if ((self.a * self.d) - (self.b * self.c)) != 0:
            return True
        
    def getX(self):
        if self.isSolvable() == True:
            return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c) 
        
    
    def getY(self):
        if self.isSolvable() == True:
            return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c) 


# l1 = LinearEquation(1, 2, 3, 4, 5, 6)
# print(l1.isSolvable())
# print(l1.getX())
# print(l1.getY())
# print(l1.get_a())
# print(l1.get_b())
# print(l1.get_c())
# print(l1.get_d())
# print(l1.get_e())
# print(l1.get_f())

l2 = LinearEquation(1, 2, 2, 4, 5, 6)
print(l2.isSolvable())
# print(l2.getX())
# print(l2.getY())
print(l2.get_a())
print(l2.get_b())
print(l2.get_c())
print(l2.get_d())
print(l2.get_e())
print(l2.get_f())
