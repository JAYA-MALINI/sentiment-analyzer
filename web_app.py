from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sentiment Analyzer</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:50px;">
    <h1>🧠 Simple Sentiment Analyzer</h1>
    <form method="POST">
        <textarea name="text" rows="5" cols="50" placeholder="Enter your text here..."></textarea><br><br>
        <button type="submit">Analyze</button>
    </form>

    {% if result %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0:
            result = "😊 Positive"
        elif sentiment < 0:
            result = "😞 Negative"
        else:
            result = "😐 Neutral"
    return render_template_string(HTML_PAGE, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


