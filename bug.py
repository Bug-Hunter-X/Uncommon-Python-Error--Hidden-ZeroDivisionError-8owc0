def function_with_uncommon_error(x, y):
    if x == 0:
        return y / x  # ZeroDivisionError
    else:
        return x / y

result = function_with_uncommon_error(0, 10)
print(result)