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
        ax.set_facecolor(facecolor)
        ax.set_aspect('equal')
        lim = self.center_circle_radius + self.ring_width * (self.num_rings + 1.5)
        ax.set(xlim=(-lim, lim), ylim=(-lim, lim))
        set_visible(ax)

    def setup_axis(self, facecolor='#FFFFFF', figsize=(12, 12), ax=None, **kwargs):
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize, **kwargs)
            self._setup_axis(facecolor=facecolor, ax=ax)
            return fig, ax

        self._setup_axis(facecolor=facecolor, ax=ax)
        return None

    def draw_circles(self, ax=None, inner=True, **kwargs):
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
