

def count_vowel_consonant(word):
    vowels = "aeiou"
    
    vowel_count = 0
    consonant_count = 0
    
    for i in word:
        if i in vowels:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
            
    print("Count of vowel is =", vowel_count)
    print("Count of consonant is =", consonant_count)

count_vowel_consonant("statistics")