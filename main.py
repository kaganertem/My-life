# Import
from flask import Flask, render_template,request, redirect
from datetime import datetime




app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    email = request.form.get('email')
    text = request.form.get('text')

    with open('feedback.txt', 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Email: {email}\nComment: {text}\n{'-'*40}\n")
    # Geri bildirim işleme kodu buraya eklenebilir
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
