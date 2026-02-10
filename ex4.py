from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
sentence = "The children are playing gaming enjoying the games"
words = sentence.split()
print("Original Word  ->  Stemmed Word")
print("--------------------------------")
for word in words:
    stemmed_word = stemmer.stem(word.lower())
    print(f"{word:<15} ->  {stemmed_word}")
