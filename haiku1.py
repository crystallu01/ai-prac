import random
from nltk.corpus import wordnet
from syllables import estimate

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('stopwords')

# Define the haiku structure as three lines with syllable counts
haiku_structure = [5, 7, 5]

# Load a corpus of haikus and split them into lines
with open("haiku_data.txt") as f:
    lines = [line.strip() for line in f]


# Get the synsets for the the current thmee for now
def synonyms(theme):
    synsets = wordnet.synsets(theme, pos='n')
    similar_words = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            similar_words.add(lemma.name())
    similar_words

# Define a function to get the syllable count of a word using a syllable dictionary
def get_syllables(word):
    return syllable_dict.get(word.lower(), 1)

def line_syllables(line):
    total_syll = 0
    for x in line:
        total_syll += estimate(x)
    return total_syll


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
          word = model.make_sentence(max_overlap_ratio = 0.3)
          if word != None:
              haiku_line = word.split(".")
              print(haiku_line)

              #haiku line is a 
              for l in haiku_line:
                  if line_syllables(l) == syllables:
                      line = l
        haiku.append(line)
    return haiku

# Train a Markov chain language model on the corpus of haikus
from markovify import NewlineText
model = NewlineText("\n".join(lines))

# Generate a haiku using the model and the defined structure
haiku = generate_haiku(model, haiku_structure)

# print(haiku)