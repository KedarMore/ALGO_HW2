import shapely.geometry as sg
import shapely.ops as so
import matplotlib.pyplot as plt
import shapely.affinity as sa

#constructing the first rect as a polygon
r1 = sg.Polygon([(0,0),(0,1),(1,1),(1,0),(0,0)])

#a shortcut for constructing a rectangular polygon
r2 = sg.box(0.5,0.5,1.5,1.5)

#cascaded union can work on a list of shapes
new_shape = so.cascaded_union([r1,r2])

r1=sa.translate(r1,1,1)

#exterior coordinates split into two arrays, xs and ys
# which is how matplotlib will need for plotting
xs, ys = r1.exterior.xy

#plot it
fig, axs = plt.subplots()
axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')
plt.show() #if not interactive
