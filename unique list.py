

def unique_list(data):
    unique = []
    
    for i in data:
        if i not in unique:
            unique.append(i)
            
    return unique

sample_list = [1,2,3,3,3,3,4,5]

print("Unique List =", unique_list(sample_list))