from nltk.corpus import wordnet
import regex as re
import spacy

from nltk.corpus import cmudict

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('cmudict')


# Define the haiku structure as three lines with syllable counts
haiku_structure = [5, 7, 5]
nlp = spacy.load('en_core_web_sm')
d = cmudict.dict()


# Load a corpus of haikus and split them into lines
with open("haiku_data.txt") as f:
    lines = [line.strip() for line in f]


# Get the synsets for the the current theme for now
def synonyms(theme):
    synsets = wordnet.synsets(theme, pos='n')
    similar_words = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            similar_words.add(lemma.name())
    return similar_words

def line_syllables(line):
    """
    given a string, find the total number of syllables in the line
    """
    def syllable_count(word):
        if word.lower() in d:
            return len([ph for ph in d[word.lower()][0] if ph[-1].isdigit()])
        else:
            return None
    line = [x for x in re.findall(r"[a-z]+", line.lower())]
    count = 0
    for word in line:
        syl_count = syllable_count(word)
        if syllable_count(word) != None:
            count += syl_count
    return count

def line_syn(line, theme):
    words = [x for x in re.findall(r"[a-z]+", line.lower())]
    for word in words: 
        tokens = nlp(word + " " + theme)
        similarity = tokens[0].similarity(tokens[1])
        if similarity > 0.6:
            return True
    # print(similarity)
    return False

# Define a function to generate a haiku using a Markov chain language model
def generate_haiku(model, structure, theme):
    haiku = ["", "", ""]
    for i, syllables in enumerate(structure):
        while haiku[i] == "":
            #word returns a list of words
            line = model.make_sentence()
            if line_syllables(line) == syllables and line_syn(line, theme):
                haiku[i] = line
                print(line)
                break
    return haiku


if __name__ == "__main__":
    # Train a Markov chain language model on the corpus of haikus
    from markov_with_positions import Markov
    model = Markov(lines)
    # while True:
    #     input('Go:')
    #     print(f'Make sentences: {model.make_sentence()}')

    # model = model.make_sentences() 

    # Generate a haiku using the model and the defined structure
    while True:
        theme = input("theme: ")
        haiku = generate_haiku(model, haiku_structure, theme)
