class fraction:
    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
        new_num= self.num*other.den+self.den*other.num
        new_den= self.den*other.den
        return '{}/{}'.format(new_num,new_den)

    def __sub__(self,other):
        new_num= self.num*other.den - self.den*other.num
        new_den= self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __mul__(self,other):
        new_num= self.num*other.den * self.den*other.num
        new_den= self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num

        return '{}/{}'.format(new_num,new_den)

 
frac=fraction(8,5)
fr1=fraction(3,4)
print(frac + fr1)
print(frac - fr1)
print(frac * fr1)
print(frac / fr1)
