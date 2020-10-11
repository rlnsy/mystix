from code.targets.data import dataLoader
from code.targets.visualization import graphs_example


if __name__ == "__main__":
    print("Doing Main Stuff")
    dataLoader.load_data("http://winterolympicsmedals.com/medals.csv")
    graphs_example.run()
