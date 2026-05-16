from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
notes = []
@app.route("/")
def index():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    if title and content:
        notes.append({
            "title": title,
            "content": content
        })

    return redirect(url_for("index"))

@app.route("/edit/<int:note_id>")
def edit_note(note_id):
    if 0 <= note_id < len(notes):
        return render_template(
            "edit.html",
            note=notes[note_id],
            note_id=note_id
        )
    return redirect(url_for("index"))

@app.route("/update/<int:note_id>", methods=["POST"])
def update_note(note_id):
    if 0 <= note_id < len(notes):
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if title and content:
            notes[note_id] = {
                "title": title,
                "content": content
            }

    return redirect(url_for("index"))

@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)