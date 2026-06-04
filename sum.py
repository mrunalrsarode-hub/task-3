

def sum_list(numbers):
    total = 0
    
    for i in numbers:
        total = total + i
        
    return total

sample_list = [8, 2, 3, 0, 7]

print("Sum of list =", sum_list(sample_list))