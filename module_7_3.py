class WordsFinder:
    def __init__(self, *name):
        self.file_names = list(name)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding="utf-8") as file:
                text = file.read().split()
                new_text = []
                for word in text:
                    for punctuation_mark in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        if punctuation_mark in word:
                            word = word.replace(punctuation_mark,'')
                    new_text.append(word.lower())
                all_words[name] = new_text
                return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего