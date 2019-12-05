"""Created a class to define exception when there the given method is not found"""


class MethodNotFoundException(Exception):
    """inherited Exception super class and defined __init__ method"""

    def __init__(self):
        super().__init__()
        print("Method Not Found")
