from __future__ import division
import numpy
from matplotlib import pyplot
from matplotlib import colors


def equalize_cmap(data, bins, cmap='viridis', name="EqualizedCM"):
    try:
        cmap = pyplot.get_cmap(cmap)
    except Exception():
        cmap = cmap
    data = data.ravel()
    data = data[~numpy.isnan(data)]
    hist = numpy.histogram(data, bins, density=False)[0]
    cdf = numpy.cumsum(hist)/numpy.float(len(data))
    indices = numpy.linspace(0, 1, bins)
    new_indices = numpy.interp(indices, cdf, indices)
    cmap_list = cmap(indices)[:, :3]
    # remap the color table
    color_dict = {'red': [], 'green': [], 'blue': []}
    for i, new_index in enumerate(new_indices):
        r, g, b = cmap_list[i]
        color_dict['red'].append([new_index, r, r])
        color_dict['green'].append([new_index, g, g])
        color_dict['blue'].append([new_index, b, b])
    return colors.LinearSegmentedColormap(name, color_dict)
