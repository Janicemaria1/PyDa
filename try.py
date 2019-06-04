import wikipedia
import wolframalpha

while True:
	inp = input("Question: ")
	
	try:
		app_id = "PYW4WA-A4HX8JR4U7"

		client = wolframalpha.Client(app_id)

		res = client.query(inp)
		answer = next(res.results).text

		print(answer)
		
	except:
		wikipedia.set_lang("en")
		print(wikipedia.summary(inp, sentences = 2))
