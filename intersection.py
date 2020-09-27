
# import Point, Polygon 
from sympy import Point, Polygon 
  
# creating points using Point() 
# p1, p2, p3, p4 = ([(0, 0), (1, 0), (5, 1), (0, 1)]) 
p5, p6 = (0, 0), (-1, -1)
  
# creating polygons using Polygon() 
poly1 = Polygon((0, 0), (1, 0), (5, 1), (0, 1))
poly2 = Polygon(p5, p6) 

parr=(Polygon((0, 0), (1, 0), (5, 1), (0, 1)),Polygon(p5, p6))
# using intersection() 
isIntersection = parr[0].intersection(parr[1]) 
  
print(len(isIntersection))
