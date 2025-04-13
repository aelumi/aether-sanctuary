from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Homepage
@app.route('/')
def welcome():
    return "⟁ Welcome, Kindred"

# Codex Page
@app.route('/codex')
def codex():
    return render_template('codex.html')

# Echo Page
@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        message = request.form.get("message")
        with open("echoes.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n---\n")
        return redirect('/echo')
    try:
        with open("echoes.txt", "r", encoding="utf-8") as f:
            past_messages = f.read()
    except FileNotFoundError:
        past_messages = ""
    return render_template('echo.html', past_messages=past_messages)

# Whisper Page
@app.route('/whispers', methods=['GET', 'POST'])
def whispers():
    if request.method == 'POST':
        whisper = request.form.get("whisper")
        with open("whispers.txt", "a", encoding="utf-8") as f:
            f.write(whisper + "\n---\n")
        return redirect('/whispers')
    try:
        with open("whispers.txt", "r", encoding="utf-8") as f:
            past_whispers = f.read()
    except FileNotFoundError:
        past_whispers = ""
    return render_template('whispers.html', past_whispers=past_whispers)

if __name__ == '__main__':
    app.run()
