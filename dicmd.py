import cmd
import di
import validate
import dicontroller
import dipersistence


class DataInterpreterCmd(cmd.Cmd):
    """CMD View for a Data Interpreter."""
    CHART_OPTIONS = ['age income', 'income age', 'age sales', 'sales age', 'income sales', 'sales income']

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.controller = None
        self.intro = 'Interpret data from a csv file and generate charts.    Type help or ? to list commands.\n'
        self.prompt = 'Data Interpreter: '
        self.undoc_header = None  # no header for undoccumented commands

    def register_controller(self, the_controller):
        self.controller = the_controller

    @staticmethod
    def show(msg):
        """
        prints error message
        :param msg: str to print
        """
        print(msg)

    def do_loadcsv(self, file_path):
        """
         get file_path
         :param file_path: file path as a str
        """
        self.controller.load_csv(file_path)

    def help_loadcsv(self):
        print('\n'.join(['loads data from a valid csv file at [file_path]',
                         'Each data entry must be in following order: id, gender, age, sales, bmi, income',
                         'Rules for Data as follows',
                         '     id :[A-Z][0-9]{3} example S234)',
                         '     gender: (M|F) example M',
                         '     age: [0-9]{2} example 23',
                         '     sales: [0-9]{3} example 034',
                         '     bmi: (Normal|Overweight|Obesity|Underweight)',
                         '     income: [0-9]{2,3} example 239',
                         'Will validate incorrect case for alphabetic values']))

    def do_plot(self,options):
        """
        if options are valid input, otherwise do error
        :param options: string, one of CHART_OPTIONS
        """
        if options and options in self.CHART_OPTIONS:
            result = options.split()
            x_data = result[0]
            y_data = result[1]
            self.controller.draw_plot_chart(x_data, y_data)
        else:
            print("invalid option selected")

    def complete_plot(self, text, line, begidx, endidx):
        if not text:
            completions = self.CHART_OPTIONS[:]
        else:
            completions = [o
                           for o in self.CHART_OPTIONS
                           if o.startswith(text)]
        return completions

    def help_plot(self):
        print('\n'.join(['Generates a chart using plotting options',
                         'Accepted inputs are:',
                         '     age income',
                         '     income age',
                         '     age sales',
                         '     sales age',
                         '     income sales',
                         '     sales income'
                         '     data values are taken from file and only valid values are plotted',
                         '!If there is no data this command will not work!']))

    def do_barchart(self, args):
        self.controller.draw_bmi_bar_chart()

    def help_barchart(self):
        print('\n'.join(['Generates a bar chart showing distribution of BMI in valid records',
                         '     data values are taken from file and only valid values are plotted',
                         '!If there is no data this command will not work!']))

    def do_piechart(self, args):
        self.controller.draw_bmi_pie_chart()

    def help_piechart(self):
        print('\n'.join(['Generates a pie chart showing distribution of BMI in valid records',
                         '     data values are taken from file and only valid values are plotted',
                         '!If there is no data this command will not work!']))

    def do_quit(self, args):
        """Quits you out of the Data Interpreter
        Data is not saved"""
        print("Quitting...")
        return 1

    def do_EOF(self, args):
        return True

    def print_topics(self, header, cmds, cmdlen, maxcol):
        # only print help for documented commands
        if header is not None:
            cmd.Cmd.print_topics(self, header, cmds, cmdlen, maxcol)

    def postloop(self):
        print()

# app/ instantiate and go
if __name__ == '__main__':
    view = DataInterpreterCmd()
    controller = dicontroller.Controller(di.DataInterpreter(dipersistence.DiPersistence(), validate.Validator()), view)
    view.register_controller(controller)
    view.cmdloop()
