# Main wrapper function for the other functions.
from word_count import topkwords

def main():
	print("Starting up.")
	data = topkwords('data/dataset-400MB.txt',10 )
	if data.res:
		print("Top {} words are :".format(10))
		print(data.res)
if __name__ == "__main__":
	main()
