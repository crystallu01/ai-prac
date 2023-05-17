import random
from collections import defaultdict
from functools import reduce

class Markov:
    def __init__(self, poems_from_data):
        self.poems_from_data = poems_from_data
        self._build()

    def _build(self):
        print('Building...')
        chain = defaultdict(lambda: [[] for _ in range(13)])
        starting_words = []
        for poem in self.poems_from_data:
            for line in poem.split(' . '):
                words = line.split(' ')
                for index, word in enumerate(words):
                    if index == 0:
                        starting_words.append(word)
                    if index + 1 < len(words):
                        next_word = words[index+1]
                        chain[word][index].append(next_word)
        self.chain = chain
        self.starting_words = starting_words

    def _select_next_word(self, length_threshold, cur_word, cur_length):
        # return 
        if cur_length > length_threshold and '$' in reduce(lambda a,b:a+b, self.chain[cur_word]):
            return '$'

        i = cur_length - 1
        while i <= 8:
            if self.chain[cur_word][i]:
                return random.choice(self.chain[cur_word][i])
            i += 1
        raise Exception

    def make_sentence(self, total_sentences=1, length_threshold=10):
        # print('Making sentences...')
        # sentences = []
        # for _ in range(total_sentences):
        starter_word = random.choice(self.starting_words)
        # starter_word = 'rain'
        acc = [starter_word]
        current_word = starter_word
        while current_word != '$':
            # horrible
            try:
                next_word = self._select_next_word(length_threshold, current_word, len(acc))
                # below code causes infinite loops when using positions
                # if next_word == '$' and len(acc) < approx_length:
                #     continue
            except Exception:
                break
            acc.append(next_word)
            current_word = next_word
            # sentences.append(' '.join(acc))
        return ' '.join(acc)
