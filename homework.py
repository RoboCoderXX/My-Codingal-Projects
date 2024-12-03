from textblob import TextBlob
def emotion_detect(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.25:
        return "pos"
    elif sentiment < -0.25:
        return "neg"
    else:
        return "neu"
print("Hello, nice to meet you may I know your name?")
name = input()
print(f"Nice to meet you {name}.")
mood = input(f"How are you feeling today {name}: \n")
emotion = emotion_detect(mood)
if emotion == "pos":
    print("Glad to hear that!")
elif emotion == "neg":
    print("Sorry to hear that hope you get better")
elif emotion == "neu":
    print("Seems like everthing is fine")
print("I wish we could have talked more but I have to go.")
print("Bye! Glad I got the chance to talk to you. Hope we talk again.")