from textblob import TextBlob

print("=== Simple Sentiment Analyzer ===")

while True:
    text = input("\nEnter a sentence (or 'exit' to quit): ")
    if text.lower() == "exit":
        break

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        print("Sentiment: 😊 Positive")
    elif sentiment < 0:
        print("Sentiment: 😞 Negative")
    else:
        print("Sentiment: 😐 Neutral")
