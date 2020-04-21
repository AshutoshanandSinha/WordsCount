# Takes in a hash table and creates a max heap returning the top k
# key value pairs with the highest values.

def max_heap(word_dic, k):
	print("Generating max heap")
	result =[]
	for word in sorted(word_dic, key=word_dic.get, reverse=True):
		if k == 0:break
		result.append(word)
		k -= 1
	return result