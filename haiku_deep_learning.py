import spacy
from spacy.matcher import Matcher
import syllapy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import random

# python3 -m spacy download en_core_web_sm
def initSyllableLists(num_lines=1000):
    nlp = spacy.load("en_core_web_sm")
    matcher2 = Matcher(nlp.vocab)
    matcher3 = Matcher(nlp.vocab)
    matcher4 = Matcher(nlp.vocab)

    pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
            {'POS':  {"IN": ["NOUN", "VERB"]} }]
    matcher2.add("TwoWords", [pattern])
    pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
            {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
            {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
    matcher3.add("ThreeWords", [pattern])
    pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
            {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
            {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
            {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
    matcher4.add("FourWords", [pattern])

    with open("haiku_data.txt", "r") as file:
        lines = file.readlines()[:num_lines]  # Read the first num_lines

    text = "".join(lines)

    doc = nlp(text)

    matches2 = matcher2(doc)
    matches3 = matcher3(doc)
    matches4 = matcher4(doc)

    five = []
    seven = []

    for match_id, start, end in matches2 + matches3 + matches4:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        syl_count = 0
        for token in span:
            syl_count += syllapy.count(token.text)
        if syl_count == 5:
            if span.text not in five:
                five.append(span.text)
        if syl_count == 7:
            if span.text not in seven:
                seven.append(span.text)
        
    return five, seven


def get_embedding_table():
    embeddings_index = {}
    with open('glove/glove.6B.100d.txt', encoding='utf8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    return embeddings_index

def average_word_vector(sentence, embeddings_index):
    words = sentence.split()
    vectors = []
    for word in words:
        if word in embeddings_index:
            vectors.append(embeddings_index[word])
    if vectors:
        return np.mean(vectors, axis=0)
    return None


def get_similar_sentences(query_vector, sentences, embeddings_index):
    similar_sentences = []
    for sentence in sentences:
        sentence_vector = average_word_vector(sentence, embeddings_index)
        if sentence_vector is not None:
            similarity = cosine_similarity([query_vector], [sentence_vector])[0][0]
            similar_sentences.append((sentence, similarity))
    return sorted(similar_sentences, key=lambda x: x[1], reverse=True)


five, seven = initSyllableLists()
embeddings_index = get_embedding_table()



while True:
    query = input("theme: ")
    query_vector = average_word_vector(query, embeddings_index)

    similar_sentences_5 = get_similar_sentences(query_vector, five, embeddings_index)
    similar_sentences_7 = get_similar_sentences(query_vector, seven, embeddings_index)

    # print(similar_sentences_5[:10])
    # print(similar_sentences_7[:10])

    print(f'Haiku for {query}')

    five = random.choice(similar_sentences_5[:10])
    seven = random.choice(similar_sentences_7[:10])
    five_2 = random.choice(similar_sentences_5[:10])

    print("%s\n%s\n%s" %(five[0], seven[0], five_2[0]))

