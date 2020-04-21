# Class to process on text file and return the top k frequent words

#importing libraries
import re
import concurrent.futures
from itertools import islice
from max_heap import max_heap
from collections import deque

class topkwords:
    # initialization
    def __init__(self, path, k):
        self.path = path
        self.k = k
        self.res=[]
        self.word_dic = {}
        self.process_text()

    # Function will process the text file and will store the word count in dictionary
    def process_text(self):
        #if valid path then enter into try statement
        try:
            with open(self.path, 'r') as f:
                print("Processing text file ...")
                while True:
                    data = list(islice(f, 1000000))
                    if not data: break
                    cur_list = []
                    for line in data:
                        templist = re.findall(r'\w{2,}', line)
                        cur_list.extend(templist) # will check for word of length greater than 1 i.e >1

                    '''with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                        executor.map(self.word_counting, cur_list)
                        executor.shutdown(wait=True)
                        
                        results = [executor.submit(self.word_counting, word)for word in cur_list]
                        for fu in concurrent.futures.as_completed(results):
                            fu.result()
                    '''
                    for word in cur_list:
                        self.word_dic[word] = self.word_dic.get(word, 0) + 1

            print("Processing of text file completed!")
            self.res = max_heap(self.word_dic, self.k )  #calling max_heap to fetch top k words
            print("Total words processed: {} .".format(len(self.word_dic.keys())))

        except Exception as e:
                print('Exception ' + str(e))

    def word_counting(self, wordlist):
        for word in wordlist:
            self.word_dic[word] = self.word_dic.get(word, 0) + 1
