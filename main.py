# Main wrapper function for the other functions.
from word_count import topkwords
import time

def main():
	start = time.time()
	print("Starting up.")
	data = topkwords('data/dataset-400MB.txt',50 )
	if data.res:
		print("Top {} words are :".format(50))
		print(data.res)
	print(time.time()-start)
if __name__ == "__main__":
	main()
