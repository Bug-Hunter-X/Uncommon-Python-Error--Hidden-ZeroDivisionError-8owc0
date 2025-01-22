def function_with_uncommon_error(x, y):
    if x == 0:
        return float('inf') if y > 0 else float('-inf') if y < 0 else float('nan') #Handle division by zero gracefully
    else:
        return x / y

result = function_with_uncommon_error(0, 10)
print(result) # Output: inf