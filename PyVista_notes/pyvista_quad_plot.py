import numpy as np
import pyvista as pv

# https://docs.pyvista.org/examples/00-load/create-poly.html#sphx-glr-examples-00-load-create-poly-py

# mesh points
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [2, 0, 0],
                     [3, 1, 0]])

# mesh faces
# the 4 indicates how many nodes are present
# other numbers are indicies in the vertices array
faces = np.hstack([[4, 0, 1, 2, 3],
                   [4, 1, 4, 5, 2]])   

# define a surface or as PyVista calls it a 'mesh' object
surf = pv.PolyData(vertices, faces)
# define nodal/point data
surf.point_arrays['point1'] = np.arange(surf.n_points)
# define cell/element data
surf.cell_arrays['cell1']   = np.arange(surf.n_cells)

# parameters for the colorbar
sargs = dict(height=0.25, vertical=True, position_x=0.85, position_y=0.05)

# create the plotter
p = pv.Plotter()
# show the axes widget 
p.show_axes()
# add the mesh to the plotter and tell it which field to display
# and set the arguments for the scalar bar
p.add_mesh(surf,scalars='point1',scalar_bar_args=sargs)
# specify the view
p.view_xy()
# plot and take a screenshot
p.show(screenshot='pyvistatest.png')

#p.camera_position = [0.0,0.0,1.5]
#p.set_viewup([1.0,1.0,0.0])

# can also plot using
#surf.plot(scalars='cell1', cpos=[0.0, 0.0, 1.5],
#          screenshot='pyvistatest.png')


