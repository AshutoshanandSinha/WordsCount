# Class to process on text file and return the top k frequent words
# USING THREADS

# importing libraries
import re
from itertools import islice
from max_heap import max_heap
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

class topkwords():
    # initialization
    def __init__(self, path, k):
        self.path = path
        self.k = k
        self.word_dic = {}
        self.lock = multiprocessing.Lock()
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        # if valid path then enter into try statement
        try:
            with open(self.path, 'r') as f:
                print("Processing text file ...")
                while True:
                    data = list(islice(f, 10000))  # slicing into the chunks of size 10k lines
                    if not data: break
                    pool = ThreadPool(8)
                    pool.map(self.word_counting, data)
                    pool.close()
                    pool.join()
            print("Processing of text file completed!")

            # calling max_heap to fetch top k words
            self.res = max_heap(self.word_dic, self.k)
            print("Total unique words processed: {}.".format(len(self.word_dic.keys())))

        except Exception as e:
            print('Exception ' + str(e))

    #function extracts words from line and store its count in the dictionary
    def word_counting(self, line):
            for word in re.findall(r'\w+', line):
                self.lock.acquire()
                self.word_dic[word] = self.word_dic.get(word, 0) + 1
                self.lock.release()
