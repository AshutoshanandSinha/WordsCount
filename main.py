# Main wrapper function for the other functions.

from word_count import WordCount
from max_heap import MaxHeap
import time


def main():
	start = time.time()
	print("Starting up.")
	heap = MaxHeap()
	data = WordCount('data/book.txt')
	k = 5

	# Parse file.
	if data.word_dict:
		print("Top {} words are :".format(50))
		print(data.word_dict)

	# Insert into max heap.
	heap.insert_dict(data.get_word_dict())
	heap.pop_top_k_words(k)

	print(time.time()-start)


if __name__ == "__main__":
	main()
