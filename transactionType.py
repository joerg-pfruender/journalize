from utils import *
from sourceCsvConfig import *


class TransactionType:
    def __init__(self, target_account, source_account, positive_amount,
                 possible_issuers=[], issuer_patterns=[],
                 possible_recipients=[], recipient_patterns=[],
                 possible_types=[],
                 purpose_patterns=[],
                 iban=None):
        self.target_account = target_account
        self.source_account = source_account
        self.positive_amount = positive_amount
        self.possible_issuers = possible_issuers
        self.issuer_patterns = issuer_patterns
        self.possible_recipients = possible_recipients
        self.recipient_patterns = recipient_patterns
        self.possible_types = possible_types
        self.purpose_patterns = purpose_patterns
        self.iban = iban

    def to_string(self):
        return "[" + str(self.target_account) + ", " + str(self.source_account) + ", " + str(
            self.positive_amount) + ", " + to_string(self.possible_issuers) + ", " + to_string(
            self.issuer_patterns) + ", " + to_string(self.possible_recipients) + ", " + to_string(
            self.possible_types) + ", " + to_string(self.purpose_patterns) + ", " + self.iban + "]"

    def matches_amount_sign(self, transaction):
        amount_in_cents = get_amount_in_cents(transaction)
        if amount_in_cents > 0:
            return self.positive_amount
        else:
            return not self.positive_amount

    def matches_transaction(self, transaction):
        try:
            if not self.matches_amount_sign(transaction):
                return False
            if self.possible_issuers:
                if not is_one_of(transaction[issuer], self.possible_issuers):
                    return False
            if self.issuer_patterns:
                issuer_found = contains_pattern(self.issuer_patterns, transaction[issuer])
                if not issuer_found:
                    return False
            if self.possible_recipients:
                if transaction[recipient] not in self.possible_recipients:
                    return False
            if self.recipient_patterns:
                recipient_found = contains_pattern(self.recipient_patterns, transaction[recipient])
                if not recipient_found:
                    return False
            if self.possible_types:
                if transaction[type] not in self.possible_types:
                    return False
            if self.purpose_patterns:
                purpose_found = contains_pattern(self.purpose_patterns, transaction[purpose])
                if not purpose_found:
                    return False
            if self.iban:
                iban_found = is_one_of_ignore_case(transaction[iban], self.iban)
                if not iban_found:
                    return False
            return True
        except Exception as e:
            raise Exception("cannot match transaction " + to_string(
                transaction) + " with transaction type " + self.to_string() + " because of " + str(e))

