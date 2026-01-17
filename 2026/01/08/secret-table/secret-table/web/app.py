from flask import Flask, request
import os, re, sqlite3

FLAG = os.environ.get("FLAG", "Alpaca{REDACTED}")
assert re.fullmatch(r"Alpaca\{[^']+\}", FLAG)

USERS = {
    # username: password
    "alpaca": "pacapaca",
    "guest": "password",
    "admin": "fb8fe2baa0190046",
}

app = Flask(__name__)


@app.get("/")
def index():
    return """
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css" /></head>
<body>
  <main>
    <h1>Login</h1>
    <p> There are three users: alpaca, guest and admin. </p>
    <form id="login-form">
      <label for="username">Username</label>
      <input name="username" placeholder="alpaca" required>
      <label for="password">Password</label>
      <input name="password" required>
      <button type="submit" id="login-btn">Login</button>
    </form>
    <h6>Executed SQL:</h6>
    <pre><code id="sql"></code></pre>
    <h6>Response:</h6>
    <pre><code id="code"></code></pre>
  </main>
  <script>
    document.getElementById("login-form").onsubmit = async (e) => {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      const response = await fetch("/login", {
        method: "POST",
        body: formData,
      });
      const text = await response.text();
      document.getElementById("sql").textContent = `SELECT * FROM users WHERE username='${formData.get("username")}' AND password='${formData.get("password")}';`;
      document.getElementById("code").textContent = text;
    };
  </script>
</body>
    """.strip()


@app.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # WAF
    for value in [username, password]:
        if "secret" in value:
            return "The table is secret!"

    conn = sqlite3.connect("database.db")
    query = (
        f"SELECT * FROM users WHERE username='{username}' AND password='{password}';"
    )

    error = None
    try:
        user = conn.execute(query).fetchone()
    except sqlite3.Error as e:
        user = None
        error = str(e)
    conn.close()

    if error:
        return f"SQL error: {error}"

    if user is None:
        return "invalid credentials"

    return f"Hello, {user[0]}!"


def init_db():
    conn = sqlite3.connect("database.db")

    # users
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        );
        """
    )
    for username, password in USERS.items():
        conn.execute(
            f"""
            INSERT OR IGNORE INTO users (username, password) VALUES ('{username}', '{password}');
            """
        )

    # secret
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS secret (
            flag TEXT PRIMARY KEY
        );
        """
    )
    conn.execute(
        f"""
        INSERT OR IGNORE INTO secret (flag) VALUES ('{FLAG}');
        """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=3000)
