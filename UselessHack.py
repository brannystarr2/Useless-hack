import random

responses = ["It is certain.", "Without a doubt.", "You may rely on it.", "Yes, definitely.", "It is decidedly so.", "As I see it, yes.", "Most likely.", "Yes.", "Outlook good.", "Signs point to yes.", "Reply hazy, try again.", "Better not tell you now.", "Ask again later.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "Outlook not so good.", "My sources say no.", "Very doubtful.", "My reply is no."]

while True:
    question = input("Ask me a yes or no question: ")
    if "?" in question:
        print(random.choice(responses))
    else:
        print("That doesn't look like a question to me. Try again!")
