from code.ui.graphics import Graphics


class GraphManager:

    def __init__(self):
        self.graphics = Graphics()
        self.graphics.add_window("410 DSL", 600, 600)

    def add_plot(self, plot_name: str):
        self.graphics.get_window("410 DSL").addPlot(title=plot_name, y=[])
