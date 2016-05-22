import chart


class Controller:
    # controller for the DataInterpreter
    def __init__(self, di_model, di_view):
        self.model = di_model
        self.view = di_view
        self.__plot = chart.PlotChart()
        self.__bar = chart.BarChart()
        self.__pie = chart.PieChart()

    def load_csv(self, file_path):
        self.model.load_csv(file_path)
        self.view.show(self.model.get_load_status())

    def draw_plot_chart(self,x_data_name, y_data_name):
        if self.model.contains_valid_records():
            try:
                    x_data = [float(item)for item in self.model.get_valid_data(x_data_name)]
                    y_data = [float(item)for item in self.model.get_valid_data(y_data_name)]
                    self.__plot.draw_plot(x_data_name.upper(), y_data_name.upper(), x_data, y_data)
            except ValueError:
                self.view.show("Chart cannot be drawn, invalid data")
        else:
            self.view.show("No valid data loaded. Please load data to generate chart")

    def draw_bmi_bar_chart(self):
        if self.model.contains_valid_records():
            try:
                    x_data = self.model.get_bmi_distribution()
                    y_data = self.model.get_bmi_options()
                    x_label = 'Distribution of {} people'.format(str(self.model.count_valid_data()))
                    self.__bar.draw_plot(x_label, 'BMI', x_data, y_data)
            except ValueError:
                self.view.show("Chart cannot be drawn, invalid data")
        else:
            self.view.show("No valid data loaded. Please load data to generate chart")
