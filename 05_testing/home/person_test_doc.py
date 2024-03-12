from person import Human
import doctest



def Test_human():
    """
    >>> Human.age = 71
    ValueError: староват
    """
    # person = Human('Smith', 'Johan', 40)
    # person.age = 71

if __name__ == '__main__':

    doctest.testmod(verbose=True)