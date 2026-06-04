

def count_case(word):
    upper = 0
    lower = 0
    
    for i in word:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
            
    print("Upper case :", upper)
    print("Lower case :", lower)

count_case("STatiStiCS")