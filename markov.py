import random

class Markov:
    def __init__(self, poems_from_data):
        self.poems_from_data = poems_from_data
        self._build()

    def _build(self):
        chain = dict()
        for poem in self.poems_from_data:
            for line in poem.split(' . '):
                words = line.split(' ')
                for index, word in enumerate(words):
                    if index + 1 < len(words):
                        next_word = words[index+1]
                        if word not in chain:
                            chain[word] = [next_word]
                        else:
                            chain[word].append(next_word)
        self.chain = chain

    def _select_next_word(self, min_length, cur_word, cur_length):
        if cur_length > min_length and '$' in self.chain[cur_word]:
            return '$'
        return random.choice(self.chain[cur_word])

    def make_sentences(self, total_sentences=3, min_length=5):
        sentences = []
        for _ in range(total_sentences):
            # starter_word = random.choice(list(self.chain.keys()))
            starter_word = 'rain'
            acc = [starter_word]
            current_word = starter_word
            while current_word != '$':
                # horrible
                try:
                    next_word = self._select_next_word(min_length, current_word, len(acc))
                    if next_word == '$' and len(acc) < min_length:
                        continue
                except KeyError:
                    break
                acc.append(next_word)
                current_word = next_word

            sentences.append(' '.join(acc))
        return sentences
