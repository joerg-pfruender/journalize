from utils import get_eurocents

decimal_separator = '.' # for German: ','
source_csv_delimiter = ';'
source_csv_encoding = 'UTF-8'

# online banking columns (example)
booking_date = 0
type = 1
issuer = 2
recipient = 3
purpose = 4
iban = 5
amount = 6
ignore_currency = 7

# online banking columns (Postbank Germany)
# booking_date = 0 # buchungstag
# value_date = 1 # wertstellung
# type = 2 # art
# issuer = 3 # auftraggeber
# recipient = 3 # empfaenger
# purpose = 4 # verwendungszweck
# iban = 5 # iban
# bic = 6 # bic
# ignore1 = 7 # kundenreferenz
# ignore2 = 8 # mandatsreferenz
# ignore3 = 9 # glaeubiger_id
# ignore4 = 10 # fremde_gebuehren
# amount = 11 # betrag
# ignore5 = 12 # abweichender_empfaenger
# ignore6 = 13 # anzahl_der_auftraege
# ignore7 = 14 # anzahl_der_schecks
# ignore8 = 15 # soll
# ignore9 = 16 # haben
# ignore10 = 17 # waehrung

# online banking columns (Volksbanken/Raiffeisenbanken Germany)
# Bezeichnung Auftragskonto
# IBAN Auftragskonto
# BIC Auftragskonto
# Bankname Auftragskonto
# booking_date = 4 # Buchungstag
# value_date = 5 # Valutadatum
# recipient = 6 # Name Zahlungsbeteiligter
# iban = 7 # IBAN Zahlungsbeteiligter
# bic = 8 # BIC (SWIFT-Code) Zahlungsbeteiligter
# type = 9 # Buchungstext
# purpose = 10 # Verwendungszweck
# amount = 11 # Betrag
# Waehrung
# Saldo nach Buchung
# Bemerkung
# Kategorie
# Steuerrelevant
# Glaeubiger ID
# Mandatsreferenz


def get_amount_in_cents(transaction):
    amount_as_string = transaction[amount]
    amount_without_euro_sign = amount_as_string.replace('\x80', '').replace(u'\u20AC', '').replace('EUR', '').strip() # you may change this to your currency
    return get_eurocents(amount_without_euro_sign, decimal_separator)


def verify_headline(transactions):
    # if your CSV has no headline, just comment the whole function
    headlines = transactions[0]
    # change the verification according to the layout of your input CSV or comment the verification code
    if headlines[booking_date] == 'Date' and headlines[purpose] == 'Purpose' and \
            headlines[issuer] == 'Issuer' and \
            headlines[amount] == 'Amount':
        print('headlines ok')
    else:
        raise 'Headlines are wrong'
    transactions.pop(0)