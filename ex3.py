import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required datasets (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Input Text
text = "Natural Language processing is interesting and useful for text analysis"

# Tokenization
tokens = word_tokenize(text)

# Convert to lowercase
tokens = [word.lower() for word in tokens]

# Stopword removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Output
print("Original Text:")
print(text)

print("\nTokens after Stopword Removal:")
print(filtered_tokens)

print("\nTokens after Lemmatization:")
print(lemmatized_tokens)

