# UTILS FOR RADAR CHART
# ////////////////////////////////////
def set_visible(
    ax,
    spine_bottom=False,
    spine_top=False,
    spine_left=False,
    spine_right=False,
    grid=False,
    tick=False,
    label=False,
):
    ax.spines["bottom"].set_visible(spine_bottom)
    ax.spines["top"].set_visible(spine_top)
    ax.spines["left"].set_visible(spine_left)
    ax.spines["right"].set_visible(spine_right)
    ax.grid(grid)
    ax.tick_params(
        bottom=tick,
        top=tick,
        left=tick,
        right=tick,
        labelbottom=label,
        labeltop=label,
        labelleft=label,
        labelright=label,
    )
