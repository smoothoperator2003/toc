# Aim: Write a program for tokenatization of given input

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_text(text):
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    return sentences, words

if __name__ == "__main__":
    input_text = "This is an example sentence.Tokenization is the process of breaking text into words."
    sentences, words = tokenize_text(input_text)
    print("Original text:")
    print(input_text)
    print("\nTokenized sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f" Sentence {i}: {sentence}")
    print("\nTokenized words:")
    for i, sentence_words in enumerate(words, start=1):
        print(f" Sentence {i}: {sentence_words}")\


# --------------------------------------------------------------


from typing import List

def fillSentence(user_input) -> List[str]:
    sentence: List[str] = []
    common: str = ""
    for i in user_input:
        if i == ".":
            sentence.append(common)
            common = ""
        if i != ".":
            common += i
    if sentence == True:
        sentence.append(common)
    return sentence
    
def fillWords(user_input) -> List[str]:
    words: List[str] = []
    common: str = ""
    for i in user_input:
        if i == " ":
            words.append(common)
            common = ""
        if i != " ":
            common += i
    if words == True:
        words.append(common)
    return words
            
def tokenization() -> List[str]:
    user_input: str = input("Enter your prompt:\n")
    sentenceList: List[str] = fillSentence(user_input)
    wordList: List[str] = fillWords(user_input)
    
    return sentenceList, wordList
    
def main() -> None:
    store_tokenization = tokenization()
    print(store_tokenization)
    
if __name__ == "__main__":
    main()
