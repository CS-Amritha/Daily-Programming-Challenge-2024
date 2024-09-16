def reverse_words(string):
    reversed_words = string.split()[::-1]
    return " ".join(reversed_words)
string = " Challenge 8 - wisdom sprouts"
print(reverse_words(string))
