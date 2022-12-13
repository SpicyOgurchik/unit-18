def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    uniq_ages = set(ages)
    oldest = None
    second = None
    
    for age in uniq_ages:
        if oldest is None or age > oldest:
            second = oldest
            oldest = age
        elif second is None or age > second:
            second = age
    
    return (second, oldest)
