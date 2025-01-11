# analyzed a csv file from online banking
# - import can be configured in sourceCsvConfig.py
# - puts the property expenses and incomes into different csv files (UTF-8)
# - rules for matching transactions can be configured in rulesConfig.py


import sys
from rulesConfig import transaction_types_and_files
from sourceCsvConfig import *
from csvUtils import *
from utils import eprint

transaction_collections_and_files = dict([])
def add_to_transaction_collection(file, transaction):
    transaction_collection = transaction_collections_and_files.get(file, [])
    transaction_collection.append(transaction)
    transaction_collections_and_files[file] = transaction_collection

def analyse_csv(filename):
    print(f'opening file {filename}')
    try:
        transactions = get_transactions_from_csv(filename, source_csv_encoding, source_csv_delimiter)
    except FileNotFoundError:
        eprint(f'File not found: {filename}')
        sys.exit(1)
    verify_headline(transactions)
    for transaction in transactions:
        found_match = False
        for transaction_types, target_file in transaction_types_and_files:
            for transaction_type in transaction_types:
                if transaction_type.matches_transaction(transaction):
                    if transaction_type.target_account is not None and transaction_type.source_account is not None:
                        transaction.append(transaction_type.target_account)
                        transaction.append(transaction_type.source_account)
                    add_to_transaction_collection(target_file, transaction)
                    found_match = True
                    break
        if not found_match:
            eprint('Transaction cannot be matched:')
            eprint(transaction)



def main(filename):
    analyse_csv(filename)
    for file, transaction_collection in transaction_collections_and_files.items():
        if file is not None:
            write_csv(file, transaction_collection)
        # else:
        #     for transaction in transaction_collection:
        #         print("ignoring")
        #         print(transaction)


if __name__ == '__main__':
    input_csv_file_name_param = sys.argv[1]
    if (input_csv_file_name_param == ''):
        eprint('usage: python main.py <input_csv_file_name>')
    else:
        main(input_csv_file_name_param)
