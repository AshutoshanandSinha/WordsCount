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
        self.k = k
        self.res = []
        self.word_dic = collections.Counter()
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        # if valid path then enter into try statement
        try:
            def read_chunks(file, chunk_size=1024*1024):
                while True:
                    data = file.read(chunk_size)
                    if not data:break
                    yield data
            with open(self.path) as f:
                print("Processing text file ...")
                for chunk in read_chunks(f):
                    self.word_dic.update(re.sub('[' + string.punctuation + ']', '', chunk).split())
            print("Processing of text file completed!")

            # calling max_heap to fetch top k words
            '''heap = MaxHeap(self.k)
            for (key, value) in self.word_dic.items():
                pair = [key, value]
                heap.insert_node(pair)

            print("Top " + str(self.k) + " Repeating Words:")
            for i in range(self.k-1):
                self.res.append(heap.pop_max_node())'''
            self.res = self.word_dic.most_common(self.k)
            print("Total unique words processed: {}.".format(len(self.word_dic.keys())))
            return self.res

        except Exception as e:
            print('Exception ' + str(e))
