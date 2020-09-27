# limited to translation
# ans is [(0,-2),(-1,-2),(-1,2),(0,4),(2,4),(2,2)]
# from sympy import Point, Polygon 
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt
from descartes import PolygonPatch
# from sympy import Point, Polygon
import math
from shapely.ops import cascaded_union
import geopandas as gpd

obstacle=[(0,0),(0,2),(1,2)]
obstaclePolygon=gpd.GeoSeries(Polygon([(0,0),(0,2),(1,2)]))
#start position
robot=[(0,0),(0,2),(1,2)]
robotPolygon=obstaclePolygon
u=robotPolygon

poly1 = obstaclePolygon['geometry']; poly2 = robotPolygon['geometry']
mergedpoly = poly1.union(poly2)
mergedpoly.plot()

if __name__ == "__main__":
    dist=1
    for angle in range(36):
        print(angle*10)
        robotPolygon=Polygon((0,0),(0,2),(1,2))
        s=dist*math.sin(angle*10)
        c=dist*math.cos(angle*10)
        isIntersection=obstaclePolygon.intersection(robotPolygon)
        while len(isIntersection)>1:
            robotPolygon=robotPolygon.translate(s,c)
            isIntersection=(obstaclePolygon).intersection(robotPolygon)
            pass
        u=u.union(robotPolygon)
        pass
    pass