# Class to process on text file and store them a dictionary.
# WITHOUT ANY THREADING OR MULTIPROCESSING

import re
from itertools import islice
from multiprocessing.dummy import Pool


class WordCount:
    # Initialization.
    def __init__(self, path):
        self.path = path
        self.word_dict = {}
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        # if valid path then enter into try statement
        try:
            with open(self.path, 'r') as f:
                print("Processing text file ...")
                while True:
                    data = list(islice(f, 10000))  # slicing into the chunks of size 10k lines
                    if not data:
                        break
                    pool = Pool()
                    pool.map(self.word_counting, data)
                    pool.close()
                    pool.join()
            print("Processing of text file completed!")
            print("Total unique words processed: {}.".format(len(self.word_dict.keys())))

        except Exception as e:
            print('Exception ' + str(e))

    # Function extracts words from line and store its count in the dictionary.
    def word_counting(self, line):
            for word in re.findall(r'\w+', line):
                self.word_dict[word] = self.word_dict.get(word, 0) + 1

    # Accessor for dictionary word_dict.
    def get_word_dict(self):
        return self.word_dict


# Driver code for testing class.
if __name__ == "__main__":
    pass
