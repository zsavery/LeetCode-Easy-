# %%
x = 0
y = ''
r = 0
if x >= 2 ** 31 - 1 or x <= -2 ** 31:
    pass
else:
    str_x = str(x)
    if x >= 0:
        y = str_x[::-1]
    else:
        str_x = str_x[1:]
        y = str_x[::-1]
        y = '-' + y
    r = int(y)
if r >= 2 ** 31 - 1 or r <= -2 ** 31:
    return 0
else:
    return r

print(r)