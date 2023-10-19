import csv
def write_row_to_csv(row):
    with open('../data.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

# header = ['ParentFolderName','FileRelPath','FileName','MethodName','Usings']
# header = ['for','foreach','if','while']
# write_row_to_csv(header)