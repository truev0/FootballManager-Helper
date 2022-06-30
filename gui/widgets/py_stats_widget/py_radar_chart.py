# IMPORT OTHER PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import textwrap

# IMPORT PROCESSING, CHART & CLUSTERING MODULES
# ///////////////////////////////////////////////////////////////
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon, Wedge

# IMPORT UTILS
# ///////////////////////////////////////////////////////////////
from . py_radar_utils import set_visible

__all__ = ['Radar']


# A radar object can be created with a name, a maximum range, and a maximum bearing, and it can be asked to scan for a
# target.
class Radar:
    def __init__(
            self,
            params,
            min_range,
            max_range,
            round_int=None,
            num_rings=4,
            ring_width=1,
            center_circle_radius=1,
    ):
        """
        It takes in a list of parameters, a list of minimum values, a list of maximum values, and a list of booleans
        indicating whether the parameter should be rounded to the nearest integer.

        It then calculates the number of rings, the width of each ring, the radius of the center circle, and the number of
        labels.

        It then calculates the rotation angles for each label, and flips the rotation if the label is in the lower half of
        the plot.

        It also calculates the sine and cosine of the rotation angles.

        :param params: the list of parameters to be plotted
        :param min_range: The minimum value for each parameter
        :param max_range: The maximum value of the parameter
        :param round_int: If True, the parameter will be rounded to the nearest integer
        :param num_rings: The number of rings in the radar chart, defaults to 4 (optional)
        :param ring_width: The width of each ring, defaults to 1 (optional)
        :param center_circle_radius: The radius of the center circle, defaults to 1 (optional)
        """
        self.params = np.asarray(params)
        self.min_range = np.asarray(min_range)
        self.max_range = np.asarray(max_range)
        np.place(self.min_range, self.min_range == 0, 0.00001)
        np.place(self.max_range, self.max_range == 0, 0.00002)
        if round_int is None:
            self.round_int = np.array([False] * self.params.size)
        else:
            self.round_int = np.asarray(round_int)
        self.ring_width = ring_width
        self.center_circle_radius = center_circle_radius
        self.num_rings = num_rings
        self.even_num_rings = self.num_rings % 2 == 0
        self.num_labels = len(self.params)

        # validation checks
        if self.params.size != self.min_range.size:
            raise ValueError('params and min_range must be the same size')
        if self.params.size != self.max_range.size:
            raise ValueError('params and max_range must be the same size')
        if self.params.size != self.round_int.size:
            raise ValueError('params and round_int must be the same size')
        if not isinstance(num_rings, int):
            raise ValueError('num_rings must be an integer')
        if self.params.size < 3:
            raise ValueError('params must have at least 3 elements')

        # Get rotation angles
        self.rotation = (2 * np.pi / self.num_labels) * np.arange(self.num_labels)
        self.rotation_sin = np.sin(self.rotation)
        self.rotation_cos = np.cos(self.rotation)

        # Flip the rotation if the label is in lower half
        mask_flip_label = (self.rotation > np.pi / 2) & (self.rotation < np.pi / 2 * 3)
        self.rotation[mask_flip_label] = self.rotation[mask_flip_label] + np.pi
        self.rotation_degrees = -np.rad2deg(self.rotation)

    def __repr__(self):
        """
        The __repr__ function returns a string representation of the object
        :return: The class name, the ring width, the center circle radius, the number of rings, the params, the min range,
        the max range, and the round int.
        """
        return (
            f'{self.__class__.__name__}('
            f'ring_width={self.ring_width!r}, '
            f'center_circle_radius={self.center_circle_radius!r}, '
            f'num_rings={self.num_rings!r}, '
            f'params={self.params!r}, '
            f'min_range={self.min_range!r}, '
            f'max_range={self.max_range!r}, '
            f'round_int={self.round_int!r}'
        )

    def _setup_axis(self, facecolor='#FFFFFF', ax=None):
        """
        It sets the face color of the axis to white, sets the aspect ratio to equal, sets the x and y limits to the radius
        of the center circle plus the width of the rings times the number of rings plus 1.5, and sets the axis to visible
        for radar chart.

        :param facecolor: the background color of the plot, defaults to #FFFFFF (optional)
        :param ax: the matplotlib axes object to draw on
        """
        ax.set_facecolor(facecolor)
        ax.set_aspect('equal')
        lim = self.center_circle_radius + self.ring_width * (self.num_rings + 1.5)
        ax.set(xlim=(-lim, lim), ylim=(-lim, lim))
        set_visible(ax)

    def setup_axis(self, facecolor='#FFFFFF', figsize=(12, 12), ax=None, **kwargs):
        """
        If you pass in an axis, it will set it up with the facecolor and return None. If you don't pass in an axis, it will
        create a new figure and axis, set it up, and return the figure and axis

        :param facecolor: the background color of the plot, defaults to #FFFFFF (optional)
        :param figsize: The size of the figure in inches
        :param ax: The axis to plot on. If None, a new figure and axis will be created
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize, **kwargs)
            self._setup_axis(facecolor=facecolor, ax=ax)
            return fig, ax

        self._setup_axis(facecolor=facecolor, ax=ax)
        return None

    def draw_circles(self, ax=None, inner=True, **kwargs):
        """
        It creates a list of wedge objects, each with a radius equal to the cumulative sum of the ring widths and center
        circle radius, and a width equal to the ring width

        :param ax: the matplotlib axes object to draw on
        :param inner: If True, draw the inner circles. If False, draw the outer circles, defaults to True (optional)
        :return: A collection of patches.
        """
        radius = np.tile(self.ring_width, self.num_rings + 1)
        radius = np.insert(radius, 0, self.center_circle_radius)
        radius = radius.cumsum()
        if (inner and self.even_num_rings) or (inner is False and self.even_num_rings is False):
            ax_circles = radius[0::2]
            first_center = True
        else:
            ax_circles = radius[1::2]
            first_center = False
        rings = []
        for idx, radius in enumerate(ax_circles):
            if (idx == 0) and first_center:
                width = self.center_circle_radius
            else:
                width = self.ring_width
            ring = Wedge(center=(0, 0), r=radius, width=width, theta1=0, theta2=360)
            rings.append(ring)
        rings = PatchCollection(rings, **kwargs)
        rings = ax.add_collection(rings)
        return rings

    def _draw_radar(self, values, ax=None, **kwargs):
        """
        It takes the values you want to plot, clips them to the range of the radar, scales them to the number of rings and
        ring width, and then rotates them to the correct angle.

        :param values: the values to be plotted on the radar chart
        :param ax: the matplotlib axes to draw the radar chart on
        :return: The radar patch and the vertices.
        """
        label_range = np.abs(self.max_range - self.min_range)
        range_min = np.minimum(self.min_range, self.max_range)
        range_max = np.maximum(self.min_range, self.max_range)
        values_clipped = np.minimum(np.maximum(values, range_min), range_max)
        proportion = np.abs(values_clipped - self.min_range) / label_range
        vertices = (proportion * self.num_rings * self.ring_width) + self.center_circle_radius
        vertices = np.c_[self.rotation_sin * vertices, self.rotation_cos * vertices]
        # create radar patch from the vertices
        radar = Polygon(vertices, **kwargs)
        radar = ax.add_patch(radar)
        return radar, vertices

    def draw_radar(self, values, ax=None, kwargs_radar=None, kwargs_rings=None):
        """
        It takes in a list of values, and returns a radar plot with the values plotted on it

        :param values: the values to be plotted on the radar chart
        :param ax: The matplotlib axes to draw the radar chart on
        :param kwargs_radar: keyword arguments for the radar plot
        :param kwargs_rings: keyword arguments for the rings
        :return: The radar, rings, and vertices.
        """
        if kwargs_radar is None:
            kwargs_radar = {}
        if kwargs_rings is None:
            kwargs_rings = {}

        values = np.asarray(values)
        if values.size != self.num_labels:
            raise ValueError('values must have the same size as params')
        radar, vertices = self._draw_radar(values, ax=ax, zorder=1, **kwargs_radar)
        rings = self.draw_circles(ax=ax, inner=False, zorder=2, **kwargs_rings)
        rings.set_clip_path(radar)
        return radar, rings, vertices

    def draw_radar_compare(self, values, compare_values, ax=None,
                           kwargs_radar=None, kwargs_compare=None):
        """
        It takes in two sets of values, and draws two radar charts on the same axis.

        The first set of values is drawn using the kwargs_radar dictionary, and the second set of values is drawn using the
        kwargs_compare dictionary.

        The function returns the two radar charts, and the two sets of vertices.

        The vertices are the points that make up the radar chart.

        The vertices are returned so that you can use them to draw lines between the two radar charts.

        The vertices are returned in the same order as the values.

        For example, if you want to draw a line between the first point on the first radar chart and the first point on the
        second radar chart, you would use the first two vertices.

        If you want to draw a line between the second point on the first radar chart and the second point on the second

        :param values: the values to be plotted
        :param compare_values: The values to compare to
        :param ax: The axis to plot on. If None, the current axis will be used
        :param kwargs_radar: keyword arguments for the radar plot
        :param kwargs_compare: keyword arguments for the compare radar
        :return: radar, radar2, vertices, vertices2
        """
        if kwargs_radar is None:
            kwargs_radar = {}
        if kwargs_compare is None:
            kwargs_compare = {}

        values = np.asarray(values)
        compare_values = np.asarray(compare_values)

        if values.size != self.params.size:
            raise ValueError('values must have the same size as params')
        if compare_values.size != self.params.size:
            raise ValueError('compare_values must have the same size as params')

        radar, vertices = self._draw_radar(values, ax=ax, **kwargs_radar)
        radar2, vertices2 = self._draw_radar(compare_values, ax=ax, **kwargs_compare)

        return radar, radar2, vertices, vertices2

    def draw_range_labels(self, ax=None, offset=0, **kwargs):
        """
        We're going to create a list of labels, one for each ring, and then place them on the plot.

        :param ax: the axis to draw the labels on
        :param offset: how far from the center of the radar chart to place the labels, defaults to 0 (optional)
        :return: A list of text objects.
        """
        label_values = np.linspace(self.min_range.reshape(-1, 1), self.max_range.reshape(-1, 1),
                                   num=self.num_rings + 1, axis=1).ravel()
        # remove the first entry so we do not label the inner circle
        mask = np.ones_like(label_values, dtype=bool)
        mask[0::self.num_rings + 1] = 0
        label_values = label_values[mask]
        # if the range is under 1, round to 2 decimal places (2dp) else 1dp
        mask_round_to_2dp = np.repeat(np.maximum(self.min_range, self.max_range) <= 1,
                                      self.num_rings)
        round_format = np.where(mask_round_to_2dp, '%.2f', '%.1f')
        # if the round_int array is True format as an integer rather than a float
        mask_int = np.repeat(self.round_int, self.num_rings)
        round_format[mask_int] = '%.0f'
        # repeat the rotation degrees for each circle so it matches the length of the label_values
        label_rotations = np.repeat(self.rotation_degrees, self.num_rings)
        # calculate how far out from the center (radius) to place each label, convert to coordinates
        label_radius = np.linspace(self.ring_width,
                                   self.ring_width * self.num_rings,
                                   self.num_rings)
        label_radius = (self.center_circle_radius + offset + label_radius)
        label_xs = np.tile(label_radius, self.num_labels) * np.repeat(self.rotation_sin,
                                                                      label_radius.size)
        label_ys = np.tile(label_radius, self.num_labels) * np.repeat(self.rotation_cos,
                                                                      label_radius.size)
        # write the labels on the axis
        label_list = []
        for idx, label in enumerate(label_values):
            text = ax.text(label_xs[idx], label_ys[idx], round_format[idx] % label,
                           rotation=label_rotations[idx], ha='center', va='center', **kwargs)
            label_list.append(text)
        return label_list

    def draw_param_labels(self, ax=None, wrap=15, offset=1, **kwargs):
        """
        It takes the list of parameters, and places them around the outside of the radar chart

        :param ax: the axis to draw the labels on
        :param wrap: The number of characters to wrap the label at, defaults to 15 (optional)
        :param offset: The distance from the outer ring to the parameter labels, defaults to 1 (optional)
        :return: A list of text objects.
        """
        outer_ring = self.center_circle_radius + (self.ring_width * self.num_rings)
        param_radius = outer_ring + offset
        param_xs = param_radius * self.rotation_sin
        param_ys = param_radius * self.rotation_cos
        label_list = []
        # write the labels on the axis
        for idx, label in enumerate(self.params):
            if wrap is not None:
                label = '\n'.join(textwrap.wrap(label, wrap, break_long_words=False))
            text = ax.text(param_xs[idx], param_ys[idx], label,
                           rotation=self.rotation_degrees[idx], ha='center', va='center', **kwargs)
            label_list.append(text)
        return label_list
