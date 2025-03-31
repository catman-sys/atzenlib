from flask import Flask, request, render_template

app = Flask(__name__)

eintraege = []  # Hier speichern wir die Gästebucheinträge

@app.route("/")
def formular():
    return render_template("formular.html", eintraege=eintraege)

@app.route("/eintrag", methods=["POST"])
def eintrag():
    name = request.form["name"]
    nachricht = request.form["nachricht"]
    eintraege.append({"name": name, "nachricht": nachricht})
    return render_template("formular.html", eintraege=eintraege)

if __name__ == "__main__":
    app.run(debug=True)
