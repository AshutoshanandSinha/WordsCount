# Main wrapper function for the other functions.

from word_count import WordCount
from max_heap import MaxHeap
import time


def main():
	start = time.time()
	print("Starting up.")
	k = 5

	# Parse file
	data = WordCount('data/book.txt')

	# Insert into max heap.
	heap = MaxHeap()
	heap.insert_dict(data.get_word_dict())
	heap.pop_top_k_words(k)

	print(time.time()-start)


if __name__ == "__main__":
	main()
