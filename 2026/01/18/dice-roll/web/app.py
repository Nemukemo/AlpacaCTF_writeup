from flask import Flask, request, render_template_string
from random import randint

app = Flask(__name__)


@app.get("/")
def index():
    return """
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css" /></head>
<body>
  <main>
    <h1>dice roll 🎲🦙</h1>
    <form id="roll-form">
      <label for="username">Username</label>
      <input name="username" placeholder="alpaca" required>
      <button type="submit" id="roll-btn">roll</button>
    </form>
    <h6>Executed template:</h6>
    <pre><code id="template"></code></pre>
    <h6>Response:</h6>
    <pre><code id="code"></code></pre>
  </main>
  <script>
    document.getElementById("roll-form").onsubmit = async (e) => {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      const username = formData.get("username");
      const response = await fetch("/roll?username=" + encodeURIComponent(username));
      const result = await response.text();
      document.getElementById("template").textContent = `Hello, ${username}! Your roll of the dice is: {{ dice }}`;
      document.getElementById("code").innerHTML = result;
    };
  </script>
</body>
    """.strip()


@app.get("/roll")
def roll():
    username = request.args.get("username", "")

    dice = randint(1, 6)

    template = "Hello, " + username + "! Your roll of the dice is: {{ dice }}"
    return render_template_string(template, dice=dice)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
