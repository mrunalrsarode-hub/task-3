

def count_digits(number):
    count = 0
    
    while number > 0:
        number = number // 10
        count = count + 1
        
    return count

print("Total digits =", count_digits(12345))