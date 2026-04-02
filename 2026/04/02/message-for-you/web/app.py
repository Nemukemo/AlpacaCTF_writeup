from flask import Flask, session
import os
import secrets 

FLAG = os.environ.get("FLAG", "Alpaca{**REDACTED**}")

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

MESSAGE = f"""
Roses are red,
Violets are blue,
I've hidden a flag
In a session for you: {FLAG}
""".strip()

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message for You!</title>
</head>
<body>
    <p>I've got a message for you.</p>
    <p>It's hidden somewhere around here...</p>
</body>
</html>
""".strip()

@app.get("/")
def index():
    session["message"] = MESSAGE
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
