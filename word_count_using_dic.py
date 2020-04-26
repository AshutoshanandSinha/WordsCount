# Class to process on text file and store them a dictionary.
# WITHOUT ANY THREADING OR MULTIPROCESSING

import re
import string
from max_heap import MaxHeap


class WordCount:
    # Initialization.
    def __init__(self, path, k):
        self.path = path
        self.word_dict = {}
        self.k = k
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        # if valid path then enter into try statement
        try:
            def read_chunks(file, chunk_size=1024*1024):
                while True:
                    data = file.read(chunk_size)
                    if not data:
                        break
                    yield data
            with open(self.path, encoding="utf8") as f:
                print("Processing text file ...")
                for chunk in read_chunks(f): # reading file in chunks
                    for word in re.sub('[' + string.punctuation + ']', '', chunk).split():
                        self.word_dict[word] = self.word_dict.get(word, 0) + 1 #extracting word from each chunk and updating dictionary
            print("Processing of text file completed!")

            # calling max_heap to fetch top k words
            hp = MaxHeap()
            hp.insert_dict(self.word_dict)
            hp.pop_top_k_words(self.k)
        except Exception as e:
            print('Exception ' + str(e))

    # Accessor for dictionary word_dict.
    def get_word_dict(self):
        return self.word_dict


# Driver code for testing class.
if __name__ == "__main__":
    pass