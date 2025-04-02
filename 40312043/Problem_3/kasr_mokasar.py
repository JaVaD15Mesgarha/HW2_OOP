import math

class Fraction :
    def __init__(self , numerator=0 , denominator=1) :
        self.numerator = numerator
        self.denominator = denominator 

    def simplify (self) :
        gcd = gcd(self.numerator , self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __str__ (self) : 
        return f"{self.numerator} / {self.denominator}"
    
    def __call__ (self) :
        return self.numerator / self.denominator
    
    def set_value (self , integer) :
        if isinstance(integer , int) :
            self.numerator = integer
            self.denominator = 1
        elif isinstance(integer , float) :
            natural = int(integer)
            self.numerator = (pow(range(integer) - range(natural) - 1) , 10) *  integer
            self.denominator = pow((range(integer) - range(natural) - 1) , 10)
        else :
            raise TypeError("value must be number")
        self.simplify()
        
    def __mul__ (self , another) :
        if isinstance(another , Fraction) :
            new_numerator = self.numerator * another.numerator
            new_denominator = self.denominator * another.denominator 
            return Fraction(new_numerator , new_denominator)
        if isinstance(another , (int,float)) :
            another = Fraction(another)
            new_numerator = self.numerator * another.numerator
            new_denominator = self.denominator * another.denominator 
            return Fraction(new_numerator , new_denominator)
        
    def __add__ (self, another) :
        if isinstance(another ,Fraction) :
            new_numerator = self.numerator * another.denominator + another.numerator * self.deminator
            new_demanitor = self.demanitor * another.denominator
        elif isinstance(another , (int , float)) :
            another = Fraction(another)
            new_numerator = self.numerator * another.denominator + another.numerator * self.deminator
            new_demanitor = self.demanitor * another.denominator
        else :
            TypeError("value must be number")
        return Fraction(new_numerator , new_demanitor)
        
    def __sub__(self , another) :
        if isinstance(another ,Fraction) :
            new_numerator = self.numerator * another.denominator - another.numerator * self.deminator
            new_demanitor = self.demanitor * another.denominator
        elif isinstance(another , (int , float)) :
            another = Fraction(another)
            new_numerator = self.numerator * another.denominator - another.numerator * self.deminator
            new_demanitor = self.demanitor * another.denominator
        else :
            TypeError("value must be number")
        return Fraction(new_numerator , new_demanitor)
    
    def __truediv__(self , another):
        if isinstance(another , Fraction):
            new_numerator = self.numerator * another.denominator
            new_denominator = self.denominator * another.numerator
            return Fraction(new_numerator , new_denominator)
        elif isinstance(another , (int , float)) :
            another = Fraction(another)
            new_numerator = self.numerator * another.denominator
            new_denominator = self.denominator * another.numerator
            return Fraction(new_numerator , new_denominator)
        else :
            TypeError("value must be number")
    
    def __gt__(self, other):
        return self() > other()
    
    def __ge__(self, other):
        return self() >= other()
    
    def __lt__(self, other):
        return self() < other()
    
    def __le__(self, other):
        return self() <= other()
    
    def __ne__(self, other):
        return self() != other()
    
    def __gt__(self, other):
        return self() > other()
    
    def __ge__(self, other):
        return self() >= other()

    def __eq__(self, other):
        return self() == other()

def main() :


if __name__ == '__main__' :
    main()