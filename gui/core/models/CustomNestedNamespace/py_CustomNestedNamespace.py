# IMPORT PACKAGES AND MODULES
from types import SimpleNamespace


class NestedNamespace(SimpleNamespace):
    """It's a `SimpleNamespace` that can contain other `SimpleNamespace`s"""

    def __init__(self, dictionary, **kwargs):
        """
        It takes a dictionary and creates a new object with the keys of the dictionary as attributes and the values
         of the dictionary as the values of the attributes

        :param dictionary: The dictionary to convert to a Namespace
        """
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)
