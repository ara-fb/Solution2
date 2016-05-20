from chartbase import ChartBase
import matplotlib.pyplot as plt
import numpy as np


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




class BarChart(ChartBase):

    def data_setup(self):
        """
        hook method for subclasses to overide - manipulate data here, if needed
        :return: None
        """
        # self._y_data = np.arange(len(self._y_data))
        pass

    def do_plot(self):
        """
        hook method for subclasses to overide - drawing is done here
        :return: None
        """
        plt.barh(self._y_data, self._x_data, align='center')

