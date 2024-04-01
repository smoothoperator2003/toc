# Aim: Write a program for tokenatization of given input

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_text(text):
    
    sentences = sent_tokenize(text)
    
    words = [word_tokenize(sentence) for sentence in sentences]
    return sentences, words

if __name__ == "__main__":
    
    input_text = "This is an example sentence. Tokenization is the process of breaking text into words."
    
    sentences, words = tokenize_text(input_text)
    
    print("Original text:")
    print(input_text)
    print("\nTokenized sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f" Sentence {i}: {sentence}")
    print("\nTokenized words:")
    for i, sentence_words in enumerate(words, start=1):
        print(f" Sentence {i}: {sentence_words}")
