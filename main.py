from code.targets.data import dataLoader
from code.targets.visualization.graphs import GraphManager

if __name__ == "__main__":
    print("Doing Main Stuff")
    dataLoader.load_data("http://winterolympicsmedals.com/medals.csv")
    gm = GraphManager()
    gm.add_plot("example plot")
    gm.graphics.display()

