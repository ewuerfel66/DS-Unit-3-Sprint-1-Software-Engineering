class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
    def add(self, c):
        print(self.r + c.r, '+ (', self.i + c.i, 'i)')
        return Complex(self.r + c.r, self.i + c.i)
    
    def subtract(self, c):
        print(self.r - c.r, '+ (', self.i - c.i, 'i)')
        return Complex(self.r - c.r, self.i - c.i)
    
    def multiply(self, c):
        print(self.r*c.r - self.i*c.i, '+ (', self.i*c.r + self.r*c.i, 'i)')
        return Complex(self.r*c.r - self.i*c.i, self.i*c.r + self.r*c.i)