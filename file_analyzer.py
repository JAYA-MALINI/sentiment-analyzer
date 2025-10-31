from textblob import TextBlob

def analyze_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            blob = TextBlob(text)
            sentiment = blob.sentiment.polarity

            print("\n=== Sentiment Analysis Result ===")
            if sentiment > 0:
                print("Overall Sentiment: 😊 Positive")
            elif sentiment < 0:
                print("Overall Sentiment: 😞 Negative")
            else:
                print("Overall Sentiment: 😐 Neutral")
    except FileNotFoundError:
        print("❌ File not found! Please check the path.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        analyze_file(sys.argv[1])
    else:
        file_path = input("Enter path to text file: ").strip()
        analyze_file(file_path)
