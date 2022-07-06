# IMPORT PYSIDE MODULES
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QVBoxLayout

# IMPORT PROCESSING, CHART & CLUSTERING MODULES
# ///////////////////////////////////////////////////////////////
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# IMPORT CUSTOM RADAR
# ///////////////////////////////////////////////////////////////
from .py_radar_chart import Radar


# PY SPYDER WIDGET
# ///////////////////////////////////////////////////////////////
# This class is a widget that contains Radar Chart
class PySpyderWidget(QWidget):
    def __init__(
            self,
            language='en',
            parent=None,
            bg_two="#343b48",
            bg_one="#343b48",
            dark_three="#21252d",
            axis_color="#f5f6f9",
            color_title="#dce1ec",
            line_color="#3f6fd1"
    ):
        """
        The function __init__() is a constructor that initializes the attributes of the class

        :param language: The language of the chart, defaults to en (optional)
        :param parent: The parent widget
        :param bg_two: background color of the chart, defaults to #343b48 (optional)
        :param bg_one: background color of the chart, defaults to #343b48 (optional)
        :param dark_three: background color of the chart, defaults to #21252d (optional)
        :param axis_color: color of the axis, defaults to #f5f6f9 (optional)
        :param color_title: The color of the title, defaults to #dce1ec (optional)
        :param line_color: The color of the lines that connect the points, defaults to #3f6fd1 (optional)
        """
        super().__init__(parent)

        self.language = language

        self.spyder_chart = _CustomSpyder(
            self,
            language=self.language,
            bg_two=bg_two,
            bg_one=bg_one,
            dark_three=dark_three,
            axis_color=axis_color,
            color_title=color_title,
            line_color=line_color
        )

        self.principal_layout = QVBoxLayout(self)
        self.principal_layout.addWidget(self.spyder_chart)


# It's a class to place radar chart
class _CustomSpyder(FigureCanvas):
    def __init__(
            self,
            parent,
            bg_two,
            bg_one,
            dark_three,
            axis_color,
            color_title,
            line_color,
            language='en',
    ):
        """
        It creates a radar chart with a title and a background color

        :param parent: The parent widget
        :param bg_two: background color of the plot
        :param bg_one: background color of the radar plot
        :param dark_three: The color of the radar's background
        :param axis_color: The color of the axis lines
        :param color_title: The color of the title
        :param line_color: The color of the lines that connect the points on the radar chart
        :param language: The language of the labels, defaults to en (optional)
        """
        self.fig, self.ax = radar_mosaic(radar_height=0.915, title_height=0.06, fig_height=14)
        super(_CustomSpyder, self).__init__(self.fig)
        # COLORS
        self.bg_two = bg_two
        self.bg_one = bg_one
        self.dark_three = dark_three
        self.axis_color = axis_color
        self.color_title = color_title
        self.line_color = line_color
        self.COLORS = ["#FF5A5F", "#007A87", "#FFB400"]

        # Inner Dataframes
        self._inner_squad = None
        self._inner_scouting = None
        self._inner_old_squad = None

        self.language = language

        self.fig.set_facecolor(self.bg_one)
        self.ax['radar'].axis('off')
        self.ax['title'].set_facecolor(self.bg_one)
        self.ax['radar'].set_facecolor(self.bg_one)
        self.ax['radar'].xaxis.label.set_color(self.bg_one)
        self.ax['radar'].yaxis.label.set_color(self.bg_one)
        self.ax['radar'].tick_params(axis='x', colors=self.bg_one)
        self.ax['radar'].tick_params(axis='y', colors=self.bg_one)

        self._parent = parent
        self._data = None
        self.setParent(parent)

    def set_data(self, data, opt=0):
        """
        If the dataframe is empty, set the dataframe to the data. If the dataframe is not empty, concatenate the dataframe
        with the data

        :param data: the dataframe that you want to add to the class
        :param opt: the option to concatenate the dataframe, defaults to 0 (optional)
        """
        if opt == 0:
            self._inner_squad = data
            if self._inner_scouting is None and self._inner_old_squad is None:
                self._data = data
            if self._inner_scouting is not None:
                self._data = pd.concat([
                    self._inner_squad,
                    self._inner_scouting
                ],
                    axis=0)
            elif self._inner_scouting is not None and self._inner_old_squad is not None:
                tmp = pd.concat(
                    [
                        self._inner_squad,
                        self._inner_scouting
                    ],
                    axis=0
                )
                self._data = pd.concat(
                    [
                        tmp,
                        self._inner_old_squad
                    ],
                    axis=0
                )
            self._data.reset_index(drop=True, inplace=True)
        elif opt == 1:
            self._inner_scouting = data
            if self._inner_old_squad is not None:
                tmp = pd.concat(
                    [
                        self._inner_squad,
                        self._inner_scouting
                    ],
                    axis=0
                )
                self._data = pd.concat(
                    [
                        tmp,
                        self._inner_old_squad
                    ],
                    axis=0
                )
            elif self._inner_old_squad is None:
                self._data = pd.concat(
                    [
                        self._inner_squad,
                        self._inner_scouting
                    ],
                    axis=0
                )
            self._data.reset_index(drop=True, inplace=True)
        elif opt == 2:
            self._inner_old_squad = data
            tmp = pd.concat(
                [
                    self._inner_squad,
                    self._inner_scouting
                ],
                axis=0
            )

            self._data = pd.concat(
                [
                    tmp,
                    self._inner_old_squad
                ],
                axis=0
            )
            self._data.reset_index(drop=True, inplace=True)

    def set_chart(self, players, squads, opts):
        """
        The function takes in a list of players, a list of squads, and a list of options. It then creates a radar chart
        comparing the players' stats

        :param players: list of players
        :param squads: list of squads
        :param opts: list of strings, the labels for each axis
        """
        if opts:
            self.ax['radar'].clear()
            self.ax['title'].clear()
            self.ax['title'].axis('off')
            if self._data is not None and len(players) <= 3:
                min_ranges = []
                max_ranges = []
                column_index_name = self._data.columns[0]
                tmp_df = self._data[self._data[column_index_name].isin(players)]
                for o in opts:
                    a = tmp_df[o].min()
                    a = a - (a * .15)

                    b = tmp_df[o].max()
                    b = b + (b * .15)

                    min_ranges.append(a)
                    max_ranges.append(b)

                radar = Radar(opts, min_ranges, max_ranges,
                              round_int=[False] * len(opts),
                              num_rings=6, ring_width=1, center_circle_radius=1)

                radar.setup_axis(ax=self.ax['radar'], facecolor=self.bg_one)
                radar.draw_circles(
                    ax=self.ax['radar'],
                    facecolor=self.dark_three,
                    edgecolor=self.dark_three,
                )
                # /////////////////////////////////////////////////////////////////////////////
                opts.append(column_index_name)
                tmp_df = tmp_df.loc[:, opts]
                tmp_df = tmp_df.set_index(column_index_name)

                values1 = tmp_df.iloc[0].tolist()
                if players[0] == players[1]:
                    values2 = tmp_df.iloc[0].tolist()
                else:
                    values2 = tmp_df.iloc[1].tolist()
                # /////////////////////////////////////////////////////////////////////////////
                radar_output = radar.draw_radar_compare(
                    values1,
                    values2,
                    ax=self.ax['radar'],
                    kwargs_radar={'facecolor': self.COLORS[0], 'alpha': 0.15},
                    kwargs_compare={'facecolor': self.COLORS[1], 'alpha': 0.15},
                )
                radar_poly, radar_poly2, vertices1, vertices2 = radar_output  # skipcq: PYL-W0612

                radar.draw_range_labels(
                    ax=self.ax['radar'],
                    fontsize=10,
                    color=self.axis_color
                )

                radar.draw_param_labels(
                    ax=self.ax['radar'],
                    fontsize=15,
                    color=self.axis_color
                )
                vertices11 = np.append(vertices1, vertices1[0])
                vertices22 = np.append(vertices2, vertices2[0])
                vertices11 = np.reshape(vertices11, (int(len(vertices11) / 2), 2))
                vertices22 = np.reshape(vertices22, (int(len(vertices22) / 2), 2))
                self.ax['radar'].scatter(vertices1[:, 0], vertices1[:, 1],
                                         c=self.COLORS[0], marker='D', s=90, zorder=2)
                self.ax['radar'].scatter(vertices2[:, 0], vertices2[:, 1],
                                         c=self.COLORS[1], marker='D', s=90, zorder=2)
                self.ax['radar'].plot(vertices11[:, 0], vertices11[:, 1], self.COLORS[0], linewidth=2.5,
                                      linestyle=':', zorder=2)
                self.ax['radar'].plot(vertices22[:, 0], vertices22[:, 1], self.COLORS[1], linewidth=2.5,
                                      linestyle=':', zorder=2)
                var1, var2 = change_squad(squads, self.language)
                self.ax['title'].text(0.01, 0.65, players[0], fontsize=18, color=self.COLORS[0], ha='left', va='center')
                self.ax['title'].text(0.99, 0.65, players[1], fontsize=18, color=self.COLORS[1], ha='right',
                                      va='center')
                self.ax['title'].text(0.01, 0.1, var1, fontsize=10, color=self.COLORS[0], ha='left', va='center')
                self.ax['title'].text(0.99, 0.1, var2, fontsize=10, color=self.COLORS[1], ha='right', va='center')
                self.fig.canvas.draw()

    def change_language(self, new_lang):
        """
        This function changes the language of the user to the new language.

        :param new_lang: The new language to change to
        """
        self.language = new_lang


def radar_mosaic(radar_height=0.915, title_height=0.06, fig_height=14):
    """
    It creates a figure with three axes, one for the title, one for the radar, and one for the endnote. The axes are
    arranged vertically, with the title at the top, the radar in the middle, and the endnote at the bottom. The height of
    the title and radar axes are specified by the user, and the height of the endnote is calculated to fill the rest of the
    figure

    :param radar_height: The height of the radar plot in the figure
    :param title_height: The height of the title, in inches
    :param fig_height: The height of the figure in inches, defaults to 14 (optional)
    :return: A tuple of the figure and axes objects.
    """
    if title_height + radar_height > 1:
        error_msg = 'Reduce one of the radar_height or title_height so the total is <= 1.'
        raise ValueError(error_msg)
    end_note_height = 1 - radar_height - title_height
    fig_width = fig_height * radar_height
    figure, axes = plt.subplot_mosaic(
        [
            ['title'],
            ['radar'],
            ['endnote']
        ],
        gridspec_kw={
            'height_ratios': [
                title_height,
                radar_height,
                end_note_height
            ],
            'bottom': 0,
            'left': 0,
            'top': 1,
            'right': 1,
            'hspace': 0
        },
        figsize=(
            fig_width,
            fig_height
        )
    )
    axes['title'].axis('off')
    axes['endnote'].axis('off')
    return figure, axes


def change_squad(inner_squad, lang):
    """
    It takes a list of two strings and a language code, and returns two strings

    :param inner_squad: This is the list of the two squad lists that are being compared
    :param lang: The language of the wiki
    :return: the inner_var1 and inner_var2 variables.
    """
    inner_var1 = ''
    inner_var2 = ''
    if lang == 'en':
        if 'Actual' in inner_squad[0]:
            inner_var1 = 'Actual Squad list'
        elif 'Scouting' in inner_squad[0]:
            inner_var1 = 'Scouting Squad list'
        elif 'Old' in inner_squad[0]:
            inner_var1 = 'Old Squad list'

        if 'Actual' in inner_squad[1]:
            inner_var2 = 'Actual Squad list'
        elif 'Scouting' in inner_squad[1]:
            inner_var2 = 'Scouting Squad list'
        elif 'Old' in inner_squad[1]:
            inner_var2 = 'Old Squad list'
    elif lang == 'es':
        if 'Actual' in inner_squad[0]:
            inner_var1 = 'Lista actual del equipo'
        elif 'Scouting' in inner_squad[0]:
            inner_var1 = 'Lista de scouting'
        elif 'Old' in inner_squad[0]:
            inner_var1 = 'Lista vieja del equipo'

        if 'Actual' in inner_squad[1]:
            inner_var2 = 'Lista actual del equipo'
        elif 'Scouting' in inner_squad[1]:
            inner_var2 = 'Lista de scouting'
        elif 'Old' in inner_squad[1]:
            inner_var2 = 'Lista vieja del equipo'

    return inner_var1, inner_var2
