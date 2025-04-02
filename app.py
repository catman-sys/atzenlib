from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        # Speichern in Textdatei
        with open('entries.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name}: {message}\n')

    # Einträge aus Datei laden
    try:
        with open('entries.txt', 'r', encoding='utf-8') as file:
            entries = file.readlines()
    except FileNotFoundError:
        entries = []

    return render_template_string('''
        <h1>Atzenblog</h1>
        <form method="post">
            <label>Name:</label><br>
            <input name="name"><br>
            <label>Nachricht:</label><br>
            <textarea name="message"></textarea><br>
            <button type="submit">Eintragen</button>
        </form>
        <hr>
        <h2>Einträge:</h2>
        <ul>
            {% for entry in entries %}
                <li>{{ entry }}</li>
            {% endfor %}
        </ul>
    ''', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
