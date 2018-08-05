def count_vowels(string):
    count = 0
    for i in string:
        if i in "aeiou":
            count += 1
    return count
