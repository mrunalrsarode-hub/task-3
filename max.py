

def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

result = find_max(10, 25, 5)
print("Maximum number is =", result)