import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def tokenize_text(text):
    return word_tokenize(text)

sample_inputs = [
    "Natural Language Processing is interesting.",
    "Tokenization breaks text into tokens.",
    "Python is widely used in NLP."
]

for text in sample_inputs:
    print("Input Text:")
    print(text)
    print("Tokens:")
    print(tokenize_text(text))
    print()