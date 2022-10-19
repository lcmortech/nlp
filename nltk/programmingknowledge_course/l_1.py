import nltk
nltk.download()

text = """Welcome to programming knowledge. Let's start with our first tutorial on NLTK. We shall learn the basics of NLTK here!"""

from nltk.tokenize import word_tokenize
print(word_tokenize(text))