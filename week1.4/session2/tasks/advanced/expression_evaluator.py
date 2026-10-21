"""
    THIS IS NOT FOR BEGINNER, PLEASE IGNORE THIS TASK IF YOU ARE
    NEW TO PROGRAMMING.

    Complete the folllowing function that takes a mathematical expression
    as a string and evaluates it. This function allows for an arbitrary number
    of keyword arguments using **kwargs, and provide default values for
    variable x, and y if they are not provided.
"""


def evaluate_expression(expression, x=0, y=0, **kwargs):
    """
    Evaluates a mathematical expression with arbitrary variables.
    - expression: A string representing the mathematical expression.
    - x, y: Default values for 'x' and 'y' if not provided.
    - **kwargs: Arbitrary additional variables for the expression.

    Example usage:
        evaluate_expression('x + y + z', x=1, y=2, z=3) -> 6
        evaluate_expression('a * b + c', a=5, b=3, c=10) -> 25

    To get started with this task, you can have a look at Python built-in
    function eval that will return the results of an evaluated expression.
    """
