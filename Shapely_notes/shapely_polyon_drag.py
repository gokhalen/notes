# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 12:02:04 2021

@author: aa
"""
import matplotlib.pyplot as plt
from shapely.geometry import Polygon,Point
from descartes.patch import PolygonPatch

import numpy as np

GREEN = '#339933'
RED = '#ff3333'
BLACK = '#000000'


def drag_polygon(polygon,drag_vector):
    '''
    drags 'polygon' according to magnitude and direction in drag_vector
    
    polygon -> polygon to be dragged
    drag_vector -> vector to drag polygon
    every point x in the polygon moves to x+drag_vector
    
    returns a new polygon containing a set of points inside the polygon
    as it is dragged continuously along drag_vector
    
    implementation: 
        1) translate every edge of 'polygon' by 'drag_vector'
        2) for each pair of edge and translated edge
           create a polygon
        3) take the union of all polygons created in step 2
        4) take the union of the result of step 3 and 'polygon'
        5) return the union created in step 4   
    
    USE AT YOUR OWN RISK
    
    '''
    
    # create coordinates of final position of polygon
    # by adding drag_vector to every point
    
    drag_vector = np.asarray(drag_vector).reshape(1,2)
    exterior_coords=np.asarray(polygon.exterior.coords)
    
    # broadcasting magic
    shifted_exterior_coords=exterior_coords + drag_vector 
    
    npoints = len(exterior_coords)
    polylist = []
     
    # create polygons from each original edge
    # and its translated final position
    
    # loop over each edge in 'polygon'
    for ipoint in range(npoints-1):
        # points of the initial polygon
        p1       = exterior_coords[ipoint]
        p2       = exterior_coords[ipoint+1]
        # their final locations
        p1_shift = shifted_exterior_coords[ipoint]
        p2_shift = shifted_exterior_coords[ipoint+1]
        
        # at this point we know initial and final coords of current edge
        # use this information to create polygon by 
        # specifying vertices in the correct order
        # save it in polylist
        polylist.append(Polygon([p1,p2,p2_shift,p1_shift]))

    # initiaize union of all polygons
    union_poly = polygon
    
    # take the union with all polygons in polylist
    for pp in polylist:
        union_poly = union_poly.union(pp)
    
    return union_poly

# points defining polygon to be dragged
poly_points  = np.asarray([(0.0,0.0),(3.0,3.0),(0.0,5.0),(-5,5),(1,3)])
# specifies amount and magnitude of drag
drag_vector  = np.asarray((2.0,2.0))


fig,axes = plt.subplots(nrows=1,ncols=2)

poly_initial = Polygon(poly_points)
patch1 = PolygonPatch(poly_initial, facecolor=RED, edgecolor=BLACK, alpha=0.5, zorder=2)
axes[0].add_patch(patch1)

# shifted points
shifted_points = poly_points + drag_vector.reshape(1,2)
poly_shift     = Polygon(shifted_points)
patch2         = PolygonPatch(poly_shift, facecolor=RED, edgecolor=BLACK, alpha=0.5, zorder=2)
axes[0].add_patch(patch2) 

# centroid 
xcen = poly_initial.centroid.x
ycen = poly_initial.centroid.y

axes[0].arrow(xcen,ycen,drag_vector[0],drag_vector[1],width=0.1)

poly_dragged = drag_polygon(polygon=poly_initial,
                            drag_vector=drag_vector
                            )

# plot poly_dragged and initial and shifted polygon borders
patch3 = PolygonPatch(poly_dragged, facecolor=GREEN, edgecolor=BLACK, alpha=0.5, zorder=2)
_xx,_yy = zip(*list(poly_initial.exterior.coords))
axes[1].plot(_xx,_yy,color='black')
_xx,_yy = zip(*list(poly_shift.exterior.coords))
axes[1].plot(_xx,_yy,color='black')


axes[1].add_patch(patch3)

# get limits of axes so that all polygons can be seen
xmin = np.inf
xmax = -np.inf
ymin = np.inf
ymax = -np.inf
polygonlist = [poly_initial,poly_shift]

for pp in polygonlist:
    _xmin,_ymin,_xmax,_ymax = pp.bounds
    
    xmin = np.minimum(xmin,_xmin)
    ymin = np.minimum(ymin,_ymin)
    xmax = np.maximum(xmax,_xmax)
    ymax = np.maximum(ymax,_ymax)

for ax in axes:
    ax.set_xlim([xmin-1.0,xmax+1.0])
    ax.set_ylim([ymin-1.0,ymax+1.0])
    ax.set_aspect('equal') 

axes[0].set_title('initial and final polygons')
axes[1].set_title('dragged polygon (green)')

plt.show()   

