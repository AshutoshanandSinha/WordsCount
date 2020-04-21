# Class to process on text file and return the top k frequent words

#importing libraries
import re
from max_heap import max_heap

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
                for line in f:
                    words = re.findall(r'\w{2,}', line)  # will check for word of length greater than 1 i.e >1
                    for word in words:
                        self.word_dic[word] = self.word_dic.get(word, 0) + 1
            print("Processing of text file completed!")
            self.res = max_heap(self.word_dic, self.k )  #calling max_heap to fetch top k words

        except Exception as e:
                print('Exception ' + str(e))
