import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def plot_shapes(shapes):
    plt.figure()
    for shape in shapes:
        geometry = shape.geometry
        x, y = geometry.exterior.xy
        centroid = geometry.centroid
        centroid_x, centroid_y = centroid.x, centroid.y
        plt.plot(x, y, color="black", alpha=1)
        plt.fill(x, y, alpha=0.2) 
        plt.text(centroid_x, centroid_y, shape.shape_type + "\n" + str(round(geometry.area, 2)) + "m²", fontsize=9, ha='center', va='center')
    plt.legend(title='Forma resultante')
    plt.axis('equal')
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
