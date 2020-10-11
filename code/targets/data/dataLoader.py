import csv, urllib.request  # type: ignore


def load_data(url: str, file: str = None):
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    data = csv.reader(lines)

    if file is not None:
        text_file = open(file, "w")

    for row in data:
        if file is not None:
            text_file.write("[")
            for s in row:
                text_file.write("'"+s+"', ")
            text_file.write("]\n")
    
    if file is not None:
        text_file.close()

    return data
