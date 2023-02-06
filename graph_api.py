# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:53:32 2021

@author: Abhishek
"""


import pandas as pd





#-----------------------------------------------------------------------------------------------------------------------------------------------------------

"""Python code to save a figure in particular dpi"""

def save_fig(fig, img_name: str,  dpi: float = 600, bbox_inches: str ='tight', pad_inches: float = 0.5, transparent: bool = True, facecolor: str ='white', edgecolor: str ='white'):
    
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    fig.tight_layout()
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.savefig( img_name,  dpi = dpi, bbox_inches=bbox_inches, pad_inches = pad_inches, transparent = transparent, facecolor=facecolor, edgecolor=edgecolor)
    
    return


#-------------------------------------------------------------------------------------------------------------------------------------------

"""Python function to plot a graph with parameter control of fig_width, fig_height, dpi, color, marker, linewidths, marker_size, x_label, y_label, label_font, graph_title, para_font"""


#





def plot_graph_multiple(ax, x, y, plot_type: str = None,  legend_label = None, graph_title : str = None,  color: str = "black", x_label: str = None, y_label: str = None, legend_loc: str = "best", marker=None, marker_size: float = 10, label_font: float = 25, linewidths: float = 3, linestyle: str ='dashed', markerfacecolor: str='black', grid_on: bool = True, limit_pad_percent: float = 0.05, grid_color: str = "k", grid_linewidth: float = 1, grid_alpha: float =0.2, para_font : float = 10):
    
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    # fig, ax = plt.subplots(1, 1, figsize=(fig_width, fig_height), dpi=dpi)
        
    # y_min = min(y) - (max(y) - min(y))*limit_pad_percent
    # y_max = max(y) + (max(y) - min(y))*limit_pad_percent       
        
    # x_min = min(x) - (max(x) - min(x))*limit_pad_percent
    # x_max = max(x) + (max(x) - min(x))*limit_pad_percent
        
    ax.autoscale(enable=True, axis='both', tight=True)
    ax.autoscale_view(tight=None, scalex=True, scaley=True)
    ax.set_xlabel(x_label, fontsize=label_font, fontweight='bold', labelpad=5)
    ax.set_ylabel(y_label, fontsize=label_font, fontweight='bold', labelpad=5)
    title = graph_title
    ax.set_title(title, fontsize=label_font*1.3, fontweight='bold', pad=5)
    # ax.tick_params(labelsize= 0.66*label_font)
    
    # ax.set_xlim(x_min, x_max)
    # ax.set_ylim(y_min, y_max)
    
    if (grid_on == True):
        
        ax.grid(color=grid_color, linestyle='-', lw =  grid_linewidth)
    
    if (plot_type.capitalize()== "Scatter"):
        ax.scatter(x, y, color = color, marker = marker, linewidths = linewidths, s=marker_size, label = legend_label)
        
    elif (plot_type.capitalize()== 'Plot'):        
        ax.plot(x, y, color, label = legend_label, linestyle=linestyle, linewidth = linewidths, marker=marker, markerfacecolor = markerfacecolor, markersize = marker_size)
        
    else:
        
        print('your input plot type is out of my knowledge. Please use any of scatter and plot in type to use this function')


    ax.tick_params(labelsize=para_font, direction='out', length=grid_linewidth, width=3, grid_color=grid_color, grid_alpha=grid_alpha)

    # plt.legend(prop={'size': label_font/2})
    # ax.legend(loc=legend_loc, frameon=False)
    
    return ax







