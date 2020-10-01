import csv, urllib.request

def load_data(url: str):
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    data = csv.reader(lines)

    for row in data:
        print(row)
    
    return data

load_data("http://winterolympicsmedals.com/medals.csv")