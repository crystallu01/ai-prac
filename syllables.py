import nltk
nltk.download('cmudict')
from nltk.corpus import cmudict

d = cmudict.dict()
def syllable_count(word):
    print(d[word.lower()])
    return len([ph for ph in d[word.lower()][0] if ph[-1].isdigit()])



def sentence_syllable_count(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        count += syllable_count(word)
    return count


sentence = "estimating stuff on syllables"
syllables = sentence_syllable_count(sentence)
print("The sentence '{}' has {} syllables.".format(sentence, syllables))
