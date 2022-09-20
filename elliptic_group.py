import math
from elliptic_element import EllipticGroupElement

class EllipticGroup:
    def __init__(self, a, b, m):
        self.a, self.b = a, b
        # check for singularity of the elliptic curve
        if (4 * self.a**3 + 27 * self.b**2) % m == 0:
            raise ValueError(f"{self.a} and {self.b} will result in a singular elliptic curve")

        self.m = m
    
        # creating group elements
        self.elems = [EllipticGroupElement(math.inf, math.inf, self.a, self.b, self.m)]
        for i in range(1, self.m):
            temp = (i ** 3 + self.a * i + self.b) % self.m
            # loop through all possible values for y
            for j in range(1, self.m):
                # if j leaves a quadratic residue append the (i, j) pair to the elem
                if (j * j) % self.m == temp:
                    self.elems.append(EllipticGroupElement(i, j, self.a, self.b, self.m))

        # check for closure property of group, if not make the elems empty
        for i in self.elems:
            for j in self.elems:
                if i + j not in self.elems:
                    self.elems = []

    def __len__(self):
        return len(self.elems)

    def __repr__(self):
        return (
            f"a = {self.a}, b = {self.b}, m = {self.m}\n" 
            f"Group Elements: \n{repr(self.elems)}"
        )