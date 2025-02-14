import http.server
import socketserver

html_content = """
<!DOCTYPE html>
<html lang='sv'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Alla hjärtans dag ❤️</title>
    <style>
        body {
            text-align: center;
            background-color: #ffe6f2;
            font-family: 'Pacifico', cursive;
            position: relative;
            overflow: hidden;
        }
        .container {
            margin-top: 50px;
            position: relative;
            z-index: 10;
        }
        h1 {
            color: #ff4081;
            font-size: 3em;
            animation: glow 2s infinite alternate;
        }
        .message {
            font-size: 1.8em;
            color: #d63384;
            font-weight: bold;
        }
        .button {
            background-color: #ff4d4d;
            color: white;
            padding: 15px 30px;
            font-size: 1.5rem;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
            animation: pulse 2s infinite;
        }
        .button:hover {
            background-color: #e60000;
        }
        @keyframes glow {
            0% { text-shadow: 0 0 10px #ff4081; }
            100% { text-shadow: 0 0 20px #ff4081, 0 0 30px #ff77a9; }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        .floating-emoji {
            position: absolute;
            font-size: 2.5em;
            animation: float 5s infinite ease-in-out;
        }
        @keyframes float {
            0% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class='container'>
        <h1>Emelie, Vill du bli min Valentine? 💖</h1>
        <p class='message'>Du är mitt hjärta, mitt allt, min eviga kärlek! 💞</p>
        <p class='message'>Jag älskar dig mer än ord kan säga, Emelie! 💗</p>
        <button class='button' onclick="alert('Jag älskar dig, Emelie! ❤️ Din Adam')">JA! 💕</button>
    </div>
    <script>
        const emojis = ['❤️', '💖', '🌸', '💐', '🧸', '💞', '💗', '💕', '🌹', '😍'];
        for (let i = 0; i < 30; i++) {
            let emoji = document.createElement('div');
            emoji.className = 'floating-emoji';
            emoji.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            emoji.style.left = Math.random() * 100 + 'vw';
            emoji.style.top = Math.random() * 100 + 'vh';
            emoji.style.animationDuration = (Math.random() * 2 + 3) + 's';
            document.body.appendChild(emoji);
        }
    </script>
    <audio autoplay loop>
        <source src='https://www.bensound.com/bensound-music/bensound-love.mp3' type='audio/mpeg'>
        Din webbläsare stöder inte ljuduppspelning.
    </audio>
</body>
</html>
"""

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servern körs på http://localhost:{PORT}")
    httpd.serve_forever()
