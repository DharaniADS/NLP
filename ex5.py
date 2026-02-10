# Python program to create Word and Character N-grams

def word_ngrams(text, n):
    words = text.split()
    grams = []

    for i in range(len(words) - n + 1):
        grams.append(tuple(words[i:i + n]))

    return grams


def char_ngrams(text, n):
    grams = []

    for i in range(len(text) - n + 1):
        grams.append(text[i:i + n])

    return grams


# ---- Main Program ----
text = input("Enter a sentence: ")
n = int(input("Enter value of N: "))

print("\nWord N-grams:")
for gram in word_ngrams(text, n):
    print(gram)

print("\nCharacter N-grams:")
for gram in char_ngrams(text, n):
    print(gram)
