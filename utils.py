import sys

stdErr = sys.stderr

def get_eurocents(str, decimal_separator):
    money_str_clean = str.replace(' ', '')
    negative = False
    if str.startswith('-'):
        negative = True
        money_str_clean = money_str_clean.replace('-', '')

    cur_str = money_str_clean.split(decimal_separator)
    euro_str = cur_str[0]
    cents_str = "00"
    if (len(cur_str) > 1):
        cents_str = cur_str[1]
    euro_str = euro_str.replace('.', '')
    try:
        euros = int(euro_str)
    except ValueError:
        raise Exception("Cannot read " + euro_str)
    cents = int(cents_str)
    cents_total = (euros * 100) + cents
    if negative:
        return -cents_total
    else:
        return cents_total
def to_string(list):
    return ','.join([str(x) for x in list])


def is_one_of(string, list_of_strings):
    return string in list_of_strings


def contains_pattern(list_of_patterns, string):
    for pattern in list_of_patterns:
        if pattern in string:
            return True
    return False

# https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
def eprint(*args, **kwargs):
    print(*args, file=stdErr, **kwargs)