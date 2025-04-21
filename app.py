from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
notes = []

@app.route("/")
def home():
    return render_template("home.html", notes=notes)

@app.route("/add", methods=['GET', 'POST'])
def add_note():
    if request.method == "GET":
        return render_template("note_form.html")
    elif request.method == "POST":
        note = {}
        note_title = request.form.get("title")
        note_content = request.form.get("content")
        note["title"] = note_title
        note["content"] = note_content
        notes.append(note)
        return redirect(url_for("home"))

@app.route("/my-notes", methods=['GET'])
def my_notes():
    return render_template("my_notes.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)