def generate_ngrams(text, n):
    words = text.split()
    ngrams_list = []

    for i in range(len(words) - n + 1):
        ngram = words[i:i+n]
        ngrams_list.append(ngram)

    return ngrams_list

text = input("Enter the sentence: ")
n = int(input("Enter the value of N: "))

ngrams = generate_ngrams(text, n)

print("\nGenerated N-grams are:")
for gram in ngrams:
    print(gram)