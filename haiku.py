import nltk
nltk.download('punkt')
from nltk.corpus import wordnet
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
theme = "Nature"

haiku_poems = ["The old pond, a frog jumps in, sound of water.", 
               "Cherry blossoms bloom, softly falling petals, the spring breeze.", 
               "Winter solitude--in a world of one color the sound of wind."]

tokens = [nltk.word_tokenize(poem.lower()) for poem in haiku_poems]
words = [word for token in tokens for word in token]
nouns = [word for (word, pos) in nltk.pos_tag(words) if pos.startswith("NN")]
freq_dist = nltk.FreqDist(nouns)
common_nouns = freq_dist.most_common(10)

synonyms = []
for word, freq in common_nouns:
    syns = wordnet.synsets(word, pos='n')
    for syn in syns:
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
similar_words = set(synonyms)

# Step 5: Test for relevance
for word in similar_words:
    print(word)

