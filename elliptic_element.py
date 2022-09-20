import math
import copy

from utils import modular_inverse

class EllipticGroupElement:
    def __init__(self, x, y, a, b, m):
        self.x, self.y = x, y
        self.a, self.b = a, b
        self.m = m

    def __add__(self, Q):
        # if either of the point is O (point at infinity) then return the same
        if self.x == math.inf:
            return Q
        if Q.x == math.inf:
            return self

        # If P and Q are same, find slope of the tangent then find R
        if self == Q:
            slope = (3 * self.x**2 + self.a) * \
                    modular_inverse((2 * self.y) % self.m, self.m)
            xr = slope**2 - 2 * self.x
            yr = slope*(self.x - xr) - self.y

        # x's are same and y's are opposite on the elliptic curve
        elif self.x == Q.x and (self.y + Q.y) % self.m == 0:
            return EllipticGroupElement(math.inf, math.inf, self.a, self.b, self.m)
        
        else:
            slope = (self.y - Q.y) * \
                    modular_inverse((self.x - Q.x) % self.m, self.m)
            xr = slope**2 - self.x - Q.x
            yr = slope*(self.x - xr) - self.y

        xr %= self.m
        yr %= self.m
        return EllipticGroupElement(xr, yr, self.a, self.b, self.m)

    def __sub__(self, Q):
        if Q.x == math.inf:
            return self
            
        Qinv = EllipticGroupElement(Q.x, self.m - Q.y, self.a, self.b, self.m)
        return self + Qinv

    def __mul__(self, scalar : int):
        temp = copy.deepcopy(self)
        ans = copy.deepcopy(self)
        for _ in range(scalar - 1):
            ans = ans + temp
        return ans
            
    def __eq__(self, Q):
        return self.x == Q.x and self.y == Q.y
        
    def __ne__(self, Q):
        return not self == Q

    def __repr__(self):
        return f"Elem: ({self.x}, {self.y})"