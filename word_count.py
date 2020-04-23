# Class to process on text file and return the top k frequent words
# WITHOUT ANY THREADING OR MULTIPROCESSING

# importing libraries
import re
from itertools import islice
from max_heap import max_heap

class topkwords():
    # initialization
    def __init__(self, path, k):
        self.path = path
        self.k = k
        self.res = []
        self.word_dic = {}
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        # if valid path then enter into try statement
        try:
            with open(self.path, 'r') as f:
                print("Processing text file ...")
                while True:
                    data = list(islice(f, 1000))  # slicing into the chunks of size 10k lines
                    if not data: break
                    for line in word:
                        for word in re.findall(r'\w+', line):
                            self.word_dic[word] = self.word_dic.get(word, 0) + 1
            print("Processing of text file completed!")

            # calling max_heap to fetch top k words
            self.res = max_heap(self.word_dic, self.k)
            print("Total unique words processed: {}.".format(len(self.word_dic.keys())))

        except Exception as e:
            print('Exception ' + str(e))