import wolframalpha

input= input("Question: ")
app_id = "PYW4WA-A4HX8JR4U7"

client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)
