import matplotlib.pyplot as plt
import numpy as np

from DataInterpreter.chartbase import ChartBase


class PlotChart(ChartBase):
    """
    plot xdata against y data
    """
    def data_setup(self):
        """
        hook method for subclasses to overide - manipulate data here, if needed
        :return: None
        """
        self._x_data.sort()
        self._y_data.sort()

    def do_plot(self):
        """
        hook method for subclasses to overide - drawing is done here
        :return: None
        """
        plt.plot(self._x_data, self._y_data, 'ro', label="",)


class HorizontalBarChart(ChartBase):
    def make_title(self, x_label, y_label):
        return '{1} {0}'.format(x_label, y_label)

    def data_setup(self):
        """
        hook method for subclasses to overide - manipulate data here, if needed
        :return: None
        """
        # self._y_data = np.arange(len())
        self._y_pos =  np.arange(len(self._y_data))
        pass

    def do_plot(self):
        """
        hook method for subclasses to overide - drawing is done here
        :return: None
        """
        plt.yticks(self._y_pos, self._y_data)
        plt.barh(self._y_pos, self._x_data, align='center')


class PieChart(ChartBase):
    def make_title(self, x_label, y_label):
        return '{1} {0}'.format(x_label, y_label)

    def data_setup(self):
        """
        hook method for subclasses to overide - manipulate data here, if needed
        :return: None

        """
        return

    def do_plot(self):
        """
        hook method for subclasses to overide - drawing is done here
        :return: None
        """
        plt.xlabel('')
        plt.ylabel('')
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        plt.pie(self._x_data, labels=self._y_data, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
