import matplotlib.pyplot as plt
import numpy as np

from DataInterpreter.chartbase import ChartBase


class PlotChart(ChartBase):
    """
    plot x data against y data
    """
    def data_setup(self):
        """
        sort data array
        :return: None
        """
        self._x_data.sort()
        self._y_data.sort()

    def do_plot(self):
        """
        plot values
        :return: None
        """
        plt.plot(self._x_data, self._y_data, label="",)


class HorizontalBarChart(ChartBase):
    """
    Draw a horizontal bar chart of bmi distribution
    """
    def make_title(self, x_label, y_label):
        return '{1} {0}'.format(x_label, y_label)

    def data_setup(self):
        """
        use y_data to calculate points
        :return: None
        """
        self._y_pos = np.arange(len(self._y_data))

    def do_plot(self):
        """
        drawing is done here
        :return: None
        """
        plt.yticks(self._y_pos, self._y_data)
        plt.barh(self._y_pos, self._x_data, align='center')


class PieChart(ChartBase):
    def make_title(self, x_label, y_label):
        return '{1} {0}'.format(x_label, y_label)

    def data_setup(self):
        """
        manipulate data here, if needed
        :return: None
        """
        pass

    def do_plot(self):
        """
        drawing is done here
        :return: None
        """
        plt.xlabel('')
        plt.ylabel('')
        colors = ['gold', 'lightskyblue', 'yellowgreen', 'lightcoral']
        plt.pie(self._x_data, labels=self._y_data, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
