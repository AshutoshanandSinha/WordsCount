This program parses a .CSV or .txt file and returns the
top K recurring unique words found in the file.

The file structure is as follows:

main.py
    - Main wrapper function for the other functions.

max_heap.py
    - Takes in a hash table and creates a max heap returning
      the top k key value pairs with the highest values.

word_count.py
    - Takes in a .CSV or .txt file and creates a hash table
      with a key:value structure of:
      string name : number of occurrences.

.gitignore
    - .gitignore file for excluding anything from the repo.

data/
    - Directory for the data files we want to parse.

data/book.txt
    - sample .txt file for parsing data.

data/.gitignore
    - .gitignore file primarily for larger data sets we
      don't want pushed into the repo.
