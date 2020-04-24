# Class to process on text file and return the top k frequent words
# WITHOUT ANY THREADING OR MULTIPROCESSING

# importing libraries
import re
from max_heap import max_heap
import collections
import string


class topkwords():
    # initialization
    def __init__(self, path, k):
        self.path = path
        self.k = k
        self.res = []
        self.word_dic = collections.Counter()
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        # if valid path then enter into try statement
        try:
            def read_chunks(file, chunk_size=1024*2048):
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
            self.res = max_heap(self.word_dic,self.k)
            print("Total unique words processed: {}.".format(len(self.word_dic.keys())))

        except Exception as e:
            print('Exception ' + str(e))

    #function extracts words from line and store its count in the dictionary
    def word_counting(self, line):
<<<<<<< HEAD
            self.word_dic.update(re.findall(r'\w+', line))
=======
            for word in re.findall(r'\w+', line):
                self.word_dic[word] = self.word_dic.get(word, 0) + 1
>>>>>>> 69904c48db2be0960184badc5206f378bce59960
