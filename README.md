# Journalize

* reads the CSV file that you get from online-banking.
* applies the rules that you provide in rulesConfig.py
  * collects the transactions that match one rule into one collection.
  * adds the GnuCash's account's names if configured.
* exports the result into CSV files, that you can import into GnuCash.

## Precondition
* Python 3.8
* Input CSV file can have at most one header line, configure this in sourceCsvConfig's `verify_headline` function.
* Input CSV file must not have other lines than the headline and the transactions.

## Usage

1. Fork and clone the repository
2. Change sourceCsvConfig.py so that it describes the format of the CSV file that you get from online-banking.
3. Change rulesConfig.py so that it describes the rules that you want to apply to the CSV file.
4. Run main.py with one parameter: the name/path to the CSV file that you get from online-banking.
5. look into std err and fix parsing errors.
6. look into std err for unmatched transactions and apply your rules accordingly.
7. if you are happy with the result, import the CSV files into [GnuCash](https://www.gnucash.org).

run the unit test in DemoTestCase.py to see how the program works.
