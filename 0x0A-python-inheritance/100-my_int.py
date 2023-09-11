#!/usr/bin/python3
"""Module that presents MyInt Class inherited from int class
"""


class MyInt(int):
    """class inherited from int class and has inverted equality operation
    """
    def __eq__(self, operand):
        """inverts the behavior of (==) equality operator

        Args:
            operand (int): right operand
        """
        equality = True
        if super().__eq__(operand):
            equality = False
        return (equality)

    def __ne__(self, operand):
        """inverts the behavior of (!=) equality operator

        Args:
            operand (int): right operand
        """
        equality = True
        if super().__ne__(operand):
            equality = False
        return (equality)
