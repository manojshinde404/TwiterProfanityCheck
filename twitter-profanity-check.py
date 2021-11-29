from profanity_check import predict_prob

#open twitter sentence file in read mode
file = open("twitter-sentences.txt","r")

#reading each line in file
for sentence in file.readlines():
	print(sentence)

	#degree of profanity of each sentence
	profanity = predict_prob(sentence)
	print(profanity)

