from transactionType import TransactionType

# example accounts in GnuCash
bank_account = 'bank_account'
regular_income = 'regular_income'
other_income = 'other_income'
rent = 'rent'
other_expenses = 'other_expenses'

# how to define a rule for matching transactions:
# TransactionType(target_account, <- string or None: When importing into GnuCash, you can specify a CSV column for the target account where to import. You can add the name of this target account if you want, of you can specify None
#                 source_account, <- string or None: When importing into GnuCash, you can specify a CSV column for the source account where to import. You can add the name of this source account if you want, of you can specify None
#                 positive_amount, <- boolean: True if the amount of the transaction should be positive, False if it should be negative (required)
#                 possible_issuers=[], <- list of strings: If the issuer of the transaction is one of these strings, the transaction will be matched (optional)
#                 issuer_patterns=[], <- list of strings: If the issuer of the transaction contains one of these strings, the transaction will be matched (optional)
#                 possible_recipients=[], <- list of strings: If the recipient of the transaction is one of these strings, the transaction will be matched (optional)
#                 recipient_patterns=[], <- list of strings: If the recipient of the transaction contains one of these strings, the transaction will be matched (optional)
#                 possible_types=[], <- list of strings: If the type of the transaction is one of these strings, the transaction will be matched (optional)
#                 purpose_patterns=[] <- list of strings: If the purpose of the transaction contains one of these strings, the transaction will be matched (optional)
#                 just add one of the lists. The matching algorithm ends when the first match was found and discards the rest of the lists

# example rules for earnings
regular_income_type = TransactionType(target_account=bank_account,
                                      source_account=regular_income,
                                      positive_amount=True,
                                      possible_issuers=['Sample Company'])

other_income_type = TransactionType(target_account=bank_account,
                                    source_account=other_income,
                                    positive_amount=True,
                                    purpose_patterns=['gift'])

# example rules for expenses
rent_expenses_type = TransactionType(target_account=bank_account,
                                     source_account=rent,
                                     positive_amount=False,
                                     possible_recipients=['Landlord'])

other_expenses_type1 = TransactionType(target_account=bank_account,
                                      source_account=other_expenses,
                                      positive_amount=False,
                                      possible_types=['Withdraw'])

other_expenses_type2 = TransactionType(target_account=bank_account,
                                       source_account=other_expenses,
                                       positive_amount=False,
                                       recipient_patterns=['Grocery', 'Person'])

# this is the configuration for the main script
transaction_types_and_files = [
    # list of transaction types and the name/path of the target file
    # e.g. ([transaction_type1, transaction_type2], 'target_file.csv')
    # if the target file is None, then the transactions will not be written to a file
    # you can use this to intentionally ignore transactions from the input CSV
    ([regular_income_type, other_income_type], 'output/income.csv'),
    ([rent_expenses_type, other_expenses_type1, other_expenses_type2], 'output/expenses.csv'),
]
