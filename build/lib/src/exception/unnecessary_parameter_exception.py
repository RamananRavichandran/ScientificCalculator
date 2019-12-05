"""Created a class to define exception when there is more than 2 parameters"""
class UnnecessaryParameterException(Exception):
    """inherited Exception super class and defined __init__ method"""

    def __init__(self):
        super().__init__()
        print("Unnecessary Number Of Parameters")
