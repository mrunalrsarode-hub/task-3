

def combinations(items):
    count = 0
    
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            print(items[i] + items[j])
            count = count + 1
            
    print("Total combinations =", count)

data = ["a", "b", "c"]

combinations(data)