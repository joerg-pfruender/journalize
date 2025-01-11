import csv

def get_transactions_from_csv(filename, encoding, delimiter):
    transactions = []
    with open(filename, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            transactions.append(row)
    return transactions


def write_csv(filename, rows):
    if len(rows) > 0:
        with open(filename, 'w') as csvfile:
            startwriter = csv.writer(csvfile, delimiter=';')
            for row in rows:
                startwriter.writerow(row)
