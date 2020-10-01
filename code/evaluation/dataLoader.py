import csv, urllib.request
import filecmp

WRITE_OUTPUT_TO_FILE = True # change to True to look at .txt output

def load_data(url: str):
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    data = csv.reader(lines)

    if (WRITE_OUTPUT_TO_FILE):
        text_file = open("dataLoaderOutputActual.txt", "w")

    for row in data:
        print(row)
        if (WRITE_OUTPUT_TO_FILE):
            text_file.write("[")
            for s in row:
                text_file.write("'"+s+"', ")
            text_file.write("]\n")
    
    if (WRITE_OUTPUT_TO_FILE):
        text_file.close()
        print("Assert data loaded as expected: ")
        print(filecmp.cmp('dataLoaderOutputExpected.txt', 'dataLoaderOutputActual.txt'))

    return data

load_data("http://winterolympicsmedals.com/medals.csv")