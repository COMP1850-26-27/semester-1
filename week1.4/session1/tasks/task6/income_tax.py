# Week 4, Session 1: Task 3

# You are given the function income_tax_calculator and a docstring.
# Your task is to write the body of the function based on the
# details in the docstring. You can create additional functions
# to be called from within income_tax_calculator


def income_tax_calculator(annual_income):
    """
    This function calculates the tax amount for a given taxable annual income
    based on the UK tax rates and allowances. The tax is calculated
    progressively across tax bands, as per the following rates and allowances:

    Band               |  Taxable income   | Tax rate
    Personal allowance | Up to 12,570      | 0%
    Basic rate         | 12,571 to 50,270  | 20%
    Higher rate        | 50,271 to 125,140 | 40%
    Additional rate    | over 125,140      | 45%

    Key Details:
    Personal Allowance: The first £12,570 of taxable income is tax-free.
    Progressive Taxation: Income tax is applied progressively across bands.
    For example, an annual income of £25,000 would be taxed as follows:
    The first £12,570 at 0% (personal allowance).
    The remaining £12,430 (i.e., £25,000 - £12,570) at 20% (basic rate).

    Args:
        annual_income: float

    Returns:
        a float, representing the total calculated tax, rounded to
        one decimal point. You can use the round() function,
        e.g round(tax, 1) 0.0 if annual_income is not a positive integer.
    """


# Check if the following lines produce the correct output
print(income_tax_calculator(12000))     # 0.0
print(income_tax_calculator(14000))     # 286.0
print(income_tax_calculator(25000))     # 2486.0
print(income_tax_calculator(100000))    # 27432.0
