def reverse(x: int) -> int:
    rev = 0
    INTMAX = 214748364
    INTMIN = -214748364
    if x == 0:
        return 0
    else:
        sgn = int(x / abs(x))
        while x != 0:
            pop = sgn * (abs(x) % 10)
            x = int(x / 10)
            if (rev < INTMIN) or (rev == INTMAX and pop < -8):
                return 0
            if (rev > INTMAX) or (rev == INTMAX and pop > 7):
                return 0
            rev = rev * 10 + pop
        return rev


def reverse_pythonic(x: int) -> int:
    try:
        rev = int(x/abs(x))*int(str(abs(x))[::-1])
        return rev if -2**31 < rev < (2**31 - 1) else 0
    except ZeroDivisionError:
        return 0
