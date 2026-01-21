from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Current Time</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 100px;">
    <h1>Current Time</h1>
    <h2>{{ time }}</h2>
    <button onclick="location.reload()">Refresh Time</button>
</body>
</html>
"""

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML, time=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
