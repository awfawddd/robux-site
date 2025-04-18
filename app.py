
import os
from flask import Flask, render_template_string

app = Flask(__name__)

URL_PATH = "/100%_download_no_virus_free.exe-free_ultimate_version.0765"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Free Robux Generator</title>
    <style>
        body {
            background-color: black;
            color: white;
            text-align: center;
            font-family: Arial, sans-serif;
            margin-top: 80px;
        }
        button {
            font-size: 24px;
            background: limegreen;
            padding: 20px 40px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        #message {
            margin-top: 30px;
            font-size: 28px;
            color: gold;
        }
        #downloads {
            display: none;
            margin-top: 20px;
        }
        a {
            display: block;
            color: cyan;
            font-size: 18px;
            margin: 10px;
        }
    </style>
    <script>
        function showWinMessage() {
            document.getElementById('message').innerText = "🎉 You won 1,000,000 Robux! 🎉";
            document.getElementById('downloads').style.display = "block";
        }
    </script>
</head>
<body>
    <h1>💸 Free Robux Generator 💸</h1>
    <p>Click the button below to generate Robux!</p>
    <button onclick="showWinMessage()">Generate Robux</button>
    <div id="message"></div>
    <div id="downloads">
        <h2>🕹️ Old Roblox Versions Unlocked!</h2>
        <a href="/static/roblox_2006.zip" download>📥 Download Roblox 2006</a>
        <a href="/static/roblox_2012.ipa" download>📥 Download Roblox 2012</a>
        <a href="/static/roblox_2015.zip" download>📥 Download Roblox 2015</a>
        <a href="/static/100%_download_no_virus_free.exe-free_ultimate_version.0765" download>
            🦠 Download 100%_download_no_virus_free.exe-free_ultimate_version.0765
        </a>
    </div>
</body>
</html>
"""

@app.route(URL_PATH)
def robux_site():
    return render_template_string(HTML_PAGE)

@app.route("/")
def home():
    return "Vai su " + URL_PATH

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
