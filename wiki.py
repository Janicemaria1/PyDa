import wikipedia

while True:
	inp = input("Question: ")
	wikipedia.set_lang("fr")
	print(wikipedia.summary(inp, sentences = 2))
