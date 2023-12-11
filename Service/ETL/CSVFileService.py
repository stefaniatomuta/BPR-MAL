import csv

csv_path = r'..\\Data\\data.csv'


def write_row_to_csv(row):
    with open(csv_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def write_to_csv(command_dictionary, csv_path=csv_path):
    columns = read_columns(csv_path)
    row = [''] * len(columns)
    for key, value in command_dictionary.items():
        if key in columns:
            column_index = columns.index(key)
            row[column_index] = value
    write_row_to_csv(row)


def read_columns(path):
    with open(path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        first_row = next(reader, None)
    return first_row


def write_column_headers_to_csv(commands):
    with open(csv_path, 'a', newline='') as f:
        writer = csv.writer(f)
        headers = ['Project_ID']
        headers.extend(command for command in commands)
        writer.writerow(headers)
