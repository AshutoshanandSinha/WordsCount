This program parses a .CSV or .txt file and returns the
top K recurring unique words found in the file.

The file structure is as follows:

main.py
    - Main wrapper function for the other functions.

max_heap.py
    - MaxHeap class creates a max heap that takes in key:value pairs.

word_count.py
    - Class to process on text file and return the top k frequent words
    WITHOUT ANY THREADING OR MULTIPROCESSING

.gitignore
    - .gitignore file for excluding anything from the repo.

data/
    - Directory for the data files we want to parse.

data/book.txt
    - sample .txt file for parsing data.

data/.gitignore
    - .gitignore file primarily for larger data sets we
     don't want pushed into the repo.
