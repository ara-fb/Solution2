import chart

class Controller:
    # controller for the DataInterpreter
    def __init__(self, di_model, di_view):
        self.model = di_model
        self.view = di_view
        # self.chart = chart.PlotChart() # default chart

    def load_csv(self, file_path):
        self.model.load_csv(file_path)
        self.view.show(self.model.get_load_status())

    def draw_chart(self, type, x_data_name, y_data_name):
        if self.model.contains_valid_records():
            try:
                if type == 'plot':
                    self.chart = chart.PlotChart()
                    x_data = [float(item)for item in self.model.get_valid_data(x_data_name)]
                    y_data = [float(item)for item in self.model.get_valid_data(y_data_name)]
                # elif type == 'bar':
                #    x_data = self.model.get_valid_data(x_data_name)
                #    y_data = [float(item)for item in self.model.get_valid_data(y_data_name)]
                    self.chart.draw_plot(x_data_name.upper(), y_data_name.upper(), x_data, y_data)
            except ValueError:
                self.view.show("Chart cannot be drawn, invalid data")
        else:
            self.view.show("No valid data loaded. Please load data to generate chart")
