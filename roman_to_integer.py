def romanToInt(self, s: str) -> int:
    mapping = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
    number = 0
    for idx in range(0, len(s) - 1, 1):
        if mapping[s[idx]] >= mapping[s[idx + 1]]:
            number += mapping[s[idx]]
        else:
            number -= mapping[s[idx]]
    return number + mapping[s[-1]]


def roman_to_int_pythonic(self, s: str) -> int:
    mapping = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
    num, p = 0, mapping['I']
    for c in s[::-1]:
        num, p = num + mapping[c] if mapping[c] >= p else num - mapping[c], mapping[c]
    return num
