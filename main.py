from code.targets.data import dataLoader
import pyqtgraph.examples  # type: ignore

if __name__ == "__main__":
    print("Doing Main Stuff")
    dataLoader.load_data("http://winterolympicsmedals.com/medals.csv")
    pyqtgraph.examples.run()

