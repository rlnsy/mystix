from code.evaluation import dataLoader

def main():
    dataLoader.load_data("http://winterolympicsmedals.com/medals.csv")

if __name__ == "__main__":
    print("Doing Main Stuff")
    main()

