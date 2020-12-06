# %%
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# %%
def deconstructromantoint(roman: str):
    num = 0
    for i, char in enumerate(roman):
        if char == 'I':
            if i != len(roman)-1 and roman[i+1] != "I":
                num -= 1
            else:
                num += 1
        elif char == 'V':
            num += 5
        elif char == 'X':
            if i != len(roman) - 1 and (roman[i+1] == "L" or roman[i+1] == "C"):
                num -= 10
            else:
                num += 10
        elif char == 'L':
            num += 50
        elif char == 'C':
            if i != len(roman) - 1 and (roman[i + 1] == "D" or roman[i + 1] == "M"):
                num -= 100
            else:
                num += 100
        elif char == 'D':
            num += 500
        elif char == 'M':
            num += 1000

    return num
# %%
# Roman Numerals
s = "III"
s_1 = "X"
s_2 = "L"
s_3 = "C"
result = deconstructromantoint(s)
print(result)
result = deconstructromantoint(s_1)
print(result)
result = deconstructromantoint(s_2)
print(result)
result = deconstructromantoint(s_3)
print(result)

# %%
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# %%
# Preceding Roman Numerals
s = "MCMXCIV"
s_1 = "X"
s_2 = "XL"
s_3 = "XC"

result = deconstructromantoint(s)
print(result)
result = deconstructromantoint(s_1)
print(result)
result = deconstructromantoint(s_2)
print(result)
result = deconstructromantoint(s_3)
print(result)
# return result
