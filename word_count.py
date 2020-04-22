# Class to process on text file and return the top k frequent words

# importing libraries
import re
import concurrent.futures
from itertools import islice
from max_heap import max_heap
from multiprocessing import Pool

class topkwords:
    # initialization
    def __init__(self, path, k):
        self.path = path
        self.k = k
        self.res = []
        self.proc_words_dic=[]
        self.word_dic = {}
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        # if valid path then enter into try statement
        try:
            with open(self.path, 'r') as f:
                print("Processing text file ...")
                while True:
                    data = list(islice(f, 10000)) # slicing into the chunks of size 10k lines
                    if not data: break
                    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
                        results = {executor.submit(self.word_counting, line):line for line in data}
                        for fr in concurrent.futures.as_completed(results):
                            self.proc_words_dic.append(fr.result())
            print("Processing of text file completed!")

            #iterating over each dictionary stored in proc_word_dic
            for dic in self.proc_words_dic:
                for word in dic.keys():
                    self.word_dic[word] = self.word_dic.get(word, 0) + 1

            # calling max_heap to fetch top k words
            self.res = max_heap(self.word_dic, self.k)

            print("Total unique words processed: {}.".format(len(self.word_dic.keys())))

        except Exception as e:
            print('Exception ' + str(e))

    def word_counting(self, line):
        new_dic = {}
        for word in re.findall(r'\w{2,}', line):
            new_dic[word] = new_dic.get(word, 0) + 1
        return new_dic