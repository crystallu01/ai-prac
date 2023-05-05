import random
from nltk.corpus import wordnet
from syllables import estimate
import regex as re
import spacy

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('stopwords')

# Define the haiku structure as three lines with syllable counts
haiku_structure = [5, 7, 5]
nlp = spacy.load('en_core_web_sm')

# Load a corpus of haikus and split them into lines
with open("haiku_data.txt") as f:
    lines = [line.strip() for line in f]

#theme = input()
theme = "rain"

# Get the synsets for the the current theme for now
def synonyms(theme):
    synsets = wordnet.synsets(theme, pos='n')
    similar_words = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            similar_words.add(lemma.name())
    return similar_words

# Define a function to get the syllable count of a word using a syllable dictionary
def get_syllables(word):
    return syllable_dict.get(word.lower(), 1)

def line_syllables(line):
    total_syll = 0
    line = [x for x in re.findall(r"[a-z]+", line.lower())]
    for x in line:
        total_syll += estimate(x)
    return total_syll

def line_syn(line, theme):
    words = [x for x in re.findall(r"[a-z]+", line.lower())]
    for word in words: 
        tokens = nlp(word + " " + theme)
        similarity = tokens[0].similarity(tokens[1])
        if similarity > 0.4:
            return True

    return False

# Create a dictionary of syllable counts for each word in the corpus
syllable_dict = {}
for line in lines:
    words = line.split()
    for i, word in enumerate(words):
        if word not in syllable_dict:
            syllable_dict[word] = get_syllables(word)

# Define a function to generate a haiku using a Markov chain language model
def generate_haiku(model, structure):
    haiku = []
    for syllables in structure:
        line = ""
        while line == "":
            #word returns a list of words
            word = model.make_sentence(max_overlap_ratio = 0.3)
            if word != None:
                haiku_line = word.split(".")
                #haiku line is a string of words
                for l in haiku_line:
                    if line_syllables(l) == syllables and line_syn(l, theme):
                        line = l
                        print(line)
                        break
        haiku.append(line)
    return haiku

# Train a Markov chain language model on the corpus of haikus
from markovify import NewlineText
from markov_with_positions import Markov
model = Markov(lines)
while True:
    input('Go:')
    print(f'Make sentences: {model.make_sentences()}')
model = NewlineText("\n".join(lines))

# Generate a haiku using the model and the defined structure
haiku = generate_haiku(model, haiku_structure)

print(haiku)