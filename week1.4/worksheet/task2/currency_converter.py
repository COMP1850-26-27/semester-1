
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # your code here
    rate = conversion_rate[from_currency][ to_currency]
    print(rate)
    #print((amount * rate).2f)
    new = amount * rate
    print(round(new, 2))

    return None

# Submit only this file currency_converter.py with the completed function.
currency_converter(amount = 786, from_currency = "CNY", to_currency = "GBP")
# Remove any additional code you may have added during development and testing.
