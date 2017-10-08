def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    lst = list(s)
    numericlst = []
    def convertint(lst):
        for i in lst:
            if i.isnumeric():
                numericlst.append(int(i))
    convertint(lst)
    if numericlst == []:
        raise ValueError
    else:
        sumdigits = 0
        for i in numericlst:
            sumdigits += i
        return sumdigits
sum_digits("a;35d4")


