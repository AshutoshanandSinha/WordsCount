# Main wrapper function for parsing and data structures.
# Times the run time of the program.

from word_count import WordCount
from word_count_dict import WordCountDict
from max_heap import MaxHeap
import time


def main():
	# NOTE: Change this to name of .txt file you are using within /data/.
	file_path = 'data/book.txt'

	start = time.time()
	print("Starting up.")
	k = int(input("Enter a value for k:\n"))

	# Parse and sort data using collections.
	data = WordCount(file_path)
	data.sort_and_pop_word_dict(k)

	# Parse and sort data using dictionary and max heap.
	# data = WordCountDict('data/book.txt')
	# heap = MaxHeap()
	# heap.insert_dict(data.get_word_dict())
	# heap.pop_top_k_words(k)

	print(time.time()-start)


if __name__ == "__main__":
	main()
