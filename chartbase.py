import matplotlib.pyplot as plt
import abc


class ChartBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__is_interactive = False
        self._x_data = None
        self._y_data = None

    @abc.abstractmethod
    def do_plot(self):
        """
        abstract method for subclasses to implement - drawing is done here
        :return: None
        """
        raise NotImplementedError

    def do_setup(self):
        """
        hook method for subclasses to override or extend - manipulate data here, if needed
        :return: None
        """
        pass

    def draw_chart(self, x_data, y_data, title=None, x_label='', y_label=''):
        """
        template method called by controller to draw the chart and open it in a window
        """
        self._x_data = x_data
        self._y_data = y_data
        self.do_setup()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.interactive(self.__is_interactive)
        self.do_plot()
        plt.show()
