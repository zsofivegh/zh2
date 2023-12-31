import datetime     #aktualis datum
import string

p = open('positive_words.txt')      #beraktam tombbe
positive = []
for line in p:
    positive_word = line.strip()
    positive.append(positive_word)
#print(positive)

n = open('negative_words.txt')
negative = []
for line in n:
    negative_word = line.strip()
    negative.append(negative_word)
#print(negative)


def emotion_statement(text, positive, negative):      #erzelem megallapitas
    words = text.split()
    positive_count = 0
    negative_count = 0
    for word in words:
        w = word.rstrip(string.punctuation).lower()
        if w in positive:
            positive_count += 1
        if w in negative:
            negative_count += 1

    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"

def link_sharing(username, link, comment):       #link megosztas

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    emotion = emotion_statement(comment, positive, negative)

    content = f"{username};{date};{link};{comment});{emotion}\n"

    with open("contents.txt", "a") as c:
        c.write(content)

#link_sharing("Zsofi", "https://github.com/", "Really good content.")

def text_sharing(username, text):

    emotion = emotion_statement(text, positive, negative)

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    content = f"{username};{date};{text};{emotion}\n"

    with open("contents.txt", "a") as c:
        c.write(content)

#text_sharing("Zsofi", "The turkey smells terrible.")
