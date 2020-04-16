import re
import time
def wordcount(filepath, word_dic, num_of_words, k):
        start = time.time()
        lines = 0
        with open(filepath, 'r') as f:
                for line in f:
                    #word = re.findall("[a-zA-Z\-\.'/]+", line)
                    words = re.findall(r'\w+', line)
                    for word in words:
                      word_dic[word] = word_dic.get(word,0) + 1
                      num_of_words += 1
                    lines +=1
                #if time.time()- start > 10:
                for w in sorted(word_dic, key=word_dic.get, reverse=True):
                    if k == 0:break
                    print(w, word_dic[w])
                    k -= 1
                return (num_of_words, (time.time() - start), lines)

    #print("Invalid path or File not present!")


word_dic = {}
filepath ='book.txt'
num_of_words = 0
k = 10

if __name__ =="__main__":
    words_processed, time_taken , lines = wordcount(filepath,word_dic, num_of_words, k)
    print("{} Words Processed from {} lines in {} seconds.".format(words_processed,lines,  time_taken) )
