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

    def make_sentences(self):
        MIN_LEN = 3
        starter_word = random.choice(list(self.chain.keys()))
        acc = [starter_word]
        current_word = starter_word
        while True:
            next_word = random.choice(self.chain[current_word])
            if next_word == '$' and len(acc) < MIN_LEN:
                continue
            acc.append(next_word)
            current_word = next_word
            if current_word == '$' and len(acc) >= MIN_LEN:
                break
        return ' '.join(acc)
