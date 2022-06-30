# UTILS FOR RADAR CHART
# ////////////////////////////////////
def set_visible(ax, spine_bottom=False, spine_top=False, spine_left=False, spine_right=False,
                grid=False, tick=False, label=False):
    """
    It sets the visibility of the spines, grid, ticks, and labels of an axis

    :param ax: the axis to modify
    :param spine_bottom: whether to show the bottom spine, defaults to False (optional)
    :param spine_top: True/False, defaults to False (optional)
    :param spine_left: whether to draw the left spine, defaults to False (optional)
    :param spine_right: whether to draw the right spine, defaults to False (optional)
    :param grid: whether to show the grid, defaults to False (optional)
    :param tick: whether to show tick marks, defaults to False (optional)
    :param label: whether to show the axis labels, defaults to False (optional)
    """
    ax.spines['bottom'].set_visible(spine_bottom)
    ax.spines['top'].set_visible(spine_top)
    ax.spines['left'].set_visible(spine_left)
    ax.spines['right'].set_visible(spine_right)
    ax.grid(grid)
    ax.tick_params(bottom=tick, top=tick, left=tick, right=tick,
                   labelbottom=label, labeltop=label, labelleft=label, labelright=label)
