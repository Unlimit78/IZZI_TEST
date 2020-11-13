import csv
import io
def csv_parser(file):
    decoded_file = file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = list(csv.reader(io_string, delimiter=','))


    return reader[1:]
