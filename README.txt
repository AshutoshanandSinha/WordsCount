This program parses a .CSV or .txt file and returns the
top K recurring unique words found in the file.

The file structure is as follows:

main.py
    - Main wrapper function for parsing and data structures.
    Times the run time of the program.

max_heap.py
    - Class to create a max heap that stores dictionary items or other
    key value pairs. Designed to be used with WordCountDict() class.

word_count.py
    - Class to parse text file and store parsed data as a collection.

word_count_dict.py
    - Class to parse text file and store parsed data as a dictionary.

.gitignore
    - .gitignore file for excluding anything from the repo.

data/
    - Directory for the data files we want to parse.

data/book.txt
    - sample .txt file for parsing data.

data/

data/.gitignore
    - .gitignore file primarily for larger data sets we
     don't want pushed into the repo.
