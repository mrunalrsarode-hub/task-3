

def permutations(items):
    count = 0
    
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j:
                print(items[i] + items[j])
                count = count + 1
                
    print("Total permutations =", count)

data = ["a", "b", "c"]

permutations(data)