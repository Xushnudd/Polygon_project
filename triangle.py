from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        if self.a <= 0 or self.b <= 0:
            return False
        return True
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.a == self.b == self.c:
            return 'Teng tomonli'
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return 'Teng yonli'
        else:
            return 'Turli tomonli'
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a + self.b + self.c

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        s = (self.a + self.b + self.c)/2
        return round((s*(s-self.a) * (s-self.b) * (s-self.c)) ** 0.5, 2)
t = Triangle(12, 23, 34)
print(t.get_type(), t.perimeter(), t.area())

