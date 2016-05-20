import matplotlib.pyplot as plt
import abc


class ChartBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__title = "Data Chart"
        self.__is_interactive = False
        self._x_data = None
        self._y_data = None

    def __make_title(self, x_label, y_label):
        return '{0} {1} RELATIONSHIP'.format(x_label, y_label)

    @abc.abstractmethod
    def do_plot(self):
        """
        hook method for subclasses to overide - drawing is done here
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def data_setup(self):
        """
        hook method for subclasses to overide - manipulate data here, if needed
        :return: None
        """
        raise NotImplementedError

    def draw_plot(self, x_label, y_label, x_data, y_data):
        """
        template method called by controller to draw the chart and open it in a window
        :param x_label: label for x axis
        :param y_label: label for y axis
        :param x_data: array of x_axis data
        :param y_data: array of y_axis data
        :return: None
        """
        self._x_data = x_data
        self._y_data = y_data
        self.data_setup()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(self.__make_title(x_label, y_label))
        plt.interactive(self.__is_interactive)
        self.do_plot()
        plt.show()
