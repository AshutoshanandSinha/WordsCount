# Class to process on text file and store them a dictionary.
# WITHOUT ANY THREADING OR MULTIPROCESSING

import re
from max_heap import MaxHeap
import collections
import string


class WordCount:
    # Initialization.
    def __init__(self, path):
        self.path = path
        self.word_dict = collections.Counter()
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
                for chunk in read_chunks(f):
                    self.word_dict.update(re.sub('[' + string.punctuation + ']', '', chunk).split())
            print("Processing of text file completed!")
            print("Total unique words processed: {}.".format(len(self.word_dict.keys())))
        except Exception as e:
            print('Exception ' + str(e))

    # Accessor for dictionary word_dict.
    def get_word_dict(self):
        return self.word_dict


# Driver code for testing class.
if __name__ == "__main__":
    pass