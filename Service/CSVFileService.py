import csv


def write_row_to_csv(row):
    with open('../Data/data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def write_to_csv(command_dictionary, csv_path='../Data/data.csv'):
    columns = read_columns(csv_path)
    row = [''] * len(columns)
    for key, value in command_dictionary.items():

        if key in columns:
            column_index = columns.index(key)
            row[column_index] = value
    write_row_to_csv(row)


def read_columns(csv_path):
    with open(csv_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        first_row = next(reader, None)
    return first_row


def write_columns_to_csv(commands):
    with open('../Data/data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        # commands = [command.__class__.__name__.rstrip("Command") for command in commands]
        headers = ['Project_ID']
        headers.extend(command for command in commands)
        writer.writerow(headers)
