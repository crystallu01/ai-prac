import nltk
from nltk.corpus import wordnet
from syllables import estimate

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('stopwords')
nltk.download('cmudict')


theme = "love"
with open('haiku_data.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Split the contents of the file based on '$' and remove any empty strings
haiku_poems = [string for string in contents.split('$') if string]

tokens = [nltk.word_tokenize(poem.lower()) for poem in haiku_poems]
words = [word for token in tokens for word in token if word != '/']
nouns = [word for (word, pos) in nltk.pos_tag(words) if pos.startswith("NN")]
freq_dist = nltk.FreqDist(nouns)
common_nouns = freq_dist.most_common(10)
#do something with nouns later
# for noun in nouns:

# Get the synsets for the the current thmee for now
def synonyms(theme):
    synsets = wordnet.synsets(theme, pos='n')
    similar_words = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            similar_words.add(lemma.name())
    syllables_dict = {word: estimate(word) for word in similar_words}
    return syllables_dict

def syllableSum(syllables_dict, target):
    complement_dict = {}
    for key, value in syllables_dict.items():
        complement = target - value
        if complement in complement_dict:
            return [complement_dict[complement], key]
        complement_dict[value] = key
    return []

syllables_dict = synonyms(theme)
five_syll = syllableSum(syllables_dict, 5)
print("haiku: ")
print(five_syll)
print("\n")

total_syl = 0
for x in five_syll:
    print(x + " is " + str(estimate(x)) + " syllables")
    total_syl += estimate(x)
